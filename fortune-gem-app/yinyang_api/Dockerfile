FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 2020
ENTRYPOINT ["python", "app.py"]