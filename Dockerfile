FROM python:3.9

RUN pip3.9 install fastapi uvicorn

EXPOSE 80

COPY ./example_rest /example_rest

CMD ["uvicorn", "example_rest.__main__:app", "--host", "0.0.0.0", "--port", "80"]

