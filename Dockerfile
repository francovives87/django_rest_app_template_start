# Usa la imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias del sistema necesarias para psycopg2, netcat (nc) y otras librerías
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    postgresql-client \
    netcat-openbsd \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Copia el archivo de requisitos al contenedor
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación al contenedor
COPY . /app/

# Establece las variables de entorno para Django
ENV DJANGO_SETTINGS_MODULE=djangoApp.settings.settings

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "djangoApp.wsgi:application"]
