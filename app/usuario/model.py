from ..extensions import db

class Usuario(db.Model):
    __tablename__           = 'usuario'
    id                      = db.Column(db.Integer, primary_key=True)
    username                = db.Column(db.String(63), nullable=False)
    senha                   = db.Column(db.String(63), nullable=False)
    nome                    = db.Column(db.String(63), nullable=False)
    endereco                = db.Column(db.String(127), nullable=False)

    pets                    = db.relationship("Pet", backref="usuario")
