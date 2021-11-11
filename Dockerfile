FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt
#pip install --upgrade pip

## Step 2:
# Copy source code to working directory
COPY . app.py /app/

## Step 4:
# Expose port 80

EXPOSE 80

## Step 5:
# Run app.py at container launch

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]