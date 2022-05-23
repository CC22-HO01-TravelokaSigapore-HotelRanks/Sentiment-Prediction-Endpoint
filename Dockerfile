FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install unzip

RUN pip install gdown

# Replace this with the model version google drive ids
# The file is in the folder model/{version}/saved_model.zip
RUN gdown 1-3kRd02jJ8-E1RkY158Wusg4lsdJDgUV

RUN unzip saved_model.zip

RUN rm saved_model.zip

RUN pip install -r requirements.txt

ENV HOST 0.0.0.0

EXPOSE 8001

CMD ["python", "main.py"]