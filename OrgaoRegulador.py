from collections import namedtuple
class OrgaoRegulador:
    def __init__(self, database):
        self.db = database

    def criar_orgao(self, nome, data_criacao):
        query = "CREATE (o:OrgaoRegulador {nome: $nome, data_criacao: $data_criacao})"
        parameters = {"nome": nome, "data_criacao": data_criacao}
        self.db.execute_query(query, parameters)

    def get_info_orgao(self, nome_orgao):
        query = "MATCH (o:OrgaoRegulador{nome: $nome_orgao}) RETURN o.nome AS nome, o.data_criacao AS data"
        parameters = {"nome_orgao": nome_orgao}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"], result["data"]) for result in results]

    def update_orgao(self, nome_antigo, novo_nome, nova_data):
        query = "MATCH (o:OrgaoRegulador {nome: $old_name}) SET o.nome = $new_name, o.data_criacao = $nova_data"
        parameters = {"old_name": nome_antigo, "new_name": novo_nome, "nova_data": nova_data}
        self.db.execute_query(query, parameters)

    def deletar_orgao(self, nome_orgao):
        query = "MATCH (o:OrgaoRegulador {nome: $nome_orgao}) DETACH DELETE (o)"
        parameters = {"nome_orgao": nome_orgao}
        self.db.execute_query(query, parameters)


    def criar_temporada(self, ano):
        query = "CREATE (t:Temporada {ano: $ano})"
        parameters = {"ano": ano}
        self.db.execute_query(query, parameters)

#########################