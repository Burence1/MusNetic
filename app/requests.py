import urllib.request,json
from .models import Chart, Artist

chart_url = None
search_url = None


def configure_request(app):
  global chart_url, artist_url, search_url
  chart_url = app.config["MUSIC_CHART_URL"]
  search_url = app.config["SEARCH_URL"]


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