from collections import namedtuple

class Corrida:
    def __init__(self, database):
        self.db = database

    def criar_corrida(self, nome, pais, pista, data):
        query = "CREATE (:Corrida {nome_corrida: $nome_corrida, pais_corrida: $pais_corrida, pista: $pista, data_corrida: $data_corrida})"
        parameters = {"nome_corrida": nome, "pais_corrida": pais, "pista": pista, "data_corrida": data}
        self.db.execute_query(query, parameters)

    def read_corrida(self, nomeCorrida):
        query = "MATCH (c:Corrida {nome_corrida: $nomeCorrida}) RETURN c.nome_corrida AS nome_corrida, c.pais_corrida AS pais_corrida, c.pista AS pista, c.data_corrida AS data_corrida"
        parameters = {"nomeCorrida": nomeCorrida}
        results = self.db.execute_query(query, parameters)
        return [(result["nome_corrida"], result["pais_corrida"], result["pista"], result["data_corrida"]) for result in results]

    def get_posicoes_corrida(self, pista):
        query = """
        MATCH (c:Corrida{pista: $pista})<-[r:PARTICIPOU]-(p:Piloto)
        RETURN p.nome_piloto AS nome_piloto, r.posicao_final AS posicao_final
        """
        parameters = {"pista": pista}
        results = self.db.execute_query(query, parameters)
        return [(result["nome_piloto"], result["posicao_final"]) for result in results]

    def update_corrida(self, nomeCorrida, novo_nome, novo_pais, nova_pista, nova_data):
        query = "MATCH (c:Corrida {nome_corrida: $nomeCorrida}) SET c.nome_corrida = $novo_nome, c.pais_corrida = $novo_pais, c.pista = $nova_pista, c.data_corrida = $nova_data"
        parameters = {"nomeCorrida": nomeCorrida, "novo_nome": novo_nome, "novo_pais": novo_pais, "nova_pista": nova_pista, "nova_data": nova_data}
        self.db.execute_query(query, parameters)

    def remover_corrida(self, nome):
        query = "MATCH (c:Corrida {nome_corrida: $nome}) DETACH DELETE c"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)
#########################
    def return_pilotos(self):
        query = "MATCH (p:Piloto) RETURN p.nome_piloto AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]


    def definir_posicoes(self, nome, piloto_lista):
        for piloto in piloto_lista:
            posicao = int(input(f"Posicao do piloto {piloto}: "))
            query = """
            MATCH (c:Corrida {nome_corrida: $nome_corrida}), (p:Piloto {nome_piloto: $nome_piloto})
            CREATE (p)-[:PARTICIPOU {posicao_final: $posicao_final}]->(c)
            """
            parameters = {"nome_corrida": nome, "nome_piloto": piloto, "posicao_final": posicao}
            self.db.execute_query(query, parameters)
