
import sys
import os

# Add the 'backend' directory to sys.path
sys.path.append(os.path.dirname(__file__))

from flask import Flask
from config import Config


app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # 加载配置类
    
    from routes import api
    app.register_blueprint(api)
    
    # 验证配置加载
    print(f"Loaded TUSHARE_TOKEN: {app.config['TUSHARE_TOKEN'][:3]}***") 
    
    return app

app = create_app()
