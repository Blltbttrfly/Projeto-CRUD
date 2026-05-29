import utils


    # titulo_livro = input("Digite o nome do livro a ser cadastrado: ")
    # if utils.validar_titulo(titulo_livro):
    #     break
livros =  [
    {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "editora": "Livraria Garnier"
    },
    {
        "titulo": "Memórias Póstumas de Brás Cubas",
        "autor": "Machado de Assis",
        "ano": 1881,
        "editora": "Tipografia Nacional"
    },
    {
        "titulo": "O Cortiço",
        "autor": "Aluísio Azevedo",
        "ano": 1890,
        "editora": "B. L. Garnier"
    },
    {
        "titulo": "Iracema",
        "autor": "José de Alencar",
        "ano": 1865,
        "editora": "Tipografia Viana & Filhos"
    },
    {
        "titulo": "Grande Sertão: Veredas",
        "autor": "João Guimarães Rosa",
        "ano": 1956,
        "editora": "José Olympio"
    },
    {
        "titulo": "Vidas Secas",
        "autor": "Graciliano Ramos",
        "ano": 1938,
        "editora": "José Olympio"
    },
    {
        "titulo": "Capitães da Areia",
        "autor": "Jorge Amado",
        "ano": 1937,
        "editora": "Companhia Editora Nacional"
    },
    {
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1943,
        "editora": "Reynal & Hitchcock"
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949,
        "editora": "Secker & Warburg"
    },
    {
        "titulo": "A Revolução dos Bichos",
        "autor": "George Orwell",
        "ano": 1945,
        "editora": "Secker & Warburg"
    },
    {
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling",
        "ano": 1997,
        "editora": "Bloomsbury"
    },
    {
        "titulo": "Harry Potter e a Câmara Secreta",
        "autor": "J.K. Rowling",
        "ano": 1998,
        "editora": "Bloomsbury"
    },
    {
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "autor": "J.R.R. Tolkien",
        "ano": 1954,
        "editora": "Allen & Unwin"
    },
    {
        "titulo": "O Hobbit",
        "autor": "J.R.R. Tolkien",
        "ano": 1937,
        "editora": "Allen & Unwin"
    },
    {
        "titulo": "Orgulho e Preconceito",
        "autor": "Jane Austen",
        "ano": 1813,
        "editora": "T. Egerton"
    },
    {
        "titulo": "Crime e Castigo",
        "autor": "Fiódor Dostoiévski",
        "ano": 1866,
        "editora": "The Russian Messenger"
    },
    {
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "ano": 1605,
        "editora": "Francisco de Robles"
    },
    {
        "titulo": "Cem Anos de Solidão",
        "autor": "Gabriel García Márquez",
        "ano": 1967,
        "editora": "Editorial Sudamericana"
    },
    {
        "titulo": "O Alquimista",
        "autor": "Paulo Coelho",
        "ano": 1988,
        "editora": "Rocco"
    },
    {
        "titulo": "A Menina que Roubava Livros",
        "autor": "Markus Zusak",
        "ano": 2005,
        "editora": "Picador"
    }
]
    
while True:

    print("""
------BEM VINDO À BIBLIOTECA SLOP----
          
    1. ver livros disponíveis
    2. cadastrar livros
    3. modificar prateleira
    4. remover títulos
    0. sair
          
""")
    
    op = input("Digite a opção desejada: ")
    if op == "1":
        utils.visualizar_livros(livros)
        

    if op == "2":
        utils.cadastrar_títulos(livros)
        

    input("DIGITE ENTER PARA CONTINUAR: ")