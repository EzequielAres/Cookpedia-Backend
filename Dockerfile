FROM python:3

RUN apt -qq -y update \
    && apt -qq -y upgrade

ADD . /FlaskRecetas
WORKDIR /FlaskRecetas

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]