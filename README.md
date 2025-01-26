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
Configurar entorno virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instalar dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Configurar la base de datos:

Actualiza la conexión a tu base de datos SQL Server en el archivo config.py:
python
Copiar
Editar
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://usuario:contraseña@servidor/base_datos?driver=ODBC+Driver+17+for+SQL+Server'
Ejecutar migraciones de la base de datos:

bash
Copiar
Editar
flask db init
flask db migrate -m "Inicial"
flask db upgrade
Ejecutar el servidor:

bash
Copiar
Editar
python run.py
📊 Uso del Sistema
Accede a la URL del sistema (por defecto, http://127.0.0.1:5000).
Selecciona un rango de fechas para consultar los gastos por departamento.
Visualiza los resultados en una tabla.
🤝 Contribuciones
Haz un fork del proyecto.
Crea una rama para tu nueva funcionalidad (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m "Agrega nueva funcionalidad").
Envía tus cambios (git push origin feature/nueva-funcionalidad).
Crea un Pull Request.
📝 Licencia
