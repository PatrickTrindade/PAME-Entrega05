from ..extensions import db

class Produto(db.Model):
    __tablename__           = 'produto'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    descricao               = db.Column(db.String(127), default="")
    qnt_estoque             = db.Column(db.Integer, default=0)
    