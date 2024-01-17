FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir /backend

COPY requirements.txt /backend

WORKDIR /backend

RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
