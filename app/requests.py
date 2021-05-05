import urllib.request,json
from .models import Genre, GenreTrack, radioTrack
from .models import Chart, Artist  

#Getting the quotes base url
chart_url = None
search_url = None
base_url = None
base_playlist_url= None
base_tracks_url=None

def configure_request(app):
    global base_url, base_playlist_url, chart_url, artist_url, search_url
    chart_url = app.config["MUSIC_CHART_URL"]
    search_url = app.config["SEARCH_URL"]

    base_url = app.config['GENRE_API_BASE_URL']
    base_playlist_url = app.config['PLAYLIST_API_BASE_URL']
    base_tracks_url = app.config['TRACK_API_BASE_URL']


# Get genres
def get_genre():
    '''
    Function that gets the json response to the url request
    '''
    
    get_genre_url = base_url

    with urllib.request.urlopen(get_genre_url) as url:
        get_genre_data = url.read()
        get_genre_response = json.loads(get_genre_data)

        genre_results = None

        if get_genre_response['data']:
            genre_results_list = get_genre_response['data']
            genre_results = process_genre_results(genre_results_list)

    return genre_results


def process_genre_results(genre_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    genre_results = []
    for genre_item in genre_list:
        id = genre_item.get('id')
        title = genre_item.get('name')
        poster = genre_item.get('picture_big')

        if poster:
            genre_object = Genre(id, title,poster)
            genre_results.append(genre_object)

    return genre_results

#Get Radio

def get_genre_tracks():
    '''
    Function that gets the json response to the url request
    '''
    get_playlist_url=base_playlist_url 
    with urllib.request.urlopen(get_playlist_url) as url:
        get_genre_track_data = url.read()
        get_genre_track_response = json.loads(get_genre_track_data)

        genre_track_results = None

        if get_genre_track_response['data']:
            genre_track_results_list = get_genre_track_response['data']
            genre_track_results = process_track_results(genre_track_results_list)

    return genre_track_results


def process_track_results(genre_track_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    genre_track_results = []
    for genre_track_item in genre_track_list:
        id = genre_track_item.get('id')
        title = genre_track_item.get('title')
        picture = genre_track_item.get('picture_medium')
        playlist = genre_track_item.get('tracklist')
        

        genre_track_object = GenreTrack(id,title,picture,playlist)
        genre_track_results.append(genre_track_object)

    return genre_track_results

#Get Playlist Tracks

def get_radio_tracks(trackid):
    '''
    Function that gets the json response to the url request
    '''
    get_radiotracks_url = 'https://api.deezer.com/radio/{}/tracks'.format(trackid)
    print(get_radiotracks_url)
    with urllib.request.urlopen(get_radiotracks_url) as url:
        get_track_data = url.read()
        get_radio_response = json.loads(get_track_data)

        track_results = None

        if get_radio_response['data']:
            track_results_list = get_radio_response['data']
            track_results = process_radio_track_results(track_results_list)

    return track_results


def process_radio_track_results(track_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    track_results = []
    for track_item in track_list:
        id=track_item.get('id')
        title = track_item.get('title')
        artist = track_item.get('artist')
        album = track_item.get('album')
        preview=track_item.get('preview')
        
        track_object = radioTrack(id,title, artist, album,preview)
        track_results.append(track_object)

    return track_results


def get_chart():

  with urllib.request.urlopen(chart_url) as url:
    get_chart_data = url.read()
    chart_data_response = json.loads(get_chart_data)

    chart_results = None

    if chart_data_response['data']:
      chart_results_list = chart_data_response['data']
      chart_results = process_results(chart_results_list)
  return chart_results


def process_results(chart_list):

  chart_results = []
  for track_item in chart_list:
    id = track_item.get('id')
    title = track_item.get('title')
    link = track_item.get('link')
    preview = track_item.get('preview')
    picture = track_item.get('artist')
    position = track_item.get('position')
    name = track_item.get('artist')

    chart_object = Chart(id, title, link, preview, picture, position, name)
    chart_results.append(chart_object)

  return chart_results

def process_artist(artist_list):

  artist_results = []
  for track_item in artist_list:
    id = track_item.get('id')
    title = track_item.get('title')
    name = track_item.get('artist')
    preview = track_item.get('preview')
    picture = track_item.get('artist')

    artist_object = Artist(id, title, name, preview,picture)
    artist_results.append(artist_object)

  return artist_results


def search_artist(artist_name):
  search_artist_url = search_url.format(artist_name)
  with urllib.request.urlopen(search_artist_url) as url:
    search_artist_data = url.read()
    search_artist_response = json.loads(search_artist_data)

    search_artist_results = None

    if search_artist_response["data"]:
      search_artist_results_list = search_artist_response["data"]
      search_artist_results = process_artist(search_artist_results_list)

  return search_artist_results