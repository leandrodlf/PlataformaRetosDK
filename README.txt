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
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Lista de Endpoints

Páginas Web
Endpoint					Método					Descripción
/						GET					Página principal, muestra categorías, retos destacados y ranking de usuarios.
/retos/						GET					Lista todos los retos filtrables por categoría y dificultad.
/reto/<reto_id>/				GET					Detalle de un reto (formulario para responder).
/ranking/					GET					Ranking de usuarios según puntos acumulados.
/registro/					GET, POST				Registro de nuevos usuarios.
/login/						GET, POST				Login de usuarios.
/logout/					GET					Cierra sesión y redirige al home.

APIs Existentes

Endpoint					Método					Descripción
/reto/<reto_id>/				POST					Recibe la respuesta de un usuario a un reto y devuelve JSON indicando si la respuesta es correcta. ({'correcto': True/False})
/api/retos/					GET	 				Obtiene lista de retos activos. Evidencia ESB en consola.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Evidencia del ESB
URL: http://localhost:8000/api/retos/

Al usar la nueva APIs, el ESB mostrará en la consola de Docker:

🔗 ESB - API_RETOS ejecutó: OBTENER_RETOS

   Datos: 62 retos obtenidos

