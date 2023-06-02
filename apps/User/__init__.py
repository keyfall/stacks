from flask import Blueprint, render_template

bp_user = Blueprint(name='user', import_name=__name__)

from apps.User import view