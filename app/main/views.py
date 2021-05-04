from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..requests import get_genre, get_genre_tracks, get_radio_tracks

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting different genre
    pop=get_genre()
    gentracks = get_genre_tracks()

    return render_template('index.html', pop=pop, gentracks=gentracks)

@main.route('/genre/music')
def genre_music():
    gentracks = get_genre_tracks()

    for track in gentracks:
        trackid=track.id
        tracks = get_radio_tracks(trackid)

        return render_template('playlist.html',tracks=tracks)

