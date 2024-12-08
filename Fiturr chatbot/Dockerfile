# Gunakan image dasar Python
FROM python:3.8

# Buka port 8080
EXPOSE 8080

# Tetapkan direktori kerja
WORKDIR /app

# Salin hanya file yang relevan
COPY requirements.txt ./
COPY main.py ./
COPY templates/ ./templates
COPY capstone-bangkit-2024-f2b8abb656f8.json ./ 
COPY capstone-bangkit-2024-8a348fce7975.json ./ 
 # Salin file JSON kredensial

# Install dependencies
RUN pip install -r requirements.txt

# Jalankan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

