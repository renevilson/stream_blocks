FROM python:3.7-slim


ENV PYTHONPATH = $PWD

RUN apt update -y && apt upgrade -y && pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD ["python", "src/init_db.py" ]
CMD ["python", "src/server.py" ]

