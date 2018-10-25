 FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 ENV PYTHONPATH=/usr/local/lib/python3.6/site-packages/:/code/
