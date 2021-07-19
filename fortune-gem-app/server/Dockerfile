FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install flask requests
EXPOSE 2020
ENTRYPOINT ["python", "app.py"]