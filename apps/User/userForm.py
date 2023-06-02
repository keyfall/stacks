from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class userForm(FlaskForm):
    uname = StringField(label="用户名",validators=[DataRequired()],
                        render_kw={'class':'span6 typeahead'}
                                  )
    upassword = StringField(label="用户密码",validators=[DataRequired()],
                        render_kw={'class':'input-file uniform_on',
                                   'id':"fileimg",
                                   'onchange':"change(this)"})