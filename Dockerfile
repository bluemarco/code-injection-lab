FROM python:3.9.6

COPY main.py .

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]