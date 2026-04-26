from produto import Produto


class Restaurante:
    def __init__(self, nome: str, categoria: str):
        self.__nome = nome
        self.__categoria = categoria
        self.__cardapio: list[Produto] = []
        self.__avaliacoes: list[float] = []

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def cardapio(self):
        return self.__cardapio

    def adicionar_produto(self, produto: Produto):
        self.__cardapio.append(produto)

    def mostrar_cardapio(self):
        disponiveis = [p for p in self.__cardapio if p.disponivel]
        if not disponiveis:
            print("  Nenhum produto disponível no momento.")
            return
        print(f"\n  {'PRODUTO':<25} {'PREÇO':>10}")
        print("  " + "-" * 40)
        for i, produto in enumerate(disponiveis, 1):
            print(f"  [{i}] {produto}")

    def mostrar_cardapio_completo(self):
        """Exibe todos os produtos (disponíveis e indisponíveis) — usado no gerenciamento."""
        if not self.__cardapio:
            print("  Nenhum produto cadastrado.")
            return
        print(f"\n  {'PRODUTO':<25} {'PREÇO':>10}  STATUS")
        print("  " + "-" * 50)
        for i, produto in enumerate(self.__cardapio, 1):
            print(f"  [{i}] {produto}")

    def get_produtos_disponiveis(self):
        return [p for p in self.__cardapio if p.disponivel]

    def receber_avaliacao(self, nota: float):
        if 0 <= nota <= 5:
            self.__avaliacoes.append(nota)

    def media_avaliacoes(self):
        if not self.__avaliacoes:
            return None
        return sum(self.__avaliacoes) / len(self.__avaliacoes)

    def atualizar_preco(self, nome_produto: str, novo_preco: float):
        for produto in self.__cardapio:
            if produto.nome.lower() == nome_produto.lower():
                produto.preco = novo_preco
                print(f"✅ Preço de '{produto.nome}' atualizado para R$ {novo_preco:.2f}")
                return
        print(f"❌ Produto '{nome_produto}' não encontrado.")

    def atualizar_disponibilidade(self, nome_produto: str, status: bool):
        for produto in self.__cardapio:
            if produto.nome.lower() == nome_produto.lower():
                produto.disponivel = status
                estado = "disponível" if status else "indisponível"
                print(f"✅ '{produto.nome}' marcado como {estado}.")
                return
        print(f"❌ Produto '{nome_produto}' não encontrado.")

    def __str__(self):
        media = self.media_avaliacoes()
        estrelas = f"⭐ {media:.1f}" if media else "Sem avaliações"
        return f"{self.__nome} [{self.__categoria}] — {estrelas}"
