# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apt-get update && apt-get install -y postgresql-client curl

COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt

RUN pip install -r /app/requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver", "0.0.0.0:9000"]

