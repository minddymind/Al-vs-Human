docker build -t predict-app .

docker run -p 5555:5555 predict-app
