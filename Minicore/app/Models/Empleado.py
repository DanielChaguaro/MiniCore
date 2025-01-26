from app.Models.db import db

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    # Relación con la tabla Gastos
    gastos = db.relationship('Gasto', back_populates='empleado', cascade='all, delete-orphan')
