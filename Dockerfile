FROM python:3.9-slim-buster

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install dependencies
RUN apt-get update && apt-get install -y postgresql-11 gcc python3-dev

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements/requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
