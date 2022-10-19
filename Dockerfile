FROM python:3.9

WORKDIR /user/src/educa

COPY ./requirements.txt /user/src/educa/requirements.txt
RUN pip install -r requirements.txt

COPY . /user/src/educa 

EXPOSE 8000

CMD [ "python", "manage.py", "runserver","0.0.0.0:8000"]
