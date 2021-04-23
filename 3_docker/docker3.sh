#!/bin/bash

mkdir temp

cp docker3.py temp/.

echo "FROM python" >> temp/Dockerfile

echo "RUN pip install flask" >> temp/Dockerfile

echo "COPY  docker3.py /home/myapp/" >> temp/Dockerfile

echo "EXPOSE 8080" >> temp/Dockerfile

echo "CMD python3 /home/myapp/docker3.py" >> temp/Dockerfile

cd temp
docker build -t docker3 .

docker run -t -d -p 8080:8080 --name kosmosas docker3

docker ps -a
