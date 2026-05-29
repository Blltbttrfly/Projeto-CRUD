def validar_titulo(titulo_livro):
    if len(titulo_livro) <= 3:
        print("Titulo precisa ser maior que 3 caracteres!")
        return False
    else:
        return True
    
def visualizar_livros(livros):
    print("Títulos disponíveis")
    contador = 1
    for livro in livros:
        print(f"{contador}. {livro['titulo']} {livro['autor']}")
        contador += 1

def cadastrar_títulos(livros):
        while True:
            titulo_novo = input("Título: ")
            if titulo_novo == "":
                print("Preencha o campo Título.")
            else: 
                break
        while True:
            autor_novo = input("Autor: ")
            if autor_novo == "":
                print("Preencha o campo Autor.")
            else:
                break
        while True:
            editora_novo = input("Editora: ")
            if editora_novo == "":
                print("Preencha o campo Editora.")
            else:
                break
        
        while True:
            ano_novo = input("Ano de publicação: ")
            if len(ano_novo) != 4:
                print("Digite um ano válido!")
            elif not ano_novo.isdigit:
                print("Digite apenas números!")
            else:
                break

        novo_livro = {
                "titulo": titulo_novo,
                "autor" : autor_novo,
                "ano": ano_novo,
                "editora" : editora_novo
            }
        livros.append(novo_livro)



        


    
    
