FROM python:3.11-bullseye

# Set environment variable to ensure Python outputs everything to the console
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install gettext -y

# Create and set the working directory
WORKDIR /code

# Copy and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /code/

# Expose the port Django will run on
EXPOSE 8000

# Run the Django application
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]