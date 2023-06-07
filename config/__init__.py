import os
import yaml
from configparser import ConfigParser


if os.environ.get("FLASK_ENV") == "PRODUCTION":
    config_file_name = "prod_config.yaml"
    uwsgi = "uwsgi.ini"
else:
    config_file_name = "dev_config.yaml"
    uwsgi = "uwsgi.ini"

realpath = os.path.realpath(__file__)
parent_path = os.path.dirname(realpath)

config_path = os.path.join(parent_path, config_file_name)

with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f.read())

# flask配置
get_flask_config = config["flask"]

# 日志配置
get_log_config = config["log"]

#postgre配置
get_postgre_config = config["postgresql"]

#白名单
get_white_list = config["whiteList"]

#是否重新导入数据库
redb = config["redb"]