from app.Models.db import db

class Departamento(db.Model):
    __tablename__ = 'departamentos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    # Relación con la tabla Gastos
    gastos = db.relationship('Gasto', back_populates='departamento', cascade='all, delete-orphan')
