FROM python:3.7-alpine
WORKDIR /hello_world

ENV FLASK_APP=hello_world/app.py
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

# ENTRYPOINT [ "python" ]
# CMD ["hello_world/app.py" ]