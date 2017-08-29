from flask import redirect, render_template, request, url_for, Blueprint, flash
from project import db

tags_blueprint = Blueprint(
    'tags',
    __name__,
    template_folder='templates'
)

@tags_blueprint.route('/', methods =["GET", "POST"])
def index():
    user =""
    # if request.method == "POST":
    #     #form = MessageForm()
    #     if form.validate():
    #         new_message = Message(form.text.data, user.id)
    #         db.session.add(new_message)
    #         db.session.commit()
    #         flash('Tag Created!')
    #         return redirect(url_for('messages.index', user_id=user.id))
    #     return render_template('messages/new.html', form=form, user=user)
    return render_template('tags/index.html', user=user)
