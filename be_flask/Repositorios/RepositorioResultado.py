from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):

    def getListadoCandidatosInscritosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getNumeroCedulaMayorCandidato(self):
        query = {
            "$group": {
                "_id": "$candidato",
                "max": {
                    "$max": "$numero_votos" # cedula
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)

    def sumaVotosCandidato(self, id_candidato):
        query1 = {
            "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
            "$group": {
                "_id": "$candidato",
                "TotalVotos": {
                    "$sum": "$numero_votos"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)