# Proyecto HTML a PDF

Este proyecto es una API en FastAPI que recibe contenido HTML y lo convierte a PDF en formato base64.

## 🛠 Requisitos

Asegúrate de tener instalado lo siguiente en tu sistema:

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Chocolatey (para instalar `wkhtmltopdf` en Windows)

## 🚀 Instalación

1. **Clona el repositorio:**

   Abre tu terminal y ejecuta:

   ```bash
   git clone https://github.com/tuusuario/html_to_pdf.git
   cd html_to_pdf
   ```

2. **Crea y activa un entorno virtual:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # En PowerShell
   ```

3. **Instala los paquetes necesarios:**

   Asegúrate de que tu entorno virtual está activo y ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

4. **Instala `wkhtmltopdf`:**

   Si no tienes `wkhtmltopdf` instalado, puedes usar Chocolatey. Abre PowerShell como administrador y ejecuta:

   ```bash
   choco install wkhtmltopdf
   ```

   Si no tienes Chocolatey instalado, puedes seguir las instrucciones en [su sitio web oficial](https://chocolatey.org/install).

## 🚀 Ejecución del proyecto

1. **Ejecuta el servidor FastAPI:**

   Asegúrate de estar en la raíz del proyecto y que el entorno virtual esté activado. Luego ejecuta:

   ```bash
   uvicorn app.main:app --reload
   ```

   El servidor debería iniciar y podrás acceder a la API en:

   ```
   http://localhost:8000/docs
   ```

2. **Prueba la API:**

   Utiliza la interfaz de Swagger en `http://localhost:8000/docs` para probar el endpoint `/api/convert` enviando un JSON con el contenido HTML. Por ejemplo:

   ```json
   {
     "html": "<h1>Hola mundo!</h1><p>Esto se va al PDF</p>"
   }
   ```

## 🛠 Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un *issue* o enviar un *pull request*.

## 📝 Licencia

Este proyecto está bajo la licencia MIT.
