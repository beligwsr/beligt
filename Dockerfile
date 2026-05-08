FROM python:3.11
WORKDIR /belig
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "my_shop.wsgi:application", "--bind", "0.0.0.0:8000"]
