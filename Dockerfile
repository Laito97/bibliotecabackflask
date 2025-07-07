# Imagen base ligera con Python 3.8 (compatible con tensorflow-cpu sin AVX)
FROM python:3.8-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la app usando gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]