FROM python:3.7.12-buster 
ADD app/requirements.recv.txt /
RUN pip install -r /requirements.recv.txt
WORKDIR /app
CMD ["uvicorn", "recv:app", "--reload", "--port", "3000", "--host", "0.0.0.0"]
