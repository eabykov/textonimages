FROM python:3.8

COPY ./easyocr.py /easyocr.py
RUN python3.8 -mpip install easyocr==1.4.1 thefuzz[speedup]==0.19.0

CMD ["python", "/easyocr.py"]
