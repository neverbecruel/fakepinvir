# aqui vai ficar as rotas(links do site).
import cloudinary.uploader
from flask import render_template, url_for, redirect
from Fakinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from Fakinterest.forms import FormLogin, FormCriarConta, FormFotos
from Fakinterest.models import Usuarios, Foto
from werkzeug.utils import secure_filename
import os


@app.route("/", methods=['GET', 'POST'])
def home_page():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuarios.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for('feed'))
    return render_template(r'homepage.html', form=formlogin )

@app.route("/criar-conta", methods=['GET', 'POST'])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(str(form_criarconta.senha.data))
        usuario = Usuarios(username=form_criarconta.username.data, senha=senha,
                           email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('feed'))
    return render_template('criarconta.html', form=form_criarconta)


@app.route('/perfil/<id_usuario>', methods=['POST', "GET"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        formFoto = FormFotos()
        if formFoto.validate_on_submit():
            foto = formFoto.foto.data
            #nome_seguro = secure_filename(foto.filename)
            '''path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    app.config["UPLOAD_FOLDER"], nome_seguro)'''
            upload = cloudinary.uploader.upload(foto, format='jpg')
            #foto.save(path)
            foto = Foto( id_usuario=current_user.id, url_img=upload['url'] )  #imagem=nome_seguro,
            database.session.add(foto)
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, form=formFoto )
    else:
        usuario = Usuarios.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template('feed.html', fotos=fotos)

