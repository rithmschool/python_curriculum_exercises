from flask import redirect, render_template, request, url_for, Blueprint, flash, session, g
from project.users.forms import UserForm, LoginForm
from project.models import User
from project import db, bcrypt
from project.decorators import ensure_authenciated, ensure_correct_user, prevent_login_signup
from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_blueprint.before_request
def current_user():
    if session.get('user_id'):
        g.current_user = User.query.get(session['user_id'])
    else:
        g.current_user = None

@ensure_authenciated
@users_blueprint.route('/')
def index():
    return render_template('users/index.html', users=User.query.all())

@users_blueprint.route('/login', methods = ["GET", "POST"])
@prevent_login_signup
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        authenticated_user = User.authenticate(form.username.data, form.password.data)
        if authenticated_user:
            session['user_id'] = authenticated_user.id
            flash("You are now logged in!")
            return redirect(url_for('users.index'))
        else:
            flash("Invalid Credentials")
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)

@users_blueprint.route('/signup', methods =["GET", "POST"])
@prevent_login_signup
def signup():
    form = UserForm(request.form)
    if request.method == "POST":
        if form.validate():
            try:
                new_user = User(
                    form.first_name.data,
                    form.last_name.data,
                    form.username.data,
                    form.password.data,
                    )
                db.session.add(new_user)
                db.session.commit()
                session['user_id'] = new_user.id
                flash('User Created!')
                return redirect(url_for('users.index'))
            except IntegrityError as e:
                flash("Username already taken")
                return render_template('users/signup.html', form=form)
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/<int:id>/edit')
@ensure_authenciated
@ensure_correct_user
def edit(id):
    owner=User.query.get(id)
    form = UserForm(obj=owner)
    return render_template('users/edit.html', form=form, owner=owner)

@users_blueprint.route('/<int:id>', methods =["GET", "PATCH", "DELETE"])
@ensure_authenciated
@ensure_correct_user
def show(id):
    found_user = User.query.get(id)
    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            found_user.first_name = form.first_name.data
            found_user.last_name = form.last_name.data
            found_user.username = form.username.data
            found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            db.session.add(found_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        return render_template('users/edit.html', form=form, owner=found_user)
    if request.method == b"DELETE":
        db.session.delete(found_user)
        db.session.commit()
        session.pop('user_id')
        flash('User Deleted')
        return redirect(url_for('users.login'))
    return render_template('users/show.html', owner=found_user)


@users_blueprint.route('/logout')
@ensure_authenciated
def logout():
    session.pop('user_id')
    flash('Logged Out!')
    return redirect(url_for('users.login'))
