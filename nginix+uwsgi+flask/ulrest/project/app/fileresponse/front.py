from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound



front = Blueprint('front', __name__,
                        template_folder='templates')

@front.route('/docktest')
def sampleui():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
@front.route('/sockettest')
def samplesock():
    try:
        return render_template('socket.html')
    except TemplateNotFound:
        abort(404)
