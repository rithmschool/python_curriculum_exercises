from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.messages.forms import MessageForm
from project.models import User
from project.models import Message
from project import db
from project.decorators import ensure_authenciated, ensure_correct_user

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages_blueprint.route('/', methods =["GET", "POST"])
@ensure_authenciated
def index(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        form = MessageForm(request.form)
        if form.validate():
            new_message = Message(form.content.data, user.id)
            db.session.add(new_message)
            db.session.commit()
            flash('Message Created!')
            return redirect(url_for('messages.index', user_id=user.id))
        return render_template('messages/new.html', form=form, user=user)
    return render_template('messages/index.html', user=user)

@messages_blueprint.route('/new')
@ensure_authenciated
@ensure_correct_user
def new(user_id):
    user = User.query.get(user_id)
    form = MessageForm()
    return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route('/<int:id>/edit')
@ensure_authenciated
@ensure_correct_user
def edit(user_id,id):
    message=Message.query.get(id)
    form = MessageForm(obj=message)
    return render_template('messages/edit.html', form=form, message=message)

@messages_blueprint.route('/<int:id>', methods =["GET", "PATCH", "DELETE"])
@ensure_authenciated
@ensure_correct_user
def show(user_id,id):
    found_message = Message.query.get(id)
    if request.method == b"PATCH":
        form = MessageForm(request.form)
        if form.validate():
            found_message.content = form.content.data
            db.session.add(found_message)
            db.session.commit()
            flash('Message Updated!')
            return redirect(url_for('messages.index', user_id=found_message.user.id))
        return render_template('messages/edit.html', form=form, message=found_message)
    if request.method == b"DELETE":
        db.session.delete(found_message)
        db.session.commit()
        flash('Message Deleted!')
        return redirect(url_for('messages.index', user_id=user_id))
    return render_template('messages/show.html', message=found_message)



