from app import db 

class diputadoModel(db.Model):
    __tablename__='Diputado'
    id = db.Column(db.Integer, primary_key=True)
    Nombre_diputado = db.Column(db.String())
    Partido = db.Column(db.String())
    Distrito = db.Column(db.String())
    Descripcion = db.Column(db.String())
def __init__(self,Nombre_diputado, Partido, Distrito, Descripcion):
    self.Nombre_diputado = Nombre_diputado
    self.Partido = Partido
    self.Distrito = Distrito
    self.Descripcion = Descripcion
def __repr__(self):
    return f"<Masc {self.Nombre_diputado}>"

class senadorModel(db.Model):
    __tablename__='Senador'
    id = db.Column(db.Integer, primary_key=True)
    Nombre_senador = db.Column(db.String())
    Partido = db.Column(db.String())
    Distrito = db.Column(db.String())
    Descripcion =  db.Column(db.String())
def __init__(self,Nombre_senador, Partido, Distrito, Descripcion):
    self.Nombre_senador = Nombre_senador
    self.Partido = Partido
    self.Distrito = Distrito
    self.descripcion = Descripcion
def __repr__(self):
    return f"<Masc {self.Nombre_senador}>"




