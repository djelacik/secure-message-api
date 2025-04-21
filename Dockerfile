FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run Flask with explicit host and port
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
