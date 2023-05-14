from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import cloudinary
import cloudinary.uploader
import cloudinary.api



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = "c2df4070689c55c7b25164b778b8edc5"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home_page'


cloudinary.config(
  cloud_name = "dpmy7xr7m",
  api_key = "916841933657258",
  api_secret = "ltUPBkWFSevYvaBhB7z42BhmleM"
)


from Fakinterest import routes

