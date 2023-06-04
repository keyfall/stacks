from apps.Book import bp_book
from flask import render_template,request
from utils.response import jsonify_response
from .book import Book
from utils.db import db

@bp_book.route('/uu', methods=['GET', 'POST'])
def ss():
    return render_template("index.html")


@bp_book.route('/upload_book', methods=['GET', 'POST'])
def upload_book():
    if request.method == "GET":
        return render_template("upload.html")
    #只能在request.files里找文件，file是前端formdata中对应文件设置的key值，可以修改，后天也要修改，否则找不到
    #file_val里面的content_length,content_type都为空,我以为没有传成功，后来尝试保存，发现保存成功就好了
    file_val = request.files['file']
    #判断一下上传的名字是否符合规范，是否是一个名字.类型这种格式
    dst = "d:\\projects\\stacks\\books\\"+file_val.filename
    file_val.save(dst)
    book = Book(book_name=file_val.filename.split(".")[0],book_url=dst)
    db.session.add(book)
    #需要把信息存到数据库中
    return jsonify_response(msg="ok")