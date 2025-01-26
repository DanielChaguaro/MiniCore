# Sistema de Gestión de Gastos por Departamento

Este proyecto es un sistema web desarrollado en **Python** utilizando Flask y SQLAlchemy que permite gestionar y visualizar los gastos realizados por empleados de diferentes departamentos.

## 🚀 Características Principales
1. **Gestión de Datos:**
   - Registro de empleados, departamentos y gastos.
   - Relaciones entre tablas:
     - Gasto → Empleado → Departamento.

2. **Consulta de Gastos:**
   - Permite consultar el gasto total por departamento en un rango de fechas.

3. **Diseño Modular:**
   - Estructura basada en el patrón **MVC**.

## 🛠️ Tecnologías Usadas
- **Backend:** Flask, SQLAlchemy.
- **Frontend:** HTML, Jinja2, Bootstrap.
- **Base de Datos:** SQL Server (ODBC Driver 17).
- **Control de Versiones:** Git y GitHub.

## 📂 Estructura del Proyecto
📦 app/ ┣ 📂 models/ ┃ ┣ empleado.py ┃ ┣ departamento.py ┃ ┣ gasto.py ┣ 📂 controllers/ ┃ ┣ gastos.py ┣ 📂 templates/ ┃ ┣ recomendaciones.html ┣ init.py ┣ config.py ┣ run.py

bash
Copiar
Editar

## ⚙️ Configuración e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
   cd nombre-del-repositorio
Configurar entorno:  
   pip install pyodbc flask sqlalchemy flask-sqlalchemy
   python main.py

   
📊 Uso del Sistema
Accede a la URL del sistema (por defecto, http://127.0.0.1:5000).
Selecciona un rango de fechas para consultar los gastos por departamento.
Visualiza los resultados en una tabla.
