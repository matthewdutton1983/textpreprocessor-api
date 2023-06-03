# Use an official Python 3.9.7 runtime as a parent time
FROM python:3.9.7-slim-buster

# Set the working directory in the container to /src
WORKDIR /src

# Add the current directory contents into the container at /src
ADD . /src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mark port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
