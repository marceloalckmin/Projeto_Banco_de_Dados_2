from database import Database
from cli import AutomobilismoCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.239.237.85:7687", "neo4j", "crystals-charts-counts")
#db.drop_all()

autoCLI = AutomobilismoCLI(db)
autoCLI.run()

#fechando db
db.close()