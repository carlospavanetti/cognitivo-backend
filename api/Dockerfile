FROM python:3.6-alpine

WORKDIR /app

# Boa prática das imagens docker: cachear uma layer de dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD gunicorn --bind=0.0.0.0:5000 server:app