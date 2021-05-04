from flask import render_template, request, redirect, url_for, abort
from ..models import User, Review


@main.route('/user/<uname>')
def profile(uname):
    """
    Route that directs users to their profiles
    """
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user)