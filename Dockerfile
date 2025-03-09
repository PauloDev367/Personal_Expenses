FROM python:3.8

WORKDIR /app/personalexpenses

RUN apt-get update && apt-get install -y wait-for-it

COPY ./requirements.txt /app/personalexpenses
COPY ./.env /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
