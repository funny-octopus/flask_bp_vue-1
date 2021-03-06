from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app.main import bp as main_bp
from app.api import bp as api_bp

app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix="/api")

from datetime import datetime
@app.shell_context_processor
def make_shell_context():
    return {'db':db,
            'Domain':models.Domain,
            'UrlTag':models.UrlTag,
            'TextTag':models.TextTag,
            'TitleTag':models.TitleTag,
            'CodePart':models.CodePart,
            'InText':models.InText,
            'InUrl':models.InUrl,
            'InTitle':models.InTitle,
            'Double':models.Double,
            'datetime':datetime,
            }

