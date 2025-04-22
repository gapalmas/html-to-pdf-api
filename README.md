# Proyecto HTML a PDF

Este proyecto es una API con FastAPI que recibe el contenido HTML y lo convierte a un PDF en formato base64.

## 🐳 Usar con Docker

También puedes ejecutar el API desde la imagen de Docker disponible en Docker Hub.

### 🔽 Descargar y ejecutar

```bash
docker pull gapalmasss/html_to_pdf:latest
docker run -d -p 8000:8000 gapalmasss/html_to_pdf:latest
```

## 🛠 Requisitos

Asegúrate de tener instalado lo siguiente en tu sistema:

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Chocolatey (para instalar `wkhtmltopdf` en Windows)

## 🚀 Instalación

1. **Clona el repositorio:**

   Abre tu terminal y ejecuta:

   ```bash
   git clone https://github.com/gapalmas/html_to_pdf.git
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
## 🧪 Análisis de Seguridad con CodeQL

Este repositorio incluye un análisis automatizado de seguridad utilizando **GitHub CodeQL**, que ayuda a detectar vulnerabilidades comunes en el código.

### 🔍 ¿Cómo ver los resultados?

1. Ve a la página principal del repositorio en GitHub.
2. Haz clic en la pestaña **Security**.
3. Luego selecciona **Code scanning alerts**.
4. Ahí verás una lista de alertas detectadas por CodeQL (si las hay).

> 💡 Si no ves la pestaña `Security`, haz clic en los tres puntos `...` en el menú superior para desplegar más opciones.

### 📜 Ver historial de ejecuciones

1. Abre la pestaña **Actions** del repositorio.
2. Busca el flujo llamado **CodeQL Analysis**.
3. Haz clic sobre una ejecución específica para ver los pasos detallados y los resultados del análisis.


## 🛡️ Escaneo de Vulnerabilidades con Trivy

Este repositorio utiliza [**Trivy**](https://trivy.dev/) para escanear automáticamente la imagen Docker en busca de vulnerabilidades de seguridad en cada `push` o `pull request` a la rama `main`.

### 🔍 ¿Cómo ver los resultados?

1. Ve a la pestaña **Security** en la página principal del repositorio.
2. Haz clic en **Code scanning alerts**.
3. Revisa las alertas generadas por Trivy, que se integran con GitHub Code Scanning.

> 💡 Si no ves la pestaña `Security`, haz clic en los tres puntos `...` en el menú superior para desplegar más opciones.

### 🧪 Ver historial de ejecuciones

1. Abre la pestaña **Actions** del repositorio.
2. Busca el flujo llamado **Trivy Docker Image Scan**.
3. Haz clic en una ejecución específica para ver los pasos detallados y los resultados del análisis.

### 🧰 ¿Qué analiza Trivy?

Trivy escanea la imagen Docker en busca de:

- Vulnerabilidades en paquetes del sistema operativo.
- Problemas en dependencias de aplicaciones.
- Configuraciones inseguras.

Para más información sobre Trivy y sus capacidades, visita la [documentación oficial](https://trivy.dev/).


## 🛠 Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un *issue* o enviar un *pull request*.

## 📝 Licencia

Este proyecto está bajo la licencia MIT.
