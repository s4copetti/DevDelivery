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
    print(f""" DᴇᴠDᴇʟɪᴠᴇʀʏ — {titulo}""")
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
#  Banco de dados em memória (espelhando o HTML)
# ─────────────────────────────────────────────

# Clientes cadastrados: lista de objetos Usuario
cliente_db: list[Usuario] = [
    Usuario("Ana Souza", "Rua das Flores, 42", "ana@email.com", "123456")
]

# Fornecedores cadastrados: lista de dicts simples {email, senha, nome}
fornecedor_db: list[dict] = [
    {"email": "admin@devdelivery.com", "senha": "123456", "nome": "Admin"}
]

# ─────────────────────────────────────────────
#  Dados iniciais de demonstração
# ─────────────────────────────────────────────

def carregar_dados_demo() -> list[Restaurante]:
    restaurantes = []

    r1 = Restaurante("Burguer House", "Fast-food")
    r1.adicionar_produto(Produto("X-Burguer",      22.90, True,  "Pão brioche, hambúrguer bovino 150g, queijo cheddar, alface americana, tomate, maionese artesanal"))
    r1.adicionar_produto(Produto("X-Bacon",        27.50, True,  "Pão brioche, hambúrguer bovino 150g, bacon crocante, queijo cheddar, cebola caramelizada, molho barbecue"))
    r1.adicionar_produto(Produto("X-Salada",       20.00, True,  "Pão integral, hambúrguer bovino 120g, alface, tomate, pepino, cenoura ralada, molho mostarda"))
    r1.adicionar_produto(Produto("Batata Frita P", 10.00, True,  "Batata palito, óleo vegetal, sal refinado"))
    r1.adicionar_produto(Produto("Batata Frita G", 15.00, False, "Batata palito, óleo vegetal, sal refinado"))
    r1.adicionar_produto(Produto("Refrigerante",    8.00, True,  "Coca-Cola, Guaraná Antarctica ou Sprite (lata 350ml)"))
    r1.receber_avaliacao(4.5)
    r1.receber_avaliacao(4.0)
    restaurantes.append(r1)

    r2 = Restaurante("Sushi Nippon", "Japonesa")
    r2.adicionar_produto(Produto("Combo 16 peças", 45.00, True, "Salmão, atum, kani, pepino japonês, cebolinha, cream cheese, arroz japonês, nori"))
    r2.adicionar_produto(Produto("Combo 30 peças", 75.00, True, "Salmão, atum, camarão, kani, pepino, cream cheese, gergelim, arroz japonês, nori"))
    r2.adicionar_produto(Produto("Temaki Salmão",  28.00, True, "Salmão fresco, cream cheese, pepino, cebolinha, gergelim branco, nori, arroz japonês"))
    r2.adicionar_produto(Produto("Missoshiru",     12.00, True, "Pasta de missô, tofu firme, alga wakame, cebolinha, dashi de katsuobushi"))
    r2.adicionar_produto(Produto("Saquê",          18.00, True, "Saquê importado japonês Hakutsuru (200ml)"))
    r2.receber_avaliacao(5.0)
    r2.receber_avaliacao(4.8)
    restaurantes.append(r2)

    r3 = Restaurante("La Bella Italia", "Italiana")
    r3.adicionar_produto(Produto("Nhoque ao Sugo",    38.00, True, "Nhoque de batata artesanal, molho pomodoro fresco, manjericão, parmesão ralado, azeite extravirgem"))
    r3.adicionar_produto(Produto("Lasanha Bolonhesa", 42.00, True, "Massa fresca, ragú bovino com vinho tinto, molho bechamel, parmesão, mussarela fior di latte"))
    r3.adicionar_produto(Produto("Pizza Margherita",  55.00, True, "Massa de fermentação lenta 48h, molho tomate San Marzano, mussarela de búfala, manjericão fresco, azeite"))
    r3.adicionar_produto(Produto("Tiramisu",          22.00, True, "Mascarpone italiano, ovos caipiras, açúcar, café espresso, biscoito champagne, cacau em pó, amaretto"))
    r3.adicionar_produto(Produto("Suco Natural",      10.00, True, "Laranja, limão ou maracujá (300ml — sem açúcar adicionado, sem conservantes)"))
    r3.receber_avaliacao(4.7)
    restaurantes.append(r3)

    return restaurantes

# ─────────────────────────────────────────────
#  Autenticação — Cliente
# ─────────────────────────────────────────────

