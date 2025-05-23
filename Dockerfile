FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app ./app

# Set the FLASK_APP environment variable
ENV FLASK_APP=app

# Expose the port the app runs on
#EXPOSE 5002

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]