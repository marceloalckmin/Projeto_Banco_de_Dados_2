from Corrida import Corrida
from OrgaoRegulador import OrgaoRegulador
from Equipe import Equipe
class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class AutomobilismoCLI(SimpleCLI):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.Corrida = Corrida(db)
        self.Equipe = Equipe(db)
        self.OrgaoRegulador = OrgaoRegulador(db)
        self.add_command("criar_corrida", self.interface_criacao_corrida)
        self.add_command("ver_corrida", self.read_corrida)
        self.add_command("atualizar_corrida", self.update_corrida)
        self.add_command("deletar_corrida", self.delete_corrida)
        self.add_command("criar_equipe", self.create_equipe)
        self.add_command("ver_equipe", self.read_equipe)
        self.add_command("atualizar_equipe", self.update_equipe)
        self.add_command("deletar_equipe", self.delete_equipe)
        self.add_command("criar_orgao", self.create_orgao)
        self.add_command("read_orgao", self.read_orgao)
        self.add_command("update_orgao", self.update_orgao)
        self.add_command("delete_orgao", self.delete_orgao)

    def interface_criacao_corrida(self):
        nome_corrida = input("Nome da corrida: ")
        pais_corrida = input("Pais da corrda: ")
        nome_pista = input("Nome da pista: ")
        data_corrida = input("Data corrida (DD-MM-AA): ")
        self.Corrida.criar_corrida(nome_corrida, pais_corrida, nome_pista, data_corrida)
        nome_pilotos = self.Corrida.return_pilotos()
        self.Corrida.definir_posicoes(nome_corrida, nome_pilotos)

    def read_corrida(self):
        nome_corrida = input("Entre o nome da corrida que você deseja ver: ")
        corrida = self.Corrida.read_corrida(nome_corrida)
        #print(corrida)
        print(f"Nome: {corrida[0][0]}, Pais: {corrida[0][1]}, Pista: {corrida[0][2]}, Data: {corrida[0][3]}")
        print("Placar da corrida: ")
        posicoes_ordenadas = sorted(self.Corrida.get_posicoes_corrida(corrida[0][2]), key=lambda x: x[1])
        print("--------------------------------------------")
        for piloto_nome, posicao_final in posicoes_ordenadas:
            print(f"Piloto: {piloto_nome} - Posição Final: {posicao_final}")
        print("--------------------------------------------")


    def update_corrida(self):
        nome_corrida = input("Entre o nome da corrida que você deseja atualizar: ")
        novo_nome = input("Entre o nome da corrida que você deseja que fique: ")
        novo_pais = input("Entre o pais da corrida: ")
        nova_pista = input("Entre o nome da pista: ")
        nova_data =input("Entre a data da corrida(DD-MM-AA): ")
        self.Corrida.update_corrida(nome_corrida, novo_nome, novo_pais, nova_pista, nova_data)

    def delete_corrida(self):
        nome_corrida = input("Entre o nome da corrida que você deseja deletar: ")
        self.Corrida.remover_corrida(nome_corrida)

    #cara não entendi só como funcionaria isso porque a classe Equipe tem um construtor e talvez isso mude alguma coisa ou sei lá, porque n ta tendo um objeto sendo criado aqui
    def create_equipe(self):
        nome_equipe = input("Entre com o nome da equipe: ")
        pais = input("Entre com o país: ")
        data = input("Entre com a data de criação da equipe(DD-MM-AA): ")
        self.Equipe.criar_equipe(nome = nome_equipe, pais = pais, data = data)
        for i in range(2):
            nome_piloto = input(f"Nome do piloto {i+1}: ")
            pais_piloto = input("Pais de nascimento: ")
            data_nascimento = input("Data de nascimento: ")
            self.Equipe.adicionar_piloto_db(nome_piloto, pais_piloto, data_nascimento)
            self.Equipe.ligar_piloto_equipe(nome_piloto, nome_equipe)
    
    def read_equipe(self):
        nome_equipe = input("Entre com o nome da equipe a ser procurada: ")
        eq = self.Equipe.read_equipe(nomeEquipe = nome_equipe)
        pilotos = self.Equipe.ver_pilotos(nome_equipe)
        #print(eq)
        print("Nome da Equipe: ", eq[0][0])
        print("Nacionalidade da Equipe: ", eq[0][1])
        print(f"Pilotos:  {pilotos[0]} e {pilotos[1]}")
        #print(pilotos)


    def update_equipe(self):
        nome_equipe = input("Entre com o nome da equipe a ser atualizada: ")
        novo_nome = input("Entre o nome da equipe que você deseja que fique: ")
        novo_pais = input("Entre o pais da equipe: ")
        nova_data =input("Entre a data de criação da equipe(DD-MM-AA): ")
        self.Equipe.update_equipe(old_nome= nome_equipe, new_nome= novo_nome, new_pais= novo_pais, new_data= nova_data)

    def delete_equipe(self):
        nome_equipe = input("Entre com o nome da equipe a ser deletada: ")
        self.Equipe.delete_equipe(nomeEquipe= nome_equipe)

    def create_orgao(self):
        nome_orgao = input("Entre com o nome do orgão: ")
        data = input("Entre com a data de criação do orgão(DD-MM-AA): ")
        self.OrgaoRegulador.criar_orgao(nome= nome_orgao, data_criacao= data)

    def read_orgao(self):
        nome_orgao = input("Entre com o nome do orgão: ")
        orgao = self.OrgaoRegulador.get_info_orgao(nome_orgao= nome_orgao)
        #print(orgao)
        print(f"Nome: {orgao[0][0]}, Data de criação: {orgao[0][1]}")

    def update_orgao(self):
        nome_orgao = input("Entre com o nome do orgão a ser atualizado: ")
        novo_nome = input("Entre com o nome do orgão: ")
        nova_data = input("Entre com a data de criação do orgão(DD-MM-AA): ")
        self.OrgaoRegulador.update_orgao(nome_antigo= nome_orgao, novo_nome= novo_nome, nova_data= nova_data)

    def delete_orgao(self):
        nome_orgao = input("Entre com o nome do orgão a ser deletado: ")
        self.OrgaoRegulador.deletar_orgao(nome_orgao= nome_orgao)


    def run(self):
        print("Seja bem vindo!")
        print("Comandos referentes às corridas: criar_corrida, ver_corrida, atualizar_corrida, deletar_corrida")
        print("Comandos referentes as equipes: criar_equipe, ver_equipe, atualizar_equipe, deletar_equipe")
        print("Comandos referentes aos orgãos reguladores: criar_orgao, read_orgao, update_orgao, delete_orgao")
        super().run()