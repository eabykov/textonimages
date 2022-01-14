FROM python:3.8

RUN mkdir -p /eabykov
WORKDIR /eabykov

COPY ./requirements.txt /eabykov/requirements.txt
COPY ./easyocr.py /eabykov/easyocr.py
RUN chmod +x /eabykov/easyocr.py \
    && python3.8 -mpip install -r requirements.txt

CMD ["/bin/sh", "-c", "python3.8", "/eabykov/easyocr.py"]
