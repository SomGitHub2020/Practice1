FROM python:3.7-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend/

# Install pip requirements
#ADD requirements.txt .
COPY requirements.txt /app/backend/

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev postgresql-dev
RUN python -m pip install -r requirements.txt

#ADD . /app
COPY . /app/backend/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
#RUN adduser appuser && chown -R appuser /app
RUN adduser -D -g '' admin
USER admin

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:Practice1. Please enter the Python path to wsgi file.
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django-todo-react/backend/backend/wsgi.py"]

