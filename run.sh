source .env

# TODO: make consistent env forwarding 
echo "REACT_APP_API_URL=${API_URL}" > ./frontend/.env

docker-compose up --build