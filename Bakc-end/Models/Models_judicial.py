from app import db  

class fiscalModel(db.Model):
    __tablename__='Fiscal_general'
    id = db.Column(db.Integer, primary_key=True)
    Nombre_Fiscal = db.Column(db.String())
    Descripcion = db.Column(db.String())
def __init__(self,Nombre_Fiscal,Descripcion):
    self.Nombre_Fiscal = Nombre_Fiscal
    self.Descripcion = Descripcion
def __repr__(self):
    return f"<Masc {self.Nombre_Fiscal}>"