#!/bin/bash

mkdir tes

cp jenkins4.py tes/.

echo "FROM python" >> tes/Dockerfile

echo "RUN pip install flask" >> tes/Dockerfile

echo "COPY  jenkins4.py /home/myapp/" >> tes/Dockerfile

echo "EXPOSE 5050" >> tes/Dockerfile

echo "CMD python3 /home/myapp/jenkins4.py" >> tes/Dockerfile

cd tes
docker build -t jenkins4 .

docker run -t -d -p 5050:5050 --name crazy jenkins4

docker ps -a
