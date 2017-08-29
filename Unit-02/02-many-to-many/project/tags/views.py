from flask import Blueprint, render_template, redirect, url_for, request
from project.tags.forms import TagForm, DeleteTagForm
from project.models import Tag, Message
from project import db

tags_blueprint = Blueprint(
    'tags',
    __name__,
    template_folder="templates"
)

@tags_blueprint.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        form = TagForm(request.form)
        form.set_choices()
        if form.validate_on_submit():
            new_tag = Tag(form.text.data)
            for message in form.messages.data:
                new_tag.messages.append(Message.query.get(message))
            db.session.add(new_tag)
            db.session.commit()
        else:
            return render_template('tags/new.html', form=form)
    return render_template('tags/index.html', tags=Tag.query.all())


@tags_blueprint.route('/new', methods=["GET"])
def new():
    form = TagForm()
    form.set_choices()
    return render_template('tags/new.html', form=form)


@tags_blueprint.route('/<int:id>/edit', methods=["GET"])
def edit(id):
    tag = Tag.query.get(id)
    messages = [message.id for message in tag.messages]
    edit_form = TagForm(messages=messages)
    delete_form = DeleteTagForm(messages=messages)
    edit_form.set_choices()
    edit_form.text.data = tag.text
    return render_template('tags/edit.html', tag=tag, form=edit_form, delete_form=delete_form)


@tags_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_tag=Tag.query.get(id)
    form = DeleteTagForm(request.form)
    if request.method == b"DELETE":
        if form.validate():
            db.session.delete(found_tag)
            db.session.commit()
        return redirect(url_for('tags.index'))
    if request.method == b"PATCH":
        form = TagForm(request.form)
        form.set_choices()
        if form.validate():
            found_tag.text = form.text.data
            found_tag.messages = []
            for message in form.messages.data:
                found_tag.messages.append(Message.query.get(message))
            db.session.add(found_tag)
            db.session.commit()
            return redirect(url_for('tags.index'))
        else:
            return render_template('tags/edit.html', form=form)
    return render_template('tags/show.html', tag=found_tag)
