from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pedido import Pedido


class Usuario:
    def __init__(self, nome: str, endereco: str, email: str = "", senha: str = ""):
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__senha = senha
        self.__historico: list[Pedido] = []

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    def adicionar_pedido_ao_historico(self, pedido: "Pedido"):
        self.__historico.append(pedido)

    def ver_historico(self):
        if not self.__historico:
            print("  Você ainda não fez nenhum pedido.")
            return
        print(f"\n  📋 Histórico de pedidos de {self.__nome}:")
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
        return f"{self.__nome} — {self.__endereco} ({self.__email})"
