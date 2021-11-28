FROM python:3.9-slim

WORKDIR /app

# copy requirements.txt file
COPY requirements.txt .

# Install app dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Add source code
COPY . .

EXPOSE 3000

# Create user to run the container process.
RUN useradd -M appuser && chmod a+w /app
USER appuser

CMD [ "sh", "-c", "uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 3000" ]
