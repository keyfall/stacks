from flask import render_template,request,flash,url_for,redirect
import re

from apps.Book import bp_book
from utils.response import jsonify_response
from .book import Book
from utils.db import db
import datetime

@bp_book.route('/uu', methods=['GET', 'POST'])
def ss():
    return render_template("index.html")

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

    dst = "d:\\projects\\stacks\\books\\"+file_val.filename
    file_val.save(dst)

    book = Book(book_name=file_val.filename.split(".")[0],book_url=dst, create_time=datetime.date.today())
    db.session.add(book)
    #需要把信息存到数据库中
    # db.session.commit()
    return jsonify_response(msg="ok")

@bp_book.route('/dele/<int:id>', methods=['POST'])
def del_book(id):
    book = Book.get_or_404(id)
    if book:
        book.logic_delete = "1"
        db.session.commit()
        dst = book.book_url
        try:
            os.remove(dst)
            print("File Deleted Successfully")
        except OSError:
            return jsonify_response(err=500, msg="File Not Found or Permission Denied")
        return jsonify_response()
