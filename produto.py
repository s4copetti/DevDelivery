class Produto:
    def __init__(self, nome: str, preco: float, disponivel: bool = True):
        self.__nome = nome
        self.__preco = preco
        self.__disponivel = disponivel

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco < 0:
            print("❌ Preço não pode ser negativo.")
            return
        self.__preco = novo_preco

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, status: bool):
        self.__disponivel = status

    def __str__(self):
        status = "✅" if self.__disponivel else "❌ Indisponível"
        return f"  {self.__nome:<25} R$ {self.__preco:>6.2f}  {status}"
