from flask import Flask, render_template, request, flash, redirect, Blueprint
app=Flask(__name__)
app.config['SECRET_KEY'] = 'sTriNgqUeniNguEmsAbe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3_g2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK+MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Usuario, Pizza, Pedido
db.init_app(app)
migrate = Migrate(app,db)
from modulos.usuarios import db_usuario
app.register_blueprint(bp_usuario, url_prefix='/usuarios')


