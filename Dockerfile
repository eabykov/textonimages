FROM python:3.8-slim-buster

RUN pip install easyocr==1.4.1 thefuzz[speedup]==0.19.0
COPY ./easyocr.py /easyocr.py

CMD ["python", "easyocr.py"]
