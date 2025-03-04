FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Default command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]