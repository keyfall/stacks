from apps import create_app
from flask_sqlalchemy import SQLAlchemy

#配置初始化
app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765, debug=True)
