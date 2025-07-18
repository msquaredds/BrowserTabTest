# Use the official Python image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies test
RUN pip install --no-cache-dir -r requirements.txt

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
