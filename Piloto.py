class Piloto:
    def __init__(self, nome, pais, data_nasc):
        self.nome = nome
        self.pais = pais
        self.data_nasc = data_nasc

    def get_nome(self):
        return self.nome

    def get_pais(self):
        return self.pais

    def get_nasc(self):
        return self.data_nasc

    #########################

'''

CREATE (:Corrida {nome_corrida: "Grande Premio do Brasil", pais_corrida: "Brasil", pista: "Interlagos", data_corrida: "22-09-2024"})

CREATE (o:OrgaoRegulador {nome: "FIA", data_criacao: "20-03-1953"})

CREATE (o:Temporada {ano: 2023})

MATCH (c:Temporada {ano: 2023}), (o:OrgaoRegulador {nome: "FIA"})
CREATE (c)-[:REGULADA_POR]->(o)

MATCH (t:Temporada {ano: 2023}), (c:Corrida {nome_corrida: "Grande Premio do Brasil"})
CREATE (t)-[:INCLUI]->(c)

CREATE (:Piloto {nome_piloto: "Lewis Hamilton", pais_piloto: "Reino Unido", data_nasc: "07-01-1985"})
CREATE (:Piloto {nome_piloto: "Max Verstappen", pais_piloto: "Holanda", data_nasc: "30-09-1997"})
CREATE (:Piloto {nome_piloto: "George Russell", pais_piloto: "Reino Unido", data_nasc: "15-02-1998"})
CREATE (:Piloto {nome_piloto: "Lando Norris", pais_piloto: "Reino Unido", data_nasc: "13-11-1999"})
CREATE (:Piloto {nome_piloto: "Oscar Piastri", pais_piloto: "Austrália", data_nasc: "06-04-2001"})
CREATE (:Piloto {nome_piloto: "Sergio Perez", pais_piloto: "México", data_nasc: "26-01-1990"})
CREATE (:Piloto {nome_piloto: "Charles Leclerc", pais_piloto: "Mônaco", data_nasc: "16-10-1997"})
CREATE (:Piloto {nome_piloto: "Carlos Sainz", pais_piloto: "Espanha", data_nasc: "01-09-1994"})
CREATE (:Piloto {nome_piloto: "Fernando Alonso", pais_piloto: "Espanha", data_nasc: "29-07-1981"})
CREATE (:Piloto {nome_piloto: "Esteban Ocon", pais_piloto: "França", data_nasc: "17-09-1996"})
CREATE (:Piloto {nome_piloto: "Pierre Gasly", pais_piloto: "França", data_nasc: "07-02-1996"})
CREATE (:Piloto {nome_piloto: "Lance Stroll", pais_piloto: "Canadá", data_nasc: "29-10-1998"})
CREATE (:Piloto {nome_piloto: "Kevin Magnussen", pais_piloto: "Dinamarca", data_nasc: "05-10-1992"})
CREATE (:Piloto {nome_piloto: "Nico Hulkenberg", pais_piloto: "Alemanha", data_nasc: "19-08-1987"})
CREATE (:Piloto {nome_piloto: "Valtteri Bottas", pais_piloto: "Finlândia", data_nasc: "28-08-1989"})
CREATE (:Piloto {nome_piloto: "Guanyu Zhou", pais_piloto: "China", data_nasc: "30-05-1999"})
CREATE (:Piloto {nome_piloto: "Yuki Tsunoda", pais_piloto: "Japão", data_nasc: "11-05-2000"})
CREATE (:Piloto {nome_piloto: "Nyck de Vries", pais_piloto: "Holanda", data_nasc: "06-02-1995"})
CREATE (:Piloto {nome_piloto: "Alexander Albon", pais_piloto: "Tailândia", data_nasc: "23-03-1996"})
CREATE (:Piloto {nome_piloto: "Logan Sargeant", pais_piloto: "Estados Unidos", data_nasc: "31-12-2000"})


CREATE (:Equipe {nome_equipe: "Mercedes", pais_equipe: "Reino Unido"})
CREATE (:Equipe {nome_equipe: "Red Bull Racing", pais_equipe: "Reino Unido"})
CREATE (:Equipe {nome_equipe: "Ferrari", pais_equipe: "Itália"})
CREATE (:Equipe {nome_equipe: "McLaren", pais_equipe: "Reino Unido"})
CREATE (:Equipe {nome_equipe: "Alpine", pais_equipe: "França"})
CREATE (:Equipe {nome_equipe: "Aston Martin", pais_equipe: "Reino Unido"})
CREATE (:Equipe {nome_equipe: "AlphaTauri", pais_equipe: "Itália"})
CREATE (:Equipe {nome_equipe: "Alfa Romeo Racing", pais_equipe: "Suíça"})
CREATE (:Equipe {nome_equipe: "Haas", pais_equipe: "Estados Unidos"})
CREATE (:Equipe {nome_equipe: "Williams", pais_equipe: "Reino Unido"})


MATCH (p:Piloto {nome_piloto: "Lewis Hamilton"}), (e:Equipe {nome_equipe: "Mercedes"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "George Russell"}), (e:Equipe {nome_equipe: "Mercedes"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Max Verstappen"}), (e:Equipe {nome_equipe: "Red Bull Racing"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Sergio Perez"}), (e:Equipe {nome_equipe: "Red Bull Racing"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Lando Norris"}), (e:Equipe {nome_equipe: "McLaren"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Oscar Piastri"}), (e:Equipe {nome_equipe: "McLaren"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Charles Leclerc"}), (e:Equipe {nome_equipe: "Ferrari"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Carlos Sainz"}), (e:Equipe {nome_equipe: "Ferrari"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Fernando Alonso"}), (e:Equipe {nome_equipe: "Aston Martin"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Lance Stroll"}), (e:Equipe {nome_equipe: "Aston Martin"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Esteban Ocon"}), (e:Equipe {nome_equipe: "Alpine"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Pierre Gasly"}), (e:Equipe {nome_equipe: "Alpine"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Kevin Magnussen"}), (e:Equipe {nome_equipe: "Haas"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Nico Hulkenberg"}), (e:Equipe {nome_equipe: "Haas"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Valtteri Bottas"}), (e:Equipe {nome_equipe: "Alfa Romeo Racing"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Guanyu Zhou"}), (e:Equipe {nome_equipe: "Alfa Romeo Racing"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Yuki Tsunoda"}), (e:Equipe {nome_equipe: "AlphaTauri"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Nyck de Vries"}), (e:Equipe {nome_equipe: "AlphaTauri"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Alexander Albon"}), (e:Equipe {nome_equipe: "Williams"})
CREATE (p)-[:CORRE_PARA]->(e)

MATCH (p:Piloto {nome_piloto: "Logan Sargeant"}), (e:Equipe {nome_equipe: "Williams"})
CREATE (p)-[:CORRE_PARA]->(e)







MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Lewis Hamilton"})
CREATE (p)-[:PARTICIPOU {posicao_final: 1}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Max Verstappen"})
CREATE (p)-[:PARTICIPOU {posicao_final: 2}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "George Russell"})
CREATE (p)-[:PARTICIPOU {posicao_final: 3}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Lando Norris"})
CREATE (p)-[:PARTICIPOU {posicao_final: 4}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Oscar Piastri"})
CREATE (p)-[:PARTICIPOU {posicao_final: 5}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Sergio Perez"})
CREATE (p)-[:PARTICIPOU {posicao_final: 6}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Charles Leclerc"})
CREATE (p)-[:PARTICIPOU {posicao_final: 7}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Carlos Sainz"})
CREATE (p)-[:PARTICIPOU {posicao_final: 8}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Fernando Alonso"})
CREATE (p)-[:PARTICIPOU {posicao_final: 9}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Esteban Ocon"})
CREATE (p)-[:PARTICIPOU {posicao_final: 10}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Pierre Gasly"})
CREATE (p)-[:PARTICIPOU {posicao_final: 11}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Lance Stroll"})
CREATE (p)-[:PARTICIPOU {posicao_final: 12}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Kevin Magnussen"})
CREATE (p)-[:PARTICIPOU {posicao_final: 13}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Nico Hulkenberg"})
CREATE (p)-[:PARTICIPOU {posicao_final: 14}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Valtteri Bottas"})
CREATE (p)-[:PARTICIPOU {posicao_final: 15}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Guanyu Zhou"})
CREATE (p)-[:PARTICIPOU {posicao_final: 16}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Yuki Tsunoda"})
CREATE (p)-[:PARTICIPOU {posicao_final: 17}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Nyck de Vries"})
CREATE (p)-[:PARTICIPOU {posicao_final: 18}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Alexander Albon"})
CREATE (p)-[:PARTICIPOU {posicao_final: 19}]->(c)

MATCH (c:Corrida {nome_corrida: "Grande Premio do Brasil"}), (p:Piloto {nome_piloto: "Logan Sargeant"})
CREATE (p)-[:PARTICIPOU {posicao_final: 20}]->(c)




#RETORNA O NOME DO PILOTO E A POSIÇÃO DELE NA CORRIDA
MATCH (c:Corrida {nome: "Grande Premio do Brasil"})<-[par:PARTICIPOU]-(p:Piloto)
return par.posicao_final as posicao, p.nome as nomePiloto








'''