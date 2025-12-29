# 🐾 Patitas Felices – Back End (API con Flask)

API REST desarrollada con **Python y Flask** para gestionar datos de mascotas en el proyecto _Patitas Felices_.  
Este backend provee los endpoints que consume el frontend alojado en Netlify.

---

## 📌 Descripción del proyecto

Este proyecto forma parte de una aplicación web completa para llevar un registro y gestión de mascotas.  
El backend está construido con Flask y expone una serie de **endpoints REST** que permiten:

- listar mascotas
- registrar nuevas mascotas
- actualizar y eliminar mascotas
- gestionar datos relacionados al sistema

El frontend se conecta a esta API para mostrar y modificar información desde la interfaz de usuario.

---

## 🛠️ Tecnologías y herramientas utilizadas

**Lenguajes**

- Python 🐍

**Frameworks / Librerías**

- Flask (microframework web para APIs)

**Control de versiones**

- Git & GitHub

**Deploy / Hosting**

- API alojada (por ejemplo en PythonAnywhere o similar; incluye link en la descripción)

---

## 🚀 Deploy en producción

🔗 **API pública (deploy):**  
https://s3b4.pythonanywhere.com/

👉 Usá esta URL como base para hacer requests desde tu frontend o herramientas como Postman o Insomnia.

---

## 📁 Estructura del proyecto

```text
PatitasFelices-Backend/
                    ├── controllers/     # Controladores que manejan la lógica de cada ruta
                    ├── models/          # Modelos de datos y estructuras
                    ├── routes/          # Definición de rutas de la API
                    ├── schemas/         # Esquemas para validación y serialización
                    ├── utils/           # Utilidades de apoyo para el backend
                    ├── public/          # Recursos públicos (imágenes, assets, etc.)
                    ├── app.py           # Punto de entrada principal
                    ├── requirements.txt # Dependencias del proyecto
                    └── README.md        # Documentación del proyecto
```

📦 Requisitos

Antes de ejecutar localmente, necesitás:

🔹 Python 3.8+
🔹 Pip o entorno virtual

🛠️ Ejecución local

Clonar el repositorio

```bash
git clone https://github.com/SHA-Arg/TP-Codo-a-Codo-DesarrolloWeb-Mascotas-Backend.git
cd TP-Codo-a-Codo-DesarrolloWeb-Mascotas-Backend
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Iniciar el servidor

```bash
python app.py
```

La API correrá típicamente en http://localhost:5000/.

🔌 Endpoints disponibles

Los principales endpoints que provee esta API incluyen (según estructura de rutas):

| Verbo  | Ruta             | Descripción               |
| ------ | ---------------- | ------------------------- |
| GET    | `/mascotas`      | Listar todas las mascotas |
| POST   | `/mascotas`      | Crear una nueva mascota   |
| GET    | `/mascotas/<id>` | Obtener mascota por ID    |
| PUT    | `/mascotas/<id>` | Actualizar mascota por ID |
| DELETE | `/mascotas/<id>` | Eliminar mascota por ID   |

🧠 ¿Cómo se integra con el Frontend?

Este backend provee datos y lógica para el frontend del proyecto Patitas Felices, alojado en:

🔗 https://github.com/SHA-Arg/TP-Codo-a-Codo-DesarrolloWeb-Mascotas

El frontend hace fetch API requests a los endpoints listados arriba para mostrar y actualizar información en la interfaz de usuario.
GitHub

📌 Buenas prácticas y aprendizajes

Con este proyecto pusiste en práctica:

✔️ Desarrollo de APIs con Flask ✔️
✔️ Gestión de rutas y lógica backend ✔️
✔️ Manejo de datos y esquemas ✔️
✔️ Integración frontend-backend desplegada ✔️
✔️ Uso de Git para control de versiones ✔️

Este tipo de proyectos es excelente para aprender cómo construir y mantener un backend funcional para aplicaciones web.
4Geeks

👤 Autores
Andrea Jiménez Espinoza
🔗 https://github.com/andreajimeneze

Sofía Egaña Jiménez
🔗 https://github.com/SofiaInSilico

Sebastian Hereñu Amaral
🔗 https://github.com/SHA-Arg

🌐 Portfolio: https://sha-arg.github.io

Edson Yañez
🔗 https://github.com/edson-yanez-villa
