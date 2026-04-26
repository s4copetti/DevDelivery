import os
import sys
from usuario import Usuario
from restaurante import Restaurante
from produto import Produto

# ─────────────────────────────────────────────
#  Utilitários de interface
# ─────────────────────────────────────────────

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n  Pressione ENTER para continuar...")

def cabecalho(titulo: str):
    print("\n" + "═" * 52)
    print(f"  🍔 DevDelivery — {titulo}")
    print("═" * 52)

def ler_int(prompt: str, minimo: int = 1, maximo: int = 9999) -> int:
    while True:
        try:
            valor = int(input(prompt))
            if minimo <= valor <= maximo:
                return valor
            print(f"  ❌ Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("  ❌ Entrada inválida. Digite um número.")

def ler_float(prompt: str) -> float:
    while True:
        try:
            valor = float(input(prompt))
            if valor >= 0:
                return valor
            print("  ❌ O valor não pode ser negativo.")
        except ValueError:
            print("  ❌ Entrada inválida. Digite um número.")

# ─────────────────────────────────────────────
#  Dados iniciais de demonstração
# ─────────────────────────────────────────────

def carregar_dados_demo():
    restaurantes = []

    r1 = Restaurante("Burguer House", "Fast-food")
    r1.adicionar_produto(Produto("X-Burguer", 22.90))
    r1.adicionar_produto(Produto("X-Bacon", 27.50))
    r1.adicionar_produto(Produto("X-Salada", 20.00))
    r1.adicionar_produto(Produto("Batata Frita P", 10.00))
    r1.adicionar_produto(Produto("Batata Frita G", 15.00))
    r1.adicionar_produto(Produto("Refrigerante", 8.00))
    r1.receber_avaliacao(4.5)
    r1.receber_avaliacao(4.0)
    restaurantes.append(r1)

    r2 = Restaurante("Sushi Nippon", "Comida Japonesa")
    r2.adicionar_produto(Produto("Combo 16 peças", 45.00))
    r2.adicionar_produto(Produto("Combo 30 peças", 75.00))
    r2.adicionar_produto(Produto("Temaki Salmão", 28.00))
    r2.adicionar_produto(Produto("Missoshiru", 12.00))
    r2.adicionar_produto(Produto("Saquê", 18.00))
    r2.receber_avaliacao(5.0)
    r2.receber_avaliacao(4.8)
    restaurantes.append(r2)

    r3 = Restaurante("La Bella Italia", "Comida Italiana")
    r3.adicionar_produto(Produto("Nhoque ao Sugo", 38.00))
    r3.adicionar_produto(Produto("Lasanha Bolonhesa", 42.00))
    r3.adicionar_produto(Produto("Pizza Margherita", 55.00))
    r3.adicionar_produto(Produto("Tiramisu", 22.00))
    r3.adicionar_produto(Produto("Suco Natural", 10.00))
    r3.receber_avaliacao(4.7)
    restaurantes.append(r3)

    return restaurantes

# ─────────────────────────────────────────────
#  Fluxo do Cliente
# ─────────────────────────────────────────────

def menu_cliente(usuario: Usuario, restaurantes: list):
    while True:
        limpar()
        cabecalho(f"Olá, {usuario.nome}!")
        print("  [1] Ver restaurantes disponíveis")
        print("  [2] Fazer um pedido")
        print("  [3] Ver meu histórico de pedidos")
        print("  [0] Sair")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            listar_restaurantes(restaurantes)
            pausar()

        elif opcao == "2":
            fazer_pedido_cliente(usuario, restaurantes)

        elif opcao == "3":
            limpar()
            cabecalho("Meu Histórico")
            usuario.ver_historico()
            pausar()

        elif opcao == "0":
            break
        else:
            print("  ❌ Opção inválida.")
            pausar()

def listar_restaurantes(restaurantes: list):
    limpar()
    cabecalho("Restaurantes Disponíveis")
    if not restaurantes:
        print("  Nenhum restaurante cadastrado.")
        return
    for i, r in enumerate(restaurantes, 1):
        print(f"  [{i}] {r}")

def fazer_pedido_cliente(usuario: Usuario, restaurantes: list):
    limpar()
    cabecalho("Fazer Pedido")
    listar_restaurantes(restaurantes)

    if not restaurantes:
        pausar()
        return

    idx = ler_int(f"\n  Escolha o restaurante (1-{len(restaurantes)}): ", 1, len(restaurantes))
    restaurante = restaurantes[idx - 1]

    limpar()
    cabecalho(f"Cardápio — {restaurante.nome}")
    restaurante.mostrar_cardapio()

    disponiveis = restaurante.get_produtos_disponiveis()
    if not disponiveis:
        pausar()
        return

    print("\n  Adicione itens ao pedido (digite 0 para finalizar):")
    selecionados = []
    while True:
        escolha = ler_int(f"  Item [{'/'.join(str(i) for i in range(1, len(disponiveis)+1))}] (0 para finalizar): ", 0, len(disponiveis))
        if escolha == 0:
            if not selecionados:
                print("  ❌ Nenhum item selecionado.")
                continue
            break
        selecionados.append(disponiveis[escolha - 1])
        print(f"  ✅ '{disponiveis[escolha-1].nome}' adicionado!")

    print("\n  💳 Forma de pagamento:")
    pagamentos = ["Cartão de Crédito", "Cartão de Débito", "Pix", "Dinheiro"]
    for i, p in enumerate(pagamentos, 1):
        print(f"    [{i}] {p}")
    idx_pag = ler_int("  Escolha: ", 1, len(pagamentos))
    pagamento = pagamentos[idx_pag - 1]

    print("\n  🛵 Forma de retirada:")
    retiradas = ["Delivery (entrega em casa)", "Retirada no local"]
    for i, r in enumerate(retiradas, 1):
        print(f"    [{i}] {r}")
    idx_ret = ler_int("  Escolha: ", 1, len(retiradas))
    retirada = retiradas[idx_ret - 1]

    pedido = usuario.fazer_pedido(restaurante, selecionados, pagamento, retirada)

    limpar()
    cabecalho("✅ Pedido Confirmado!")
    pedido.resumo()
    print("  🍽️  Seu pedido foi enviado ao restaurante!")

    # Avaliação opcional
    print("\n  Deseja avaliar o restaurante? (s/n): ", end="")
    if input().strip().lower() == "s":
        nota = ler_float("  Nota (0 a 5): ")
        if 0 <= nota <= 5:
            restaurante.receber_avaliacao(nota)
            print(f"  ⭐ Obrigado pela avaliação!")
        else:
            print("  ❌ Nota fora do intervalo.")

    pausar()

# ─────────────────────────────────────────────
#  Fluxo do Fornecedor
# ─────────────────────────────────────────────

def menu_fornecedor(restaurantes: list):
    while True:
        limpar()
        cabecalho("Painel do Fornecedor")
        print("  [1] Listar restaurantes")
        print("  [2] Cadastrar novo restaurante")
        print("  [3] Gerenciar cardápio")
        print("  [0] Sair")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            listar_restaurantes(restaurantes)
            pausar()

        elif opcao == "2":
            cadastrar_restaurante(restaurantes)

        elif opcao == "3":
            gerenciar_cardapio(restaurantes)

        elif opcao == "0":
            break
        else:
            print("  ❌ Opção inválida.")
            pausar()

def cadastrar_restaurante(restaurantes: list):
    limpar()
    cabecalho("Cadastrar Restaurante")
    nome = input("  Nome do restaurante: ").strip()
    if not nome:
        print("  ❌ Nome não pode ser vazio.")
        pausar()
        return

    print("  Categorias sugeridas: Fast-food, Italiana, Japonesa, Brasileira, Árabe, Vegana")
    categoria = input("  Categoria: ").strip()
    if not categoria:
        categoria = "Outros"

    restaurante = Restaurante(nome, categoria)

    print("\n  Deseja adicionar produtos agora? (s/n): ", end="")
    if input().strip().lower() == "s":
        while True:
            nome_prod = input("  Nome do produto (ou ENTER para encerrar): ").strip()
            if not nome_prod:
                break
            preco = ler_float(f"  Preço de '{nome_prod}': R$ ")
            restaurante.adicionar_produto(Produto(nome_prod, preco))
            print(f"  ✅ '{nome_prod}' adicionado!")

    restaurantes.append(restaurante)
    print(f"\n  ✅ Restaurante '{nome}' cadastrado com sucesso!")
    pausar()

def gerenciar_cardapio(restaurantes: list):
    limpar()
    cabecalho("Gerenciar Cardápio")

    if not restaurantes:
        print("  Nenhum restaurante cadastrado.")
        pausar()
        return

    listar_restaurantes(restaurantes)
    idx = ler_int(f"\n  Escolha o restaurante (1-{len(restaurantes)}): ", 1, len(restaurantes))
    restaurante = restaurantes[idx - 1]

    while True:
        limpar()
        cabecalho(f"Gerenciar — {restaurante.nome}")
        restaurante.mostrar_cardapio()
        print("\n  [1] Adicionar produto")
        print("  [2] Atualizar preço")
        print("  [3] Alterar disponibilidade")
        print("  [0] Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            nome_prod = input("  Nome do produto: ").strip()
            if nome_prod:
                preco = ler_float(f"  Preço de '{nome_prod}': R$ ")
                restaurante.adicionar_produto(Produto(nome_prod, preco))
                print(f"  ✅ '{nome_prod}' adicionado!")
            pausar()

        elif opcao == "2":
            nome_prod = input("  Nome do produto: ").strip()
            novo_preco = ler_float("  Novo preço: R$ ")
            restaurante.atualizar_preco(nome_prod, novo_preco)
            pausar()

        elif opcao == "3":
            nome_prod = input("  Nome do produto: ").strip()
            print("  [1] Disponível  [2] Indisponível")
            status_op = ler_int("  Escolha: ", 1, 2)
            restaurante.atualizar_disponibilidade(nome_prod, status_op == 1)
            pausar()

        elif opcao == "0":
            break
        else:
            print("  ❌ Opção inválida.")
            pausar()

# ─────────────────────────────────────────────
#  Tela inicial / Login
# ─────────────────────────────────────────────

def login_cliente() -> Usuario:
    limpar()
    cabecalho("Login — Cliente")
    nome = input("  Seu nome: ").strip() or "Cliente"
    endereco = input("  Seu endereço: ").strip() or "Não informado"
    return Usuario(nome, endereco)

def tela_inicial(restaurantes: list):
    while True:
        limpar()
        print("═" * 52)
        print("   🍔  DevDelivery — O sistema que mata sua fome!")
        print("═" * 52)
        print("  [1] Entrar como Cliente")
        print("  [2] Entrar como Fornecedor")
        print("  [0] Sair")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            usuario = login_cliente()
            menu_cliente(usuario, restaurantes)

        elif opcao == "2":
            limpar()
            cabecalho("Painel do Fornecedor")
            menu_fornecedor(restaurantes)

        elif opcao == "0":
            limpar()
            print("\n  👋 Obrigado por usar o DevDelivery! Até logo!\n")
            sys.exit(0)
        else:
            print("  ❌ Opção inválida.")
            pausar()

# ─────────────────────────────────────────────
#  Ponto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    restaurantes = carregar_dados_demo()
    tela_inicial(restaurantes)
