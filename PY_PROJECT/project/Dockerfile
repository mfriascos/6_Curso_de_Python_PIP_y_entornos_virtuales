FROM python:3.8

WORKDIR /project
COPY requirements.txt /project/requirements.txt

RUN pip install --no-cache-dir --upgrade --force-reinstall -r requirements.txt

COPY ./ /project/

CMD bash -c "while true; do sleep 1; done"
