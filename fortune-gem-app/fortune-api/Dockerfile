FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install flask
EXPOSE 2020
ENTRYPOINT ["python", "app.py"]