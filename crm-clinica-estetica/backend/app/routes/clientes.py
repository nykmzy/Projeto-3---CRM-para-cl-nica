from flask import Blueprint, jsonify, request

from app.database.db import db
from app.models.cliente import Cliente

clientes_bp = Blueprint("clientes", __name__)


@clientes_bp.route("/api/clientes", methods=["GET"])
def listar_clientes():

    clientes = Cliente.query.all()

    return jsonify(
        [cliente.to_dict() for cliente in clientes]
    )


@clientes_bp.route("/api/clientes", methods=["POST"])
def criar_cliente():

    dados = request.get_json()

    cliente = Cliente(
        nome=dados["nome"],
        telefone=dados.get("telefone"),
        email=dados.get("email"),
        cpf=dados.get("cpf")
    )

    db.session.add(cliente)
    db.session.commit()

    return jsonify(cliente.to_dict()), 201


@clientes_bp.route("/api/clientes/<int:id>", methods=["GET"])
def buscar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    return jsonify(cliente.to_dict())


@clientes_bp.route("/api/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    dados = request.get_json()

    cliente.nome = dados.get("nome", cliente.nome)
    cliente.telefone = dados.get("telefone", cliente.telefone)
    cliente.email = dados.get("email", cliente.email)
    cliente.cpf = dados.get("cpf", cliente.cpf)

    db.session.commit()

    return jsonify(cliente.to_dict())


@clientes_bp.route("/api/clientes/<int:id>", methods=["DELETE"])
def excluir_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)
    db.session.commit()

    return jsonify({
        "mensagem": "Cliente removido com sucesso"
    })