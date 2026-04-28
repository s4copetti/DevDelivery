from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pedido import Pedido

# ─────────────────────────────────────────────
#  Classe base
# ─────────────────────────────────────────────

class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    def __str__(self):
        return f"{self.__nome} ({self.__email})"

# ─────────────────────────────────────────────
#  Subclasse Cliente
# ─────────────────────────────────────────────

class Cliente(Usuario):
    def __init__(self, nome: str, email: str, senha: str, endereco: str):
        super().__init__(nome, email, senha)   
        self.__endereco = endereco
        self.__historico: list[Pedido] = []

    @property
    def endereco(self):
        return self.__endereco

    def ver_historico(self):
        if not self.__historico:
            print("  Você ainda não fez nenhum pedido.")
            return
        print(f"\n  📋 Histórico de pedidos de {self.nome}:")
        print("  " + "=" * 50)
        for i, pedido in enumerate(self.__historico, 1):
            print(f"\n  Pedido #{i}")
            pedido.resumo()

    def fazer_pedido(self, restaurante, produtos: list, forma_pagamento: str, forma_retirada: str) -> "Pedido":
        from pedido import Pedido
        pedido = Pedido(self, restaurante, produtos, forma_pagamento, forma_retirada)
        self.__historico.append(pedido)
        return pedido

    def __str__(self):
        return f"{self.nome} — {self.__endereco} ({self.email})"

# ─────────────────────────────────────────────
#  Subclasse Fornecedor
# ─────────────────────────────────────────────

class Fornecedor(Usuario):
    def __init__(self, nome: str, email: str, senha: str):
        super().__init__(nome, email, senha)

    def __str__(self):
        return f"Fornecedor: {self.nome} ({self.email})"

