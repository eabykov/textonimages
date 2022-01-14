FROM python:3.10.1

COPY ./requirements.txt /eabykov/requirements.txt
COPY ./easyocr.py /eabykov/easyocr.py
RUN /usr/local/bin/python3.8 -m pip install --upgrade pip
RUN python3.8 -mpip install -r /eabykov/requirements.txt

ENTRYPOINT ["/usr/local/bin/python3.8", "/eabykov/easyocr.py"]
