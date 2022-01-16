FROM python:3.8

RUN pip install easyocr==1.4.1 thefuzz[speedup]==0.19.0
COPY ./easyocr.py /textonimages/easyocr.py

WORKDIR /textonimages
CMD ["python", "easyocr.py"]
