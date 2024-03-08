FROM python:3.11
WORKDIR /server
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]