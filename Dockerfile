FROM python:3.9.6

COPY main.py .

ENV MAGIC_NUMBER=1337

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]