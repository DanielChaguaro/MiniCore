from flask import render_template , request
from app.Models.db import db
from app.Models.Gasto import Gasto
from app.Models.Empleado import Empleado
from app.Models.Departamento import Departamento
from sqlalchemy import func
from datetime import datetime


def recomendaciones_basicas():
    fecha_inicial = request.form.get('fecha_inicial')
    fecha_final = request.form.get('fecha_final')
    if fecha_inicial:
            fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    else:
            fecha_inicial = datetime.strptime('2000-01-01', "%Y-%m-%d")

    if fecha_final:
            fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
    else:
            fecha_final =  datetime.strptime('2025-12-31', "%Y-%m-%d")
    totales_por_departamento = (
            db.session.query(
                Departamento.nombre.label("departamento"),
                func.sum(Gasto.monto).label("total_monto")
            )
            .join(Gasto, Gasto.id_dept == Departamento.id)
            .filter(Gasto.fecha >= fecha_inicial)
            .filter(Gasto.fecha <= fecha_final)
            .group_by(Departamento.nombre)
            .all()
    )
    resultados = [{"departamento": t.departamento, "total_monto": t.total_monto or 0} for t in totales_por_departamento]

    return render_template('recomendaciones.html', resultados=resultados)