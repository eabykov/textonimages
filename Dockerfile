FROM python:3.8-alpine3.15

COPY ./requirements.txt /eabykov/requirements.txt
COPY ./easyocr.py /eabykov/easyocr.py
RUN python3.8 -mpip install -r /eabykov/requirements.txt

ENTRYPOINT ["/usr/local/bin/python3.8", "/eabykov/easyocr.py"]
