#!/bin/bash

mkdir tes

cp tes.py tes/.

echo "FROM python" >> tes/Dockerfile

echo "RUN pip install flask" >> tes/Dockerfile

echo "COPY  tes.py /home/myapp/" >> tes/Dockerfile

echo "EXPOSE 5050" >> tes/Dockerfile

echo "CMD python3 /home/myapp/tes.py" >> tes/Dockerfile

cd tes
docker build -t tests .

docker run -t -d -p 5050:5050 --name kosmosas tests

docker ps -a
