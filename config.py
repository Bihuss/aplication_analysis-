import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or "n39$&4bXq@#MznQ!q3&b>PfT_1%"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'flask_app.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
