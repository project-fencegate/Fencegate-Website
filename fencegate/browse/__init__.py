from flask import Blueprint, render_template, redirect, url_for

browse = Blueprint('browse', __name__, url_prefix='/browse')


@browse.route('/')
def index():
    return redirect(url_for('.view_plugins'))


@browse.route('/plugins')
def view_plugins():
    return render_template('browse/plugins.html')
