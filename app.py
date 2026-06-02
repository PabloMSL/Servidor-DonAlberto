from flask import  Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/api/repuestos')
def get_repuestos():
        return jsonify({
          "status" : "Online",
          "servidor" : "Linux-Ubuntu usado por pablo",
          "hora_servidor" : str(datetime.datetime.now()),
          "inventario" : ["Bujias de Iridio", "Filtro de aceite", "Aceite motul 7100"]
        })

peritajes_db = [{"placa":"ABC-123", "estado": "En revision"}]

@app.route('/api/registros', methods=['GET'])
def get_registros():
    return jsonify({
       "servidor": "Servidor Mozuca",
       "hora_servidor": str(datetime.datetime.now()),
       "inventario": ["Llanta delantera", "Aceite 10W40", "Cadena Reforzada"],
    })

@app.route('/api/peritajes', methods=['GET', 'POST'])
def gestionar_peritajes():
    if request.method == 'POST':
        datos = request.get_json()
        nueva_moto = {"placa": datos['placa'].upper(), "estado": "Recibida"}
        peritajes_db.append(nueva_moto)
        return jsonify({"mensaje": "Registro Exitoso", "moto": nueva_moto}), 201
    return jsonify(peritajes_db)


if __name__ == "__main__":
         app.run()

@app.route('/api/inventario', methods=['GET', 'POST'])
def gestionar_inventario():
      if request.method == 'POST':