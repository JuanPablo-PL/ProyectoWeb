from app import db 

class presidenteModel(db.Model):
    __tablename__='Presidente'
    id = db.Column(db.Integer, primary_key=True)
    Nombre_Presidente = db.Column(db.String())
    Descripcion = db.Column(db.String())
def __init__(self,Nombre_Presidente,Descripcion):
    self.Nombre_Presidente = Nombre_Presidente
    self.Descripcion = Descripcion
def __repr__(self):
    return f"<Masc {self.Nombre_Presidente}>"

class vicepresidenteModel(db.Model):
    __tablename__='Vicepresidente'
    id = db.Column(db.Integer, primary_key=True)
    Nombre_Vicepresidente = db.Column(db.String())
    Descripcion =  db.Column(db.String())
def __init__(self,Nombre_Vicepresidente, Descripcion):
    self.Nombre_Vicepresidente = Nombre_Vicepresidente
    self.Descripcion = Descripcion
def __repr__(self):
    return f"<Masc {self.Nombre_Vicepresidente}>"