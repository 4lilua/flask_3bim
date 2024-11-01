from flask import Blueprint, render_template, request, redirect, flash
from models import Pedido
from database import db

bp_pedidos = Blueprint('pedidos', __name__, template_folder="templates")

@bp_pedido.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedido.html', pedidos = dados)

@bp_pedido.route('/add')
def add():
    return render_template('pedido_add.html')

@bp_pedido.route('/save', methods=['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preco = request.form.get('preco')
    if sabor and ingredientes and preco:
        db_pizza = Pizza(sabor, ingredientes, preco)
        db.session.add(db_pizza)
        db.session.commit()
        flash('Pizza salva com sucesso!!!')
        return redirect ('/pizzas')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/pizzas/add')
