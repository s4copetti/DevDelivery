from produto import Produto
from datetime import datetime

class Pedido:
    _contador = 1

    def __init__(self, usuario, restaurante, produtos: list[Produto], forma_pagamento: str, forma_retirada: str):
        self.__id = Pedido._contador
        Pedido._contador += 1
        self.__usuario = usuario
        self.__restaurante = restaurante
        self.__produtos = produtos
        self.__forma_pagamento = forma_pagamento
        self.__forma_retirada = forma_retirada
        self.__total = sum(p.preco for p in produtos)
        self.__data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.__status = "Aguardando confirmação"

    @property
    def id(self):
        return self.__id

    @property
    def total(self):
        return self.__total

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status: str):
        self.__status = novo_status

    def resumo(self):
        print(f"  {'─' * 48}")
        print(f"  🧾 Pedido #{self.__id} — {self.__data}")
        print(f"  🏠 Restaurante : {self.__restaurante.nome}")
        print(f"  👤 Cliente     : {self.__usuario.nome}")
        print(f"  📍 Endereço    : {self.__usuario.endereco}")
        print(f"  {'─' * 48}")
        print(f"  Itens do pedido:")
        for produto in self.__produtos:
            print(f"    • {produto.nome:<23} R$ {produto.preco:>6.2f}")
        print(f"  {'─' * 48}")
        print(f"  💰 Total       : R$ {self.__total:.2f}")
        print(f"  💳 Pagamento   : {self.__forma_pagamento}")
        print(f"  🛵 Retirada    : {self.__forma_retirada}")
        print(f"  📌 Status      : {self.__status}")
        print(f"  {'─' * 48}")
