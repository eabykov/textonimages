FROM python:3.8

RUN python3.8 -mpip install easyocr==1.4.1 thefuzz[speedup]==0.19.0
COPY ./easyocr.py /easyocr.py

CMD ["python", "/easyocr.py"]
