# python image
FROM python:3.11-alpine

# the working directory inside the container
WORKDIR /cinema

# copie files into the container
COPY . /cinema

# installation of dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add manage.py to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/cinema"

# default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
