alunos = []
def menu():
    print("Menu: \n")
    print("1 - Cadastrar\n")
    print("2 - Remover\n")
    print("3 - Listar\n")
    print("4 - Atualizar\n")
    print("5 - Sair")
    selecao = int(input("Selecione um valor: \n"))
    if selecao == 1:
        cadastro_alunos(alunos)
    elif selecao == 2:
        remove_alunos(alunos)
    elif selecao == 3:
        listagem(alunos)
    elif selecao == 4:
        atualiza_aluno(alunos)
    elif selecao == 5:
        print("Até logo!")
    else:
        print("Operação inválida, tente novamente!")


def cadastro_alunos(alunos):
    dados_alunos = {
        "Id": input("Digite o ID: \n"),
        "Nome": input("Digite o nome: \n"),
        "idade": input("Digite a idade: \n"),
        "cpf": input("Digite o cpf: \n")
    }
    alunos.append(dados_alunos)
    print("Aluno cadastrado com sucesso!")
    sim_nao()


def remove_alunos(alunos):
    item = input("Digite o ID do aluno que deseja remover: \n")
    verifica = False
    for i in alunos:
        if i.get("Id") == item:
            alunos.remove(i)
            verifica = True
            print("Aluno removido com sucesso")
    if not verifica:
        print("Valor não encontrado")
    sim_nao()


def listagem(alunos):
    for i in alunos:
        print(i)
    sim_nao()


def atualiza_aluno(alunos):
    item = input("Digite o ID do aluno que deseja atualizar: \n")
    verifica = False
    for i in alunos:
        if i.get("Id") == item:
            alunos.remove(i)
            atualiza = {
                "Id": item,
                "Nome": input("Digite o nome: \n"),
                "idade": input("Digite a idade: \n"),
                "cpf": input("Digite o cpf: \n")
            }
            alunos.append(atualiza)
            print("Aluno atualizado com sucesso!")
            verifica = True
    if not verifica:
        print("Valor não encontrado")
    sim_nao()


def sim_nao():
    escolha = int(input("Digite 1 para continuar ou 0 para sair: \n"))
    if escolha == 1:
        menu()
    else:
        print("Encerrando a execução!")


if __name__ == '__main__':
    print(menu())
