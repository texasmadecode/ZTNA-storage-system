# 1. Use an official, minimal Python environment as our base image
FROM python:3.12-slim

# 2. Set an isolated directory inside the container for our application
WORKDIR /app

# 3. Copy our security package and main script from your Mac into the container
COPY security_system/ ./security_system/
COPY main.py .

# 4. Tell Docker to execute your script the moment the container fires up
CMD ["python", "main.py"]
