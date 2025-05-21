# Use an official Python runtime as a parent image
# Using a "slim" version to keep the image size smaller
FROM python:3.11-slim

# Set the working directory in the container
# All subsequent commands (COPY, RUN, CMD, etc.) will be relative to this directory
WORKDIR /app

# Copy the requirements file into the container at the current working directory (/app)
COPY requirements.txt .

# Install Python dependencies specified in requirements.txt using pip
# Using --no-cache-dir is a good practice to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot script into the container at the current working directory (/app)
COPY bot.py .

# Make the bot script executable
# While the bot is run with "python bot.py", making it executable is a good practice
RUN chmod +x bot.py

# Set the command to run the application when the container starts
# This will execute "python bot.py"
CMD ["python", "bot.py"]
