from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.messages.forms import MessageForm
from project.models import User, Message, Tag
from project import db

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages_blueprint.route('/', methods =["GET", "POST"])
def index(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        form = MessageForm(request.form)
        form.set_choices()
        if form.validate():
            new_message = Message(form.text.data, user.id)
            for tag in form.tags.data:
                new_message.messages.append(Tag.query.get(tag))
            db.session.add(new_message)
            db.session.commit()
            flash('Message Created!')
            return redirect(url_for('messages.index', user_id=user.id))
        return render_template('messages/new.html', form=form, user=user)
    return render_template('messages/index.html', user=user)

@messages_blueprint.route('/new')
def new(user_id):
    user = User.query.get(user_id)
    form = MessageForm()
    form.set_choices()
    return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id,id):
    message=Message.query.get(id)
    tags = [tag.id for tag in message.tags]
    form = MessageForm(tags=tags)
    form.set_choices()
    form.text.data = message.text
    return render_template('messages/edit.html', form=form, message=message)

@messages_blueprint.route('/<int:id>', methods =["GET", "PATCH", "DELETE"])
def show(user_id,id):
    found_message = Message.query.get(id)
    if request.method == b"PATCH":
        form = MessageForm(request.form)
        form.set_choices()
        if form.validate():
            found_message.text = form.text.data
            found_message.tags = []
            for tag in form.tags.data:
                found_message.tags.append(Tag.query.get(tag))
            db.session.add(found_message)
            db.session.add(found_message)
            db.session.commit()
            return redirect(url_for('messages.index', user_id=found_message.user.id))
        return render_template('messages/edit.html', form=form, message=found_message)
    if request.method == b"DELETE":
        db.session.delete(found_message)
        db.session.commit()
        return redirect(url_for('messages.index', user_id=user_id))
    return render_template('messages/show.html', message=found_message)
