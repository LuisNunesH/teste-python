FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY testes/ ./testes/

EXPOSE 5000

CMD ["python", "testes/teste_3.py"]
