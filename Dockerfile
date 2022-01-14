FROM python:3.8.10

COPY ./requirements.txt /eabykov/requirements.txt
COPY ./easyocr.py /eabykov/easyocr.py
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN python3 -mpip install -r /eabykov/requirements.txt

ENTRYPOINT ["/usr/local/bin/python3", "/eabykov/easyocr.py"]
