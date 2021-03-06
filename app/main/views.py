from flask_login import login_required, current_user
from . import main
from ..models import User,Favorite,Playlist
from ..requests import get_genre, get_genre_tracks, get_radio_tracks, get_chart, search_artist
from flask import url_for, redirect,request,render_template,abort,flash
from .. import db, photos
from .forms import UpdateProfile
from flask import jsonify
from flask_cors import CORS,cross_origin
from dotenv import load_dotenv


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    track = get_chart()
    #Getting different genre
    pop = get_genre()
    gentracks = get_genre_tracks()

  # tracks = get_tracks(4, get_chart)

    search_artist = request.args.get('artist_query')
    if search_artist:
        return redirect(url_for('.search', artist_name=search_artist))
    else:
        return render_template('index.html', tracks=track, pop=pop, gentracks=gentracks)
   

@main.route('/genre/music')
def genre_music():
    gentracks = get_genre_tracks()

    for track in gentracks:
        trackid=track.id
        tracks = get_radio_tracks(trackid)

        search_artist = request.args.get('artist_query')
        if search_artist:
            return redirect(url_for('.search', artist_name=search_artist))
        else:
            return render_template('playlist.html',tracks=tracks)

@main.route('/search/<artist_name>')
def search(artist_name):
  '''
  view function that displays articles search results
  '''
  artist_name_list = artist_name.split(" ")
  artist_name_format = "+".join(artist_name_list)
  searched_artist = search_artist(artist_name_format)
  title = f"{artist_name}'s search results"

  search_artistOne = request.args.get('artist_query')

  if search_artistOne:
      return redirect(url_for('.search', artist_name=search_artistOne))
  else:
      return render_template('search.html', artists=searched_artist)


@main.route('/playlist/<int:id>', methods=['POST', 'GET'])
@login_required
def playlist_chart(id):
    track = get_chart()
    for tracks in track:
        track_id = tracks.id
        title = tracks.title
        user_id=current_user._get_current_object().id
        preview = tracks.preview
        if track_id == id:
            new_playlist = Playlist(track_id=track_id,title=title,user_id=user_id, preview=preview)
            new_playlist.save_playlist()
    return redirect(url_for('main.index', id=id))


@main.route('/playlist_radio/<int:id>', methods=['POST', 'GET'])
@login_required
def playlist_radio(id):
    gentracks = get_genre_tracks()
    for track in gentracks:
        trackid = track.id
        tracks = get_radio_tracks(trackid)
        for items in tracks:
            track_id = items.id
            title = items.title
            user_id = current_user._get_current_object().id
            preview = items.preview
            if track_id == id:
                new_playlist = Playlist(
                    track_id=track_id, title=title, user_id=user_id, preview=preview)
                new_playlist.save_playlist()
        return render_template('playlist.html', tracks=tracks)

@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def favourite_top(id):
    trackid_list=[]
    track = get_chart()
    for tracks in track:
        track_id = tracks.id
        title=tracks.title 
        preview=tracks.preview
        if track_id == id:
            new_like = Favorite(track_id=track_id, title=title, preview=preview,user_id=current_user._get_current_object().id)
            new_like.save_favourite()
    return redirect(url_for('main.index', id=id))

@main.route('/favtrack/<int:id>', methods=['POST', 'GET'])
@login_required
def favourite_radio(id):
    gentracks = get_genre_tracks()
    for track in gentracks:
        trackid = track.id
        tracks = get_radio_tracks(trackid)
        for items in tracks:
            track_id = items.id
            title = items.title
            preview = items.preview

            if track_id == id:
                new_like = Favorite(track_id=track_id, title=title, preview=preview,
                                    user_id=current_user._get_current_object().id)
                new_like.save_favourite()
        return render_template('playlist.html', tracks=tracks)
        

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id
    favorite = Favorite.query.filter_by(user_id=user_id).all()
    playlist = Playlist.query.filter_by(user_id=user_id).all()


    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user,favorite=favorite, user_id=user_id,playlist=playlist)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route("/upload", methods=['POST'])
def upload_file():
  app.logger.info('in upload route')

  cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'),
                    api_secret=os.getenv('API_SECRET'))
  upload_result = None
  if request.method == 'POST':
    file_to_upload = request.files['file']
    app.logger.info('%s file_to_upload', file_to_upload)
    if file_to_upload:
      upload_result = cloudinary.uploader.upload(file_to_upload)
      app.logger.info(upload_result)
      return jsonify(upload_result)
