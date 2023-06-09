# Use a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the desired port
EXPOSE 8080

# Define the command to run the application
CMD [ "python", "app.py" ]
