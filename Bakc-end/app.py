from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request
from flask_cors import CORS

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://postgres:0000@localhost:5432/poder_publico"
CORS(app)
app.config['DEBUG_MODE'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Models.Models_legislativa import diputadoModel, senadorModel
from Models.Models_ejecutiva import presidenteModel, vicepresidenteModel
from Models.Models_judicial import fiscalModel

from app import db

@app.route('/')
def Hola_Mundo():
    return "Hola Esto es de Prueba"

#GET legislativa
@app.route('/LegislativaGET', methods=["GET"])
def Ver_Legislativa():
    legislativa=diputadoModel.query.all()
    results=[
        {
            "Nombre_diputado":Masc.Nombre_diputado,
            "Partido":Masc.Partido,
            "Distrito":Masc.Distrito,
            "Descripcion":Masc.Descripcion
        }
    for Masc in legislativa]
    return{"count": len(results), "legislativa":results}

@app.route('/Legislativa2GET', methods=["GET"])
def Ver_Legislativa2():
    legislativa2=senadorModel.query.all()
    results=[
        {
            "Nombre_senador":Masc.Nombre_senador,
            "Partido":Masc.Partido,
            "Distrito":Masc.Distrito,
            "Descripcion":Masc.Descripcion
        }
    for Masc in legislativa2]
    return{"count": len(results), "legislativa2":results}

#POST legislativa
@app.route('/LegislativaPOST',methods=["POST"])
def post_legislativa():
    if request.is_json:
        data = request.get_json()
        print(data)
        nuevo_diputado = diputadoModel(Nombre_diputado=data["Nombre del diputado"],Partido=data["Partido"],Distrito=data["Distrito"],Descripcion=data["Descripcion"])
        db.session.add(nuevo_diputado)
        db.session.commit()
        return {"message":"Nuevo diputado Creado"}
    else:
        return{"error":"Error al intentar crear un nuevo diputado"}

@app.route('/Legislativa2POST',methods=["POST"])
def post_legislativa2():
    if request.is_json:
        data = request.get_json()
        print(data)
        nuevo_senador = senadorModel(Nombre_senador=data["Nombre del senador"],Partido=data["Partido"],Distrito=data["Distrito"],Descripcion=data["Descripcion"])
        db.session.add(nuevo_senador)
        db.session.commit()
        return {"message":"Nuevo diputado Creado"}
    else:
        return{"error":"Error al intentar crear un nuevo diputado"}

#PUT legislativa 
@app.route('/LegislativaPUT', methods=["PUT"])
def put_legislativa():
    if request.is_json:
        data = request.get_json()
        Act_diputado = diputadoModel.query.get(data["id"])  
        if Act_diputado:
            Act_diputado.Nombre_diputado = data["Nombre del diputado"]
            Act_diputado.Partido = data["Partido"]
            Act_diputado.Distrito = data["Distrito"]
            Act_diputado.Descripcion = data["Descripcion"]
            db.session.commit()
            return {"message": "Diputado Actualizado"}
        else:
            return {"error": "No se encontró el Diputado con el ID proporcionado"}
    else:
        return {"error": "Error al actualizar la información del Diputado"}

@app.route('/Legislativa2PUT', methods=["PUT"])
def put_legislativa2():
    if request.is_json:
        data = request.get_json()
        Act_senador = senadorModel.query.get(data["id"]) 
        if Act_senador:
            Act_senador.Nombre_senador = data["Nombre del senador"]
            Act_senador.Partido = data["Partido"]
            Act_senador.Distrito = data["Distrito"]
            Act_senador.Descripcion = data["Descripcion"]
            db.session.commit()
            return {"message": "Senador Actualizado"}
        else:
            return {"error": "No se encontró el Senador con el ID proporcionado"}
    else:
        return {"error": "Error al actualizar la información del Senador"}
    
#DELETE legislativa
@app.route('/LegislativaDELETE/<int:id>', methods=['DELETE'])
def Delete_legislativa(id):
    Del_Diputado = diputadoModel.query.get(id)
    if Del_Diputado:
        db.session.delete(Del_Diputado)
        db.session.commit()
        return {"message": f"Diputado con ID {id} ha sido eliminada"}
    else:
        return {"error": f"No se encontró el Diputado con ID {id}"}

@app.route('/Legislativa2DELETE/<int:id>', methods=['DELETE'])
def Delete_legislativa2(id):
    Del_Senador = senadorModel.query.get(id)
    if Del_Senador:
        db.session.delete(Del_Senador)
        db.session.commit()
        return {"message": f"Senador con ID {id} ha sido eliminada"}
    else:
        return {"error": f"No se encontró el Senador con ID {id}"}

#GET ejecutiva 
@app.route('/EjecutivaGET', methods=["GET"])
def Ver_ejecutiva():
    ejecutiva=presidenteModel.query.all()
    results=[
        {
            "Nombre_Presidente":Masc.Nombre_Presidente,
            "Descripcion":Masc.Descripcion
        }
    for Masc in ejecutiva]
    return{"count": len(results), "ejecutiva":results}

@app.route('/Ejecutiva2GET', methods=["GET"])
def Ver_ejecutiva2():
    ejecutiva2=vicepresidenteModel.query.all()
    results=[
        {
            "Nombre_Vicepresidente":Masc.Nombre_Vicepresidente,
            "Descripcion":Masc.Descripcion
        }
    for Masc in ejecutiva2]
    return{"count": len(results), "ejecutiva2":results}

#POST ejecutiva 
@app.route('/EjecutivaPOST',methods=["POST"])
def post_ejecutiva():
    if request.is_json:
        data = request.get_json()
        print(data)
        nuevo_Presidente = presidenteModel(Nombre_Presidente=data["Nombre del Presidente"], Descripcion=data["Descripcion"])
        db.session.add(nuevo_Presidente)
        db.session.commit()
        return {"message":"Nuevo Presidente Creado"}
    else:
        return{"error":"Error al intentar crear un nuevo Presidente"}

@app.route('/Ejecutiva2POST',methods=["POST"])
def post_ejecutiva2():
    if request.is_json:
        data = request.get_json()
        print(data)
        nuevo_Vicepresidente = vicepresidenteModel(Nombre_Vicepresidente=data["Nombre del Vicepresidente"], Descripcion=data["Descripcion"])
        db.session.add(nuevo_Vicepresidente)
        db.session.commit()
        return {"message":"Nuevo Vicepresidente Creado"}
    else:
        return{"error":"Error al intentar crear un nuevo Vicepresidente"}

#PUT ejecutiva 
@app.route('/EjecutivaPUT', methods=["PUT"])
def put_ejecutiva():
    if request.is_json:
        data = request.get_json()
        Act_presidente = presidenteModel.query.get(data["id"])  
        if Act_presidente:
            Act_presidente.Nombre_presidente = data["Nombre del presidente"]
            Act_presidente.Descripcion = data["Descripcion"]
            db.session.commit()
            return {"message": "Presidente Actualizado"}
        else:
            return {"error": "No se encontró el Presidente con el ID proporcionado"}
    else:
        return {"error": "Error al actualizar la información del Presidente"}

@app.route('/Ejecutiva2PUT', methods=["PUT"])
def put_ejecutiva2():
    if request.is_json:
        data = request.get_json()
        Act_vicepresidente = vicepresidenteModel.query.get(data["id"]) 
        if Act_vicepresidente:
            Act_vicepresidente.Nombre_vicepresidente = data["Nombre del Vicepresidente"]
            Act_vicepresidente.Descripcion = data["Descripcion"]
            db.session.commit()
            return {"message": "Vicepresidente Actualizado"}
        else:
            return {"error": "No se encontró el Vicepresidente con el ID proporcionado"}
    else:
        return {"error": "Error al actualizar la información del Vicepresidente"}

#DELETE ejecutiva 
@app.route('/EjecutivaDELETE/<int:id>', methods=['DELETE'])
def Delete_ejecutiva(id):
    Del_presidente = presidenteModel.query.get(id)
    if Del_presidente:
        db.session.delete(Del_presidente)
        db.session.commit()
        return {"message": f"Presidente con ID {id} ha sido eliminada"}
    else:
        return {"error": f"No se encontró el Presidente con ID {id}"}

@app.route('/Ejecutiva2DELETE/<int:id>', methods=['DELETE'])
def Delete_ejecutiva2(id):
    Del_vicepresidente = vicepresidenteModel.query.get(id)
    if Del_vicepresidente:
        db.session.delete(Del_vicepresidente)
        db.session.commit()
        return {"message": f"Vicepresidente con ID {id} ha sido eliminada"}
    else:
        return {"error": f"No se encontró el Vicepresidente con ID {id}"}
    
#GET judicial
@app.route('/JudicialGET', methods=["GET"])
def Ver_judicial():
    judicial=fiscalModel.query.all()
    results=[
        {
            "Nombre_Fiscal":Masc.Nombre_Fiscal,
            "Descripcion":Masc.Descripcion
        }
    for Masc in judicial]
    return{"count": len(results), "judicial":results}

#POST judicial 
@app.route('/JudicialPOST',methods=["POST"])
def post_judicial():
    if request.is_json:
        data = request.get_json()
        print(data)
        nuevo_Fiscal = fiscalModel(Nombre_Fiscal=data["Nombre del Fiscal general de la nacion"], Descripcion=data["Descripcion"])
        db.session.add(nuevo_Fiscal)
        db.session.commit()
        return {"message":"Nuevo Fiscal Creado"}
    else:
        return{"error":"Error al intentar crear un nuevo Fiscal"}

#PUT judicial
@app.route('/JudicialPUT', methods=["PUT"])
def put_judicial():
    if request.is_json:
        data = request.get_json()
        Act_fiscal = fiscalModel.query.get(data["id"])  
        if Act_fiscal:
            Act_fiscal.Nombre_Fiscal = data["Nombre del Fiscal general de la nacion"]
            Act_fiscal.Descripcion = data["Descripcion"]
            db.session.commit()
            return {"message":"Fiscal Actualizado"}
        else:
            return {"error": "No se encontró el Fiscal con el ID proporcionado"}
    else:
        return {"error": "Error al actualizar la información del Fiscal"}

#DELETE judicial
@app.route('/JudicialDELETE/<int:id>', methods=['DELETE'])
def Delete_judicial(id):
    Del_fiscal = fiscalModel.query.get(id)
    if Del_fiscal:
        db.session.delete(Del_fiscal)
        db.session.commit()
        return {"message": f"Fiscal con ID {id} ha sido eliminada"}
    else:
        return {"error": f"No se encontró el Fiscal con ID {id}"}
