from flask import Flask,jsonify,request

app = Flask(__name__)

musicas = [
    {
        "cancao":"Your Love",
        "artista":"The Outfield"
    },
    {
        "cancao": "Wish You Were Here",
        "artista": "Pink Floyd"
    },
    {
        "cancao":"I Want To Break Free",
        "artista": "Queen"
    },
    {
        "cancao":"I Want To Know What Love Is",
        "artista": "Foreigner"
    }
]

#Rota padrão - GET http://localhost:5000
@app.route('/')
def obter_musicas():
    return jsonify(musicas)

#Obter postagem por id - GET http://localhost:5000/musicas/id
@app.route('/musicas/<int:indice>',methods=['GET'])
def obter_musica_por_id(indice):
    return jsonify(musicas[indice],200)

#Criar uma nova Musica - POST
@app.route('/musicas',methods=['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)

    return jsonify(musica,200)

#Alterar uma Musica - PUT
@app.route('/musicas/<int:indice>',methods=['PUT'])
def alterar_musica(indice):
   musica_alterada = request.get_json()
   musicas[indice].update(musica_alterada)

   return jsonify(musicas[indice],200)

#Exlcuindo uma musica - DELETE
@app.route('/musicas/<int:indice>',methods=['DELETE'])
def excluir_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f"Musica {musicas[indice]} excluida",200)
    except :
        return jsonify({"status":"Musica não encontrada"},404)


app.run(port=5000,host='localhost',debug=True)