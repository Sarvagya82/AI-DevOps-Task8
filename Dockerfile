FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY iris_model.joblib /app
COPY app.py /app

EXPOSE 80

CMD ["python", "app.py"]
