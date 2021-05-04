from flask import url_for,redirect,request,render_template,abort,flash
from .import main
from ..models import User
from flask_login import current_user,login_required
from ..requests import get_chart,search_artist


@main.route('/')
def index():

  track = get_chart()
  # tracks = get_tracks(4, get_chart)

  search_artist = request.args.get('artist_query')
  if search_artist:
    return redirect(url_for('.search', artist_name=search_artist))
  else:
    return render_template('index.html', tracks=track)


@main.route('/search/<artist_name>')
def search(artist_name):
  '''
  view function that displays articles search results
  '''
  artist_name_list = artist_name.split(" ")
  artist_name_format = "+".join(artist_name_list)
  searched_artist = search_artist(artist_name_format)
  title = f"{artist_name}'s search results"

  return render_template('search.html', artists=searched_artist)