# 🐍 Proyecto Django - Backend basic until intermediate

Este proyecto es una API REST construida con Django y Django REST Framework. Permite [describir brevemente qué hace: gestionar usuarios, clientes, ventas, etc.].

---

## 🛠️ Tecnologías Usadas

- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL / SQLite
- JWT / Token Authentication
- CORS Headers
- (otros: Celery, Redis, Swagger, etc.)

---

## ⚙️ Requisitos

- Python >= 3.11
- pip
- virtualenv (recomendado)
- PostgreSQL o SQLite (según configuración)

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate



# Migraciones
python manage.py makemigrations && python manage.py migrate

# Crear superusuario, productos, clientes, etc.. 
python manage.py createsuperuser

# Correr el servidor
python manage.py runserver

# ver documentacion del swagger
#http://localhost:8000/swagger/

# para authenticar y tener acceso a ls rutas protegidas: 
http://127.0.0.1:8000/api/login/

POST /api/login/
{
  "username": "admin",
  "password": "admin"
}



| Método | Endpoint      | Descripción             |
| ------ | ------------- | ----------------------- |
| GET    | `/api/users/` | Listar usuarios         |
| POST   | `/api/users/` | Crear usuario           |
| POST   | `/api/token/` | Obtener token JWT       |
| GET    | `/admin/`     | Panel de administración |

# Clic en Authorize (swagger) → pega:
Clave: Bearer <tu_token>
Authorization: Bearer <token>


backend/
├── manage.py
├── backend/           # Configuración principal
│   ├── settings.py
│   └── urls.py
├── users/             # App personalizada
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── authusers/             # App personalizada
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── products/             # App personalizada
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── ...

#genera el archivo para tus dependencias
pip freeze > requirements.txt

# Instalar dependencias
pip install -r requirements.txt

#instalar token_blacklist en commillas
pip install 'djangorestframework-simplejwt[token_blacklist]'
