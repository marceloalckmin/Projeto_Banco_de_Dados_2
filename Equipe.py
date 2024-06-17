from Piloto import Piloto

class Equipe:
    def __init__(self, database):
        self.db = database
        self.pilotos = []

    def criar_equipe(self, nome, pais, data):
        query = "CREATE (:Equipe {nome_equipe: $nome, pais_equipe: $pais, data_criacao: $data})"
        parameters = {"nome": nome, "pais": pais, "data": data}
        self.db.execute_query(query, parameters)

    def read_equipe(self,nomeEquipe):
        query = "MATCH (e:Equipe {nome_equipe: $nomeEquipe}) RETURN e.nome_equipe AS nome_equipe, e.pais_equipe AS pais_equipe"
        parameters = {"nomeEquipe": nomeEquipe}
        results = self.db.execute_query(query, parameters)
        return [(result["nome_equipe"], result["pais_equipe"]) for result in results]

    def ver_pilotos(self, nome_equipe):
        query = "MATCH (p:Piloto)-[:CORRE_PARA]->(e:Equipe{nome_equipe: $nome_equipe}) RETURN p.nome_piloto AS nome_piloto"
        parameters = {"nome_equipe": nome_equipe}
        results = self.db.execute_query(query, parameters)
        return [(result["nome_piloto"]) for result in results]

    def update_equipe(self, old_nome, new_nome, new_pais, new_data):
        query = """
        MATCH (e:Equipe {nome_equipe: $old_nome})
        SET e.nome_equipe = $new_nome, e.pais_equipe = $new_pais, e.data_criacao = $new_data
        """
        parameters = {"old_nome": old_nome, "new_nome": new_nome, "new_pais": new_pais, "new_data": new_data}
        self.db.execute_query(query, parameters)

    def delete_equipe(self, nomeEquipe):
        query = "MATCH (e:Equipe {nome_equipe: $nomeEquipe}) DETACH DELETE (e)"
        parameters = {"nomeEquipe": nomeEquipe}
        self.db.execute_query(query, parameters)

    def adicionar_piloto(self, nome, numero):
        piloto = Piloto(nome, numero)
        self.pilotos.append(piloto)

    def adicionar_piloto_db(self, nome, pais, data_nasc):
        query = "CREATE (:Piloto {nome_piloto: $nome, pais_piloto: $pais, data_nasc: $data_nasc})"
        parameters = {"nome": nome, "pais": pais, "data_nasc": data_nasc}
        self.db.execute_query(query, parameters)

    def ligar_piloto_equipe(self, nome_piloto, nome_equipe):
        query = "MATCH (p:Piloto{nome_piloto: $nome_piloto}), (e:Equipe {nome_equipe: $nome_equipe}) CREATE (p)-[:CORRE_PARA]->(e)"
        parameters = {"nome_piloto": nome_piloto, "nome_equipe": nome_equipe}
        self.db.execute_query(query, parameters)



    #########################
