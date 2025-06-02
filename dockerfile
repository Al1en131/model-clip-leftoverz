# Gunakan base image Python resmi versi 3.10 slim (ringan)
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Salin file requirements.txt ke container
COPY requirements.txt .

# Install dependencies langsung di global Python environment tanpa virtualenv
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode project ke container
COPY . .

# Expose port yang dipakai Flask (5000)
EXPOSE 5000

# Jalankan app.py saat container dijalankan
CMD ["python", "app.py"]
