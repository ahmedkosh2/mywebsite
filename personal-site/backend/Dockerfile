# # backend/Dockerfile
# FROM python:3.12-slim

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# COPY ./requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app/



# FROM python:3.12-slim

# # Install system dependencies for dlib
# RUN apt-get update && apt-get install -y \
#     cmake \
#     g++ \
#     make \
#     libboost-all-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Set working directory
# WORKDIR /app

# COPY ./requirements.txt /app/

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy rest of backend
# COPY . .



FROM python:3.11-slim

# Установим системные зависимости (нужны для dlib, opencv, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libboost-all-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Скопируем requirements отдельно (для кэша)
WORKDIR /app
COPY requirements.txt .

# Установим зависимости (с кешированием wheels)
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем остальной код
COPY . .

CMD ["python", "main.py"]
