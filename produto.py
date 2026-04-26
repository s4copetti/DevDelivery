class Produto:
    def __init__(self, nome: str, preco: float, disponivel: bool = True, ingredientes: str = ""):
        self.__nome = nome
        self.__preco = preco
        self.__disponivel = disponivel
        self.__ingredientes = ingredientes

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

    @property
    def ingredientes(self):
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, valor: str):
        self.__ingredientes = valor

    def __str__(self):
        status = "✅" if self.__disponivel else "❌ Indisponível"
        linha = f"  {self.__nome:<25} R$ {self.__preco:>6.2f}  {status}"
        if self.__ingredientes:
            linha += f"\n     🧂 {self.__ingredientes}"
        return linha
