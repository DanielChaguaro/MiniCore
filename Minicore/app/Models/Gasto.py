from app.Models.db import db

class Gasto(db.Model):
    __tablename__ = 'gastos'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    id_dept = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)

    # Relación inversa
    empleado = db.relationship('Empleado', back_populates='gastos')
    departamento = db.relationship('Departamento', back_populates='gastos')