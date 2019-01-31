FROM python:3.7.2-stretch

WORKDIR /usr/src/app

COPY req.txt ./
RUN  pip install --no-cache-dir -r req.txt

CMD ["python","-m","flask","run","--host=0.0.0.0"]
