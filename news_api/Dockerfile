FROM python:3.9

RUN mkdir /api

WORKDIR /api

COPY . /api

RUN python -m venv env

RUN chmod 777 env/bin/activate

RUN env/bin/activate

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

#RUN python news_api/manage.py migrate
