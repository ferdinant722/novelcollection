# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run manage.py commands
RUN python manage.py collectstatic --noinput

# Run gunicorn server
CMD ["gunicorn", "novelcollection.wsgi", "--bind", "0.0.0.0:8000"]

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run manage.py commands
RUN python manage.py collectstatic --noinput

# Run gunicorn server
CMD ["gunicorn", "novelcollection.wsgi", "--bind", "0.0.0.0:8000"]
