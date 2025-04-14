# 使用官方 Python 映像作為基底
FROM python:3.10

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製你的 API 程式碼
COPY . .

# 啟動 API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
