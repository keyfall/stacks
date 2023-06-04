from apps import create_app
from utils.db import db

#配置初始化
app = create_app()
# db.drop_all(app=app)
# db.create_all(app=app)

if __name__ == '__main__':
    #这里debug为true时会进行2次运行create_all
    # 这里执行2次，可能是因为create_all时进行了类加载器，flask探测到代码发生改变，触发自动重载
    app.run(host='0.0.0.0', port=8765, debug=True)
