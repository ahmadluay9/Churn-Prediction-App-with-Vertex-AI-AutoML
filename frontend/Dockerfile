FROM python:3.9

RUN mkdir /frontend

COPY requirements.txt /frontend

WORKDIR /frontend

RUN pip install --no-cache-dir -r requirements.txt

COPY . /frontend

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
