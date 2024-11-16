FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt . /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

EXPOSE 8000

CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000"]