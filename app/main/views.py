from flask_login import login_required, current_user
from . import main
from ..models import User,Favorite
from ..requests import get_genre, get_genre_tracks, get_radio_tracks, get_chart, search_artist
from flask import url_for, redirect,request,render_template,abort,flash


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
        return render_template('index.html', tracks=track,pop=pop,gentracks=gentracks)
   

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


@main.route('/like/<int:id>', methods=['POST', 'GET'])
def favourite_top(id):
    trackid_list=[]
    track = get_chart()
    for tracks in track:
        track_id = tracks.id
        title=tracks.title 
        preview=tracks.preview
        if track_id == id:
            new_like=Favorite(track_id=track_id,title=title,preview=preview)
            new_like.save_favourite()
        else:
            print("no")
        
    return redirect(url_for('main.index', id=id))

@main.route('/favtrack/<int:id>', methods=['POST', 'GET'])
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
                new_like=Favorite(track_id=track_id,title=title,preview=preview)
                new_like.save_favourite()
    
        return redirect(url_for('main.index',id=id))
