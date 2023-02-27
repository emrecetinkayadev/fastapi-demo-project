FROM python:3.9.6

WORKDIR /app
# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# copy project
COPY . /app/