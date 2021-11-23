FROM python:3.7

WORKDIR /app


# copy requirements.txt file

COPY ./requirements.txt /app/requirements.txt

# Install app dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Add source code
COPY . /app

EXPOSE 3000

RUN useradd -M appuser
RUN chmod a+w /app
USER appuser

CMD [ "sh", "-c", "uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 3000" ]
