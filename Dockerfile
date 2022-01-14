FROM bitnami/pytorch:1.10.1

COPY ./requirements.txt /eabykov/requirements.txt
COPY ./easyocr.py /eabykov/easyocr.py
RUN python -m pip install --upgrade pip
RUN python -mpip install -r /eabykov/requirements.txt

CMD ["python", "/eabykov/easyocr.py"]
