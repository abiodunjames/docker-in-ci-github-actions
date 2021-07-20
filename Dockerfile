FROM python:3.7

WORKDIR /app

# install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add source code
COPY . /app

EXPOSE 8000

CMD [ "sh", "-c", "uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000" ]
