from dataclasses import dataclass
fila = []
@dataclass
class Paciente:
    nome: str
    idade: int
    sexo: str
    medico: str

def statusFila():
    return len(fila) > 0

def create():
    print("-------MENU CADASTRO DE FILA HOSPITALAR-------")
    paciente_nome = str(input("Nome do paciente: ")).capitalize()
    while True:
        try:
            paciente_idade = int(input("Idade: "))
            break
        except:
            print("Idade deve ser um número inteiro")
    paciente_sexo = str(input("Sexo: ")).capitalize()
    paciente_medico = str(input("Profissional: ")).capitalize()
    paciente = Paciente(nome=paciente_nome, idade=paciente_idade, sexo=paciente_sexo, medico=paciente_medico)
    fila.append(paciente)
    print(f"Paciente {paciente_nome} cadastrado.")

def read():
    if not statusFila():
        print("Fila vazia!")
        return False
    else:
        print("Fila de espera")
        for i in fila:
            posicao = fila.index(i) + 1
            print("Posição: ", posicao, "Paciente: ", i.nome," | Idade: ", i.idade, " | Sexo: ", i.sexo, " | Profissional: ", i.medico)
        return True

def update():
    while True:
        print("-------MENU ATUALIZAÇÃO DE FILA-------")
        if not read():
            return
        else:
                try:
                    opt = int(input("Qual índice deseja atualizar(Aperte zero para voltar ao menu principal)? "))
                    if opt == 0:
                        return
                    opt -= 1
                    print(fila[opt])
                    try:
                        print("-------------------------")
                        alt = int(input("O que deseja alterar? 1- Nome, 2- Idade, 3- Sexo, 4- Profissional, 5- Voltar ao menu de indice \n Insira a opção: "))
                        if alt == 1:
                            fila[opt].nome = input("Nome do paciente: ").capitalize()
                            break
                        elif alt == 2:
                            while True:
                                try:
                                    fila[opt].idade = int(input("Idade: "))
                                    break
                                except:
                                    print("Idade deve ser um número inteiro")
                        elif alt == 3:
                            fila[opt].sexo = str(input("Sexo: ")).capitalize()
                            break
                        elif alt == 4:
                            fila[opt].medico = str(input("Profissional: ")).capitalize()
                            break
                    except:
                        print("Digite uma opção válida!")
                except:
                    print("Digite uma opção válida!")

def delete():
    while True:
        print("-------MENU EXCLUSÃO-------")
        if not read():
            return
        else:
            try:
                print("Qual paciente deseja excluir(Aperte 0 para voltar)?")
                opt = int(input("Índice: "))
                if opt == 0:
                    return
                opt -= 1
                del fila[opt]
            except:
                print("Digite um índice válido!")


def main():
    while True:
        print("-------MENU SISTEMA DE FILA HOSPITALAR-------")
        try:
            opt = int(input("O que deseja fazer? \n 1- Inserir \n 2-Visualizar lista \n 3-Atualizar \n 4-Excluir \n Insira a opção: "))
            if opt == 1:
                create()
            elif opt == 2:
                read()
            elif opt == 3:
                update()
            elif opt == 4:
                delete()
            else:
                print("Insira uma opção válida!")
        except:
            print("Insira apenas números!")

main()