PlataformaRetos/
├── manage.py                
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
├── plataforma_retos/        
│   ├── settings.py          
│   ├── urls.py              
│   └── ...
└──── retos/                   
    ├── models.py            
    ├── views.py             
    ├── urls.py              
    ├── templates/           
    └── management/commands/ 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Descripción

Plataforma web educativa desarrollada con Django para resolver retos matemáticos y lógicos.
Incluye sistema de puntuación, ranking de usuarios y panel de administración.

Funciona completamente con Docker, usando PostgreSQL como base de datos.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Requisitos del Sistema
Software necesario:
	Docker Desktop instalado (Windows 10/11, Linux o macOS)
	Navegador web (Chrome, Firefox, Edge)
No necesitas instalar Python ni crear entornos virtuales.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Instalación Paso a Paso

1. Descargar el proyecto
	Coloca la carpeta PlataformaRetos en el Escritorio.

2. Abrir la terminal y navegar al proyecto (o en su defecto ejecutar la terminal en la carpeta correspondiente).
	Windows/Linux: cd ~/Desktop/PlataformaRetosDK

3. Construir las imágenes y levantar los contenedores
	docker compose build --no-cache
	docker compose up -d

4. Aplicar migraciones
	docker compose exec web python manage.py migrate

5. Cargar datos iniciales
	docker compose exec web python manage.py cargar_datos

6. Acceder a la plataforma
	Abre tu navegador y ve a:
		Plataforma principal: http://localhost:8000/
		Panel de administración: http://localhost:8000/admin/

7. Credenciales superusuario
	Usuario: inacap
	Password: inacap


