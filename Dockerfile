FROM python:3.10


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]

# In case you are running your container behind a TLS Termination Proxy (load balancer)
# CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]