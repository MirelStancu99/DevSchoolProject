# Setam imaginea de baza pe Python 3.9
FROM python:3.9

# Se seteaza directorul de lucru la /app
WORKDIR /app

# Copiem fișierele necesare în container
COPY requirements.txt .
COPY app.py .

# Instalam pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

# Dezvăluim portul 80 pe care rulează aplicația
EXPOSE 80

# Definim comanda care va rula aplicația
CMD ["python", "app.py"]