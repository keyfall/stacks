from flask import render_template,request,flash,url_for,redirect
import re

from flask_login import login_required, current_user
from apps.Book import bp_book
from utils.response import jsonify_response
from .book import Book
from utils.db import db
import datetime
import os

@bp_book.route('/search_book/<string:book_name>', methods=['GET', 'POST'])
def search_book(book_name):
    if request.method == "GET":
        return render_template("index.html")
    books = Book.query.filter_by(book_name=book_name,verify='1',logic_delete='0').all()
    if books:
        return jsonify_response(data=books,code=200)
    return jsonify_response(code=400, msg="错误的文件名称 '{}'".format(book_name))


def is_valid_filename(filename):
    pattern = r'^.+\.\w+$'
    # a-zA-Z0-9：数字，大小写字母
    # ?:表示可有可无,\s、-、_：空格、下划线、减号
    # [a-zA-Z0-9]+：循环一次或多次，格式为“字母数字字母数字”，反复出现
    # \.[a-zA-Z]{2,4}$：最后以.连接，后接2到4位字母结尾。
    return re.match(pattern, filename)

@bp_book.route('/upload_book', methods=['GET', 'POST'])
def upload_book():
    if request.method == "GET":
        return render_template("upload.html")
    #只能在request.files里找文件，file是前端formdata中对应文件设置的key值，可以修改，后天也要修改，否则找不到
    #file_val里面的content_length,content_type都为空,我以为没有传成功，后来尝试保存，发现保存成功就好了
    file_val = request.files['file']
    #判断一下上传的名字是否符合规范，是否是一个名字.类型这种格式

    if not is_valid_filename(file_val.filename):
         flash("错误的文件名称 '%s'".format(file_val.filename))
         # 这里不能使用jsonify，因为之前用的是ajax，所以使用flask无法显现，试试跳转和重定向，不行搜百度
         return jsonify_response(code=400, msg="错误的文件名称 '{}'".format(file_val.filename))
    # odst = "d:\\projects\\stacks\\books\\"

    #通过文件名验证是否存在
    #后面和用户绑定后，当前用户下的文件不能重复

    odst = "e:\\projects\\stacks\\books\\"
    dst = odst+file_val.filename
    if not os.path.exists(odst):
        os.makedirs(odst)
    file_val.save(dst)

    book = Book(book_name=file_val.filename.split(".")[0],book_url=dst, create_time=datetime.date.today())
    db.session.add(book)
    #需要把信息存到数据库中
    # db.session.commit()
    return jsonify_response(msg="ok")

@bp_book.route('/dele/<int:id>', methods=['POST'])
@login_required
def del_book(id):
    book = Book.query.get_or_404(id)
    if book:
        book.logic_delete = "1"
        db.session.commit()
        # dst = book.book_url
        #暂时不删除文件
        # try:
        #     if os.path.exists(dst):
        #         os.remove(dst)
        #     print("File Deleted Successfully")
        # except OSError:
        #     return jsonify_response(err=500, msg="File Not Found or Permission Denied")
        return jsonify_response()

@bp_book.route('/verify/<int:id>', methods=['POST'])
@login_required
def verify_book(id):
    book = Book.query.get_or_404(id)
    if book:
        book.verify = "1"
        db.session.commit()
        return jsonify_response()
    return jsonify_response(code=400,msg="没有此文件")

@bp_book.route('book_pagin/<int:page>')
@login_required
def pagination(page):
    if(page==None):
        page=1
    pagination = Book.query.order_by(Book.create_time.desc()).paginate(page,10,error_out=False)
    books=pagination.items
    context = {
        "books":books,
        "uname":current_user.uname,
        "pagination": pagination
    }

    return render_template("audit.html", **context)