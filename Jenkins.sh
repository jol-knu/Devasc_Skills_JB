#!/bin/bash

mkdir test

cp Jenkins.py test/.

echo "FROM python" >> test/Dockerfile

echo "RUN pip install flask" >> test/Dockerfile

echo "COPY  Jenkins.py /home/myapp/" >> test/Dockerfile

echo "EXPOSE 5050" >> test/Dockerfile

echo "CMD python3 /home/myapp/Jenkins.py" >> test/Dockerfile

cd test

docker build -t jenkinsr .

docker run -t -d -p 5050:5050 --name rasa jenkinsr

docker ps -a