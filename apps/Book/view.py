from apps.Book import bp_book
from flask import render_template


@bp_book.route('/uu', methods=['GET', 'POST'])
def ss():
    return render_template("index.html")
