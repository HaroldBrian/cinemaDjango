# python image
FROM python:3.11

# the working directory inside the container
WORKDIR /app

# copie files into the container
COPY . /app

# installation of dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add manage.py to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
