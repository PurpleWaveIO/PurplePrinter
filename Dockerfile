FROM python:3.10.13-slim
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install build-essential libsasl2-dev libldap2-dev libssl-dev -y
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "purpleprinter.py"]
