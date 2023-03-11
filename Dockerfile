FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 3003

COPY . .

CMD [ "python3", "./app.py" ]