def cadastrar_cliente() -> Usuario | None:
    limpar()
    cabecalho("Criar conta — Cliente")
    nome = input("  Seu nome: ").strip()
    if not nome:
        print("  ❌ Informe seu nome.")
        pausar()
        return None
    endereco = input("  Endereço de entrega: ").strip()
    if not endereco:
        print("  ❌ Informe seu endereço.")
        pausar()
        return None
    email = input("  E-mail: ").strip().lower()
    if not email or "@" not in email:
        print("  ❌ Informe um e-mail válido.")
        pausar()
        return None
    if any(u.email == email for u in cliente_db):
        print("  ❌ E-mail já cadastrado.")
        pausar()
        return None
    senha = input("  Senha (mín. 6 caracteres): ")
    if len(senha) < 6:
        print("  ❌ A senha deve ter ao menos 6 caracteres.")
        pausar()
        return None
    usuario = Usuario(nome, endereco, email, senha)
    cliente_db.append(usuario)
    print(f"\n  ✅ Conta criada! Bem-vindo(a), {nome}!")
    pausar()
    return usuario

def login_cliente() -> Usuario | None:
    limpar()
    cabecalho("Entrar — Cliente")
    email = input("  E-mail: ").strip().lower()
    if not email or "@" not in email:
        print("  ❌ Informe um e-mail válido.")
        pausar()
        return None
    senha = input("  Senha: ")
    usuario = next((u for u in cliente_db if u.email == email and u.senha == senha), None)
    if not usuario:
        print("  ❌ E-mail ou senha incorretos.")
        pausar()
        return None
    return usuario

# ─────────────────────────────────────────────
#  Autenticação — Fornecedor
# ─────────────────────────────────────────────

def cadastrar_fornecedor() -> dict | None:
    limpar()
    cabecalho("Criar conta — Fornecedor")
    nome = input("  Nome do responsável: ").strip()
    if not nome:
        print("  ❌ Informe o nome.")
        pausar()
        return None
    email = input("  E-mail: ").strip().lower()
    if not email or "@" not in email:
        print("  ❌ Informe um e-mail válido.")
        pausar()
        return None
    if any(f["email"] == email for f in fornecedor_db):
        print("  ❌ E-mail já cadastrado.")
        pausar()
        return None
    senha = input("  Senha (mín. 6 caracteres): ")
    if len(senha) < 6:
        print("  ❌ A senha deve ter ao menos 6 caracteres.")
        pausar()
        return None
    conta = {"email": email, "senha": senha, "nome": nome}
    fornecedor_db.append(conta)
    print(f"\n  ✅ Conta criada! Bem-vindo(a), {nome}!")
    pausar()
    return conta

def login_fornecedor() -> dict | None:
    limpar()
    cabecalho("Entrar — Fornecedor")
    email = input("  E-mail: ").strip().lower()
    if not email or "@" not in email:
        print("  ❌ Informe um e-mail válido.")
        pausar()
        return None
    senha = input("  Senha: ")
    conta = next((f for f in fornecedor_db if f["email"] == email and f["senha"] == senha), None)
    if not conta:
        print("  ❌ E-mail ou senha incorretos.")
        pausar()
        return None
    return conta

# ─────────────────────────────────────────────
#  Fluxo do Cliente
# ─────────────────────────────────────────────

def menu_cliente(usuario: Usuario, restaurantes: list):
    while True:
        limpar()
        cabecalho(f"Olá, {usuario.nome.split()[0]}!")
        print("  [1] Ver restaurantes disponíveis")
        print("  [2] Fazer um pedido")
        print("  [3] Ver meu histórico de pedidos")
        print("  [0] Sair (logout)")
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
        print("  🏪 Nenhum restaurante cadastrado.")
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
        escolha = ler_int(f"  Item (1-{len(disponiveis)}, 0 para finalizar): ", 0, len(disponiveis))
        if escolha == 0:
            if not selecionados:
                print("  ❌ Nenhum item selecionado.")
                continue
            break
        selecionados.append(disponiveis[escolha - 1])
        print(f"  ✅ '{disponiveis[escolha-1].nome}' adicionado!")

    print("\n  💳 Forma de pagamento:")
    pagamentos = ["Cartão de crédito", "Cartão de débito", "Pix", "Dinheiro"]
    for i, p in enumerate(pagamentos, 1):
        print(f"    [{i}] {p}")
    idx_pag = ler_int("  Escolha: ", 1, len(pagamentos))
    pagamento = pagamentos[idx_pag - 1]

    print("\n  🛵 Forma de retirada:")
    retiradas = ["Delivery", "Retirada no local"]
    for i, r in enumerate(retiradas, 1):
        print(f"    [{i}] {r}")
    idx_ret = ler_int("  Escolha: ", 1, len(retiradas))
    retirada = retiradas[idx_ret - 1]

    pedido = usuario.fazer_pedido(restaurante, selecionados, pagamento, retirada)

    limpar()
    cabecalho("✅ Pedido Confirmado!")
    pedido.resumo()
    print("  🍽️  Seu pedido foi enviado ao restaurante!")

    # Avaliação — estrelas 1-5 (igual ao HTML)
    print("\n  Deseja avaliar o restaurante? (s/n): ", end="")
    if input().strip().lower() == "s":
        nota = ler_int("  Nota de 1 a 5 estrelas: ", 1, 5)
        restaurante.receber_avaliacao(float(nota))
        print(f"  ⭐ Avaliação enviada!")

    pausar()

