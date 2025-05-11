source .env

# TODO: make consistent env forwarding 
echo "REACT_APP_API_URL=${API_URL_CONTAINER}" > ./frontend/.env

docker-compose up --build