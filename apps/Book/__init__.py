from flask import Blueprint, render_template

bp_book = Blueprint(name='book', import_name=__name__)

from apps.Book import view

