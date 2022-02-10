FROM python:3.7.12-buster 
ADD app/requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app
CMD ["python", "./fetcher.py"]
