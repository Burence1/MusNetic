from flask import url_for,flash,redirect,render_template,request
from .import auth
from flask_login import login_user,logout_user,login_required
from app.models import User
from ..import db
from .forms import RegistrationForm,LoginForm


@auth.route("/register",methods=["GET","POST"])
def register():
  form=RegistrationForm()
  if form.validate_on_submit():
    user=User(username=form.username.data,email=form.email.data,password=form.password.data)
    user.save_user()

    return redirect(url_for('auth.login'))

  title="Registration"
  return render_template('auth/register.html',registration_form=form,title=title)

@auth.route("/login",methods=["GET","POST"])
def login():
  form=LoginForm()
  if form.validate_on_submit():
    user=User.query.filter_by(username=form.username.data).first()
    if user is not None and user.password_verification(form.password.data):
      login_user(user,form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))

    flash("Invalid username/password")

  title="Login"
  return render_template('auth/login.html',login_form=form,title=title)


@auth.route("/logout")
@login_required
def logout():
  logout_user()
  flash("Logged out")
  return redirect(url_for("main.index"))
