from apps.Book import bp_book
from flask import render_template,request
from utils.response import jsonify_response


@bp_book.route('/uu', methods=['GET', 'POST'])
def ss():
    return render_template("index.html")


@bp_book.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template("upload.html")

@bp_book.route('/upload_book', methods=['GET', 'POST'])
def upload_book():
    #只能在request.files里找文件，file是前端formdata中对应文件设置的key值，可以修改，后天也要修改，否则找不到
    #file_val里面的content_length,content_type都为空,我以为没有传成功，后来尝试保存，发现保存成功就好了
    file_val = request.files["file"]
    dst = "e:\\projects\\stacks\\books\\"+file_val.filename
    file_val.save(dst)
    #需要把信息存到数据库中
    return jsonify_response(msg="ok")