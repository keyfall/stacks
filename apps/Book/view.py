from apps.Book import bp_book
from flask import render_template
from utils.response import jsonify_response


@bp_book.route('/uu', methods=['GET', 'POST'])
def ss():
    return render_template("index.html")


@bp_book.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template("upload.html")

@bp_book.route('/upload_book', methods=['GET', 'POST'])
def upload_book():
    print("成功")
    return "sss"