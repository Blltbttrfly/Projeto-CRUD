import utils

livros = [
    {
        "Título": "Dom Casmurro",
        "Autor": "Machado de Assis",
        "Editora": "Principis",
        "Ano": 1899,
        "Sinopse": "Bentinho relembra sua juventude e o relacionamento com Capitu, levantando dúvidas sobre amor, ciúme e traição."
    },
    {
        "Título": "O Pequeno Príncipe",
        "Autor": "Antoine de Saint-Exupéry",
        "Editora": "Agir",
        "Ano": 1943,
        "Sinopse": "Um piloto perdido no deserto conhece um pequeno príncipe vindo de outro planeta, aprendendo lições sobre amizade e humanidade."
    },
    {
        "Título": "A Hora da Estrela",
        "Autor": "Clarice Lispector",
        "Editora": "Rocco",
        "Ano": 1977,
        "Sinopse": "A história de Macabéa, uma jovem nordestina simples e invisível socialmente, em busca de sentido para sua vida no Rio de Janeiro."
    },
    {
        "Título": "Capitães da Areia",
        "Autor": "Jorge Amado",
        "Editora": "Companhia das Letras",
        "Ano": 1937,
        "Sinopse": "O cotidiano de crianças abandonadas que sobrevivem nas ruas de Salvador, enfrentando pobreza e preconceito."
    },
    {
        "Título": "Anne de Green Gables",
        "Autor": "Lucy Maud Montgomery",
        "Editora": "Pedrazul",
        "Ano": 1908,
        "Sinopse": "Anne Shirley, uma órfã imaginativa e falante, transforma a vida das pessoas ao seu redor em Green Gables."
    },
    {
        "Título": "Extraordinário",
        "Autor": "R. J. Palacio",
        "Editora": "Intrínseca",
        "Ano": 2012,
        "Sinopse": "Auggie Pullman enfrenta os desafios de frequentar a escola pela primeira vez enquanto lida com diferenças físicas."
    },
    {
        "Título": "A Revolução dos Bichos",
        "Autor": "George Orwell",
        "Editora": "Companhia das Letras",
        "Ano": 1945,
        "Sinopse": "Animais de uma fazenda se rebelam contra os humanos, criando uma crítica política sobre poder e corrupção."
    },
    {
        "Título": "Vidas Secas",
        "Autor": "Graciliano Ramos",
        "Editora": "Record",
        "Ano": 1938,
        "Sinopse": "Uma família sertaneja enfrenta a seca, a fome e as dificuldades da sobrevivência no interior nordestino."
    },
    {
        "Título": "O Hobbit",
        "Autor": "J. R. R. Tolkien",
        "Editora": "HarperCollins Brasil",
        "Ano": 1937,
        "Sinopse": "Bilbo Bolseiro embarca em uma aventura inesperada para ajudar anões a recuperarem um tesouro guardado por um dragão."
    },
    {
        "Título": "Persuasão",
        "Autor": "Jane Austen",
        "Editora": "Martin Claret",
        "Ano": 1817,
        "Sinopse": "Anne Elliot reencontra um antigo amor anos depois de ter sido convencida a romper o relacionamento."
    },
    {
        "Título": "Coraline",
        "Autor": "Neil Gaiman",
        "Editora": "Intrínseca",
        "Ano": 2002,
        "Sinopse": "Uma menina curiosa descobre um mundo paralelo aparentemente perfeito, mas cheio de perigos ocultos."
    },
    {
        "Título": "Moby Dick",
        "Autor": "Herman Melville",
        "Editora": "Penguin Companhia",
        "Ano": 1851,
        "Sinopse": "O capitão Ahab lidera uma obsessiva caçada à gigantesca baleia branca Moby Dick."
    },
    {
        "Título": "O Jardim Secreto",
        "Autor": "Frances Hodgson Burnett",
        "Editora": "Penguin Companhia",
        "Ano": 1911,
        "Sinopse": "Uma garota órfã encontra um jardim abandonado que transforma sua vida e a das pessoas ao redor."
    },
    {
        "Título": "Quarto de Despejo",
        "Autor": "Carolina Maria de Jesus",
        "Editora": "Ática",
        "Ano": 1960,
        "Sinopse": "Diário real da autora retratando a pobreza, a fome e o cotidiano em uma favela de São Paulo."
    },
    {
        "Título": "A Bolsa Amarela",
        "Autor": "Lygia Bojunga",
        "Editora": "Casa Lygia Bojunga",
        "Ano": 1976,
        "Sinopse": "Raquel guarda em uma bolsa seus desejos e sentimentos enquanto enfrenta os desafios da infância."
    },
    {
        "Título": "O Velho e o Mar",
        "Autor": "Ernest Hemingway",
        "Editora": "Bertrand Brasil",
        "Ano": 1952,
        "Sinopse": "Um velho pescador cubano trava uma batalha de resistência e coragem contra um enorme peixe."
    },
    {
        "Título": "A Menina que Roubava Livros",
        "Autor": "Markus Zusak",
        "Editora": "Intrínseca",
        "Ano": 2005,
        "Sinopse": "Durante a Segunda Guerra Mundial, Liesel encontra nos livros uma forma de sobreviver aos horrores do período."
    },
    {
        "Título": "Memórias Póstumas de Brás Cubas",
        "Autor": "Machado de Assis",
        "Editora": "Principis",
        "Ano": 1881,
        "Sinopse": "Narrado por um defunto autor, o romance mistura ironia e crítica social ao contar a vida de Brás Cubas."
    },
    {
        "Título": "O Meu Pé de Laranja Lima",
        "Autor": "José Mauro de Vasconcelos",
        "Editora": "Melhoramentos",
        "Ano": 1968,
        "Sinopse": "Zezé, um menino sensível e criativo, enfrenta dificuldades familiares enquanto cria amizade com um pé de laranja lima."
    },
    {
        "Título": "A Máquina do Tempo",
        "Autor": "H. G. Wells",
        "Editora": "Zahar",
        "Ano": 1895,
        "Sinopse": "Um cientista viaja ao futuro e descobre transformações surpreendentes na humanidade."
    }
]

    
while True:

    print("""
          
    📚 ------ BEM-VINDO À BIBLIOTECA SLOP ------ 📚
    
                1. Ver Livros Disponíveis
                2. Cadastrar Livros
                3. Modificar Livros
                4. Remover Livros
                5. Ler Sinopses
                6. Buscar por Autor
            
                0. Sair
          
""")
    
    op = input("Digite a opção desejada: ")
    
    if op == "1":
        utils.visualizar_titulos(livros)
        
    elif op == "2":
        utils.cadastrar_livro(livros)

    elif op == "3":
        utils.modificar_livro(livros)

    elif op == "4":
        utils.remover_livro(livros)
    
    elif op == "5":
        utils.ler_sinopses(livros)
    
    elif op == "6":
        utils.buscar_autor(livros)
    
    elif op == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Digite uma opção válida!")
        

    input("DIGITE ENTER PARA CONTINUAR")