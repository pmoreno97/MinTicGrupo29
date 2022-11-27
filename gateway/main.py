from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import datetime
import requests
import re

app = Flask(__name__)
cors = CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


@app.before_request
def before_request_callback():
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        print("ruta excluida ", request.path)
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePersmiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            if not tienePersmiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401


def limpiarURL(url):
    partes = request.path.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint, metodo, idRol):
    url = dataConfig["url-backend-security"] + "/permisos-roles/validar-permiso/rol/" + str(idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


####################################mesas###################

@app.route("/mesas", methods=['GET'])
def getMesas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/mesas'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/mesas'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/mesas/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/mesas/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/mesas/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)


##############################

####################################partidos###################

@app.route("/partidos", methods=['GET'])
def getPartidos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/partidos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/partidos'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/partidos/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/partidos/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/partidos/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/candidatos/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartidoCandidato(id, id_partido):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/candidatos/' + id + '/partido/' + id_partido
    response = requests.put(url, headers=headers)
    json = response.json()
    return jsonify(json)


##############################

####################################candidatos###################

@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/candidatos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/candidatos'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/candidatos/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/candidatos/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/candidatos/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)


##############################

####################################resultados###################

@app.route("/resultados", methods=['GET'])
def getResultados():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def crearResultado(id_candidato, id_mesa):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados' + '/candidato/' + id_candidato + '/mesa/' + id_mesa
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def modificarResultado(id_resultado,id_candidato,id_mesa):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + id_resultado + '/candidato/' + id_candidato + '/mesa/' + id_mesa
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)


####################################Visualización Reportes###################

@app.route("/resultados/mesas/<string:id_mesa>", methods=['GET'])
def inscritosMesa(id_mesa):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + '/mesas/' + id_mesa
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/MESAS/<string:id_candidato>", methods=['GET'])
def inscritoEnMesas(id_candidato):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + '/MESAS/' + id_candidato
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/totalvotos", methods=['GET'])
def getMaxDocument():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + '/totalvotos/'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/resultados/suma_votos/candidatos/<string:id_candidato>", methods=['GET'])
def getSumaVotosCandidato(id_candidato):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-academic"] + '/resultados/' + '/suma_votos/' + '/candidatos/' + id_candidato
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


##############################USUARIOS#############

@app.route("/usuarios", methods=['GET'])
def getUsuarios():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios", methods=['POST'])
def crearUsuario():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/usuarios/<string:id>", methods=['GET'])
def getUsuario(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/usuarios/<string:id>", methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/usuarios/<string:id>", methods=['DELETE'])
def eliminarUsuario(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

################################

##############################ROLES#############

@app.route("/roles", methods=['GET'])
def getRoles():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/roles", methods=['POST'])
def crearRol():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['GET'])
def getRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles/' + id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['PUT'])
def modificarRol(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles/' + id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/roles/<string:id>", methods=['DELETE'])
def eliminarRol(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/roles/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

################################


@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"] + '/usuarios/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60 * 24)
        access_token = create_access_token(identity=user,
                                           expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"msg": "Bad username or password"}), 401


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" +
          str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
