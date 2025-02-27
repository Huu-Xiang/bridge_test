import os
from dotenv import load_dotenv
import sys
import os

# Add the 'backend' directory to sys.path
sys.path.append(os.path.dirname(__file__))

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))  # 显式指定.env路径


class Config:
    TUSHARE_TOKEN = os.getenv('TUSHARE_TOKEN', 'default_token')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