# ─────────────────────────────────────────────
#  Fluxo do Fornecedor
# ─────────────────────────────────────────────

def menu_fornecedor(conta: dict, restaurantes: list):
    while True:
        limpar()
        cabecalho(f"Fornecedor — {conta['nome']}")
        print("  [1] Ver meus restaurantes")
        print("  [2] Cadastrar novo restaurante")
        print("  [3] Gerenciar cardápio")
        print("  [0] Sair (logout)")
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
    """Espelha a tela 'Novo restaurante' do HTML: nome + categoria fixa."""
    limpar()
    cabecalho("Novo Restaurante")
    nome = input("  Nome do restaurante: ").strip()
    if not nome:
        print("  ❌ Informe um nome.")
        pausar()
        return

    categorias = ["Fast-food", "Italiana", "Japonesa", "Brasileira", "Árabe", "Vegana", "Outros"]
    print("\n  Categoria:")
    for i, c in enumerate(categorias, 1):
        print(f"    [{i}] {c}")
    idx_cat = ler_int("  Escolha: ", 1, len(categorias))
    categoria = categorias[idx_cat - 1]

    restaurante = Restaurante(nome, categoria)
    restaurantes.append(restaurante)
    print(f"\n  ✅ Restaurante '{nome}' cadastrado!")
    pausar()

def gerenciar_cardapio(restaurantes: list):
    """Espelha a tela 'Gerenciar' do HTML: lista produtos com toggle + formulário de adição."""
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
        restaurante.mostrar_cardapio_completo()
        print("\n  [1] Adicionar produto")
        print("  [2] Alterar disponibilidade (toggle)")
        print("  [3] Atualizar preço")
        print("  [0] Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            # Formulário igual ao HTML: nome, preço, ingredientes
            limpar()
            cabecalho("Adicionar Produto")
            nome_prod = input("  Nome do produto: ").strip()
            if not nome_prod:
                print("  ❌ Informe um nome.")
                pausar()
                continue
            preco = ler_float(f"  Preço de '{nome_prod}': R$ ")
            ingr = input("  Ingredientes: ").strip()
            restaurante.adicionar_produto(Produto(nome_prod, preco, True, ingr))
            print(f"  ✅ '{nome_prod}' adicionado!")
            pausar()

        elif opcao == "2":
            # Toggle direto pelo número (igual ao botão toggle do HTML)
            todos = restaurante.cardapio
            if not todos:
                print("  Nenhum produto no cardápio.")
                pausar()
                continue
            idx_p = ler_int(f"  Número do produto (1-{len(todos)}): ", 1, len(todos))
            prod = todos[idx_p - 1]
            prod.disponivel = not prod.disponivel
            estado = "disponível" if prod.disponivel else "indisponível"
            print(f"  ✅ '{prod.nome}' marcado como {estado}.")
            pausar()

        elif opcao == "3":
            nome_prod = input("  Nome do produto: ").strip()
            novo_preco = ler_float("  Novo preço: R$ ")
            restaurante.atualizar_preco(nome_prod, novo_preco)
            pausar()

        elif opcao == "0":
            break
        else:
            print("  ❌ Opção inválida.")
            pausar()

# ─────────────────────────────────────────────
#  Tela inicial — Login / Cadastro
# ─────────────────────────────────────────────

def tela_home_cliente(restaurantes: list):
    """Submenu de acesso cliente: login ou cadastro (espelha as abas do HTML)."""
    while True:
        limpar()
        cabecalho("Área do Cliente")
        print("  [1] Entrar na conta")
        print("  [2] Criar conta nova")
        print("  [0] Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            usuario = login_cliente()
            if usuario:
                menu_cliente(usuario, restaurantes)
        elif opcao == "2":
            usuario = cadastrar_cliente()
            if usuario:
                menu_cliente(usuario, restaurantes)
        elif opcao == "0":
            break
        else:
            print("  ❌ Opção inválida.")
            pausar()

def tela_home_fornecedor(restaurantes: list):
    """Submenu de acesso fornecedor: login ou cadastro (espelha as abas do HTML)."""
    while True:
        limpar()
        cabecalho("Área do Fornecedor")
        print("  [1] Entrar como fornecedor")
        print("  [2] Criar conta de fornecedor")
        print("  [0] Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            conta = login_fornecedor()
            if conta:
                menu_fornecedor(conta, restaurantes)
        elif opcao == "2":
            conta = cadastrar_fornecedor()
            if conta:
                menu_fornecedor(conta, restaurantes)
        elif opcao == "0":
            break
        else:
            print("  ❌ Opção inválida.")
            pausar()

def tela_inicial(restaurantes: list):
    while True:
        limpar()
        print("═" * 52)
        print("   🍔  DevDelivery — O sabor que chega até você!")
        print("═" * 52)
        print("  [1] Cliente")
        print("  [2] Fornecedor")
        print("  [0] Sair")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            tela_home_cliente(restaurantes)

        elif opcao == "2":
            tela_home_fornecedor(restaurantes)

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
