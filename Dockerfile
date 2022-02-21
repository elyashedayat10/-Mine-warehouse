FROM hub.hamdocker.ir/library/python:3.8
WORKDIR /Madan/
ADD ./requiremrnts.txt ./
RUN pip install -r ./requiremrnts.txt
ADD ./ ./
ENTRYPOINT ["/bin/sh", "-c" , "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 Madan.wsgi"]