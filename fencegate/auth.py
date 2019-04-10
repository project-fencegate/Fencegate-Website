import functools
from flask import Blueprint, g, render_template, session, request, url_for, flash

auth = Blueprint('auth', __name__, url_prefix="/auth")