FROM python

WORKDIR /usr/src/app

COPY ./app.py .

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
