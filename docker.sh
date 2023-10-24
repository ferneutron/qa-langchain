IMAGE_NAME=qa-langchain-image
CONTAINER_NAME=qa-langchain-container
ENV_FILE=.env

docker build --no-cache -t ${IMAGE_NAME} .
docker run --env-file ${ENV_FILE} -it --name ${CONTAINER_NAME} -v $PWD/app/:/app -p 8501:8501 ${IMAGE_NAME}