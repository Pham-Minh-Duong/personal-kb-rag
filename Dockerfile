# 1. Sử dụng Python 3.10 mỏng nhẹ làm base image
FROM python:3.10-slim

# 2. Thiết lập thư mục làm việc trong container
WORKDIR /app

# 3. Cài đặt các công cụ hệ thống cần thiết (nếu có)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy file requirements.txt và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ code nguồn và dữ liệu vào container
COPY . .

# 6. Mở cổng 8000 cho FastAPI
EXPOSE 8000

# 7. Lệnh khởi chạy ứng dụng FastAPI khi container xuất phát
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]