# aqui vai ter as coisas do banco de dados.
from Fakinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuarios(id_usuario):
    return Usuarios.query.get(int(id_usuario))
class Usuarios(database.Model, UserMixin):

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False, unique=True)
    fotos = database.relationship('Foto', backref='usuarios', lazy=True)

class Foto(database.Model):
        id = database.Column(database.Integer, primary_key=True)
        url_img = database.Column(database.String, default="default.png")
        data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
        id_usuario = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False)
