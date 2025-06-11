# Use official Python image as base
FROM  python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file if exists
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 5000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Run the application (update as needed, e.g., app.py or main.py)
CMD ["python", "app.py"]