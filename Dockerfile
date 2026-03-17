# 1. Use an official, lightweight Python image as our base operating system
FROM python:3.9-slim

# 2. Set the working directory inside our container to /app
WORKDIR /app

# 3. Copy our requirements file into the container
COPY requirements.txt .

# 4. Install the required Python libraries inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy our actual Python script into the container
COPY monitor.py .

# 6. Tell the container what command to run when it starts up
CMD ["python", "monitor.py"]