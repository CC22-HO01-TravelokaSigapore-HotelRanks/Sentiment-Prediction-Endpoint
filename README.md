# Sentiment Prediction Endpoint

This is only an endpoint for one of the pipeline to optimize Hotel Ranking.  

| Information  | Value                                  |
|--------------|----------------------------------------|
| Docker Image | kaenova/traveloka-sentiment-prediction |
|   Port Open  |                  8001                  |


| Endpoint | Method |           Body Sent (JSON)          |                 Description                |
|:--------:|:------:|:-----------------------------------:|:------------------------------------------:|
|     /    |   GET  |                 None                |            Hello World Endpoint            |
|     /    |  POST  | {"text" : ["example1", "example2"]} | Sentiment Prediction from Pretrained Model |

Checkout all our pre-trained model through this [link](https://drive.google.com/drive/folders/1A7N_McAxnxrThlDyArJXr0_k-nHPDfiI).  

CC22-HO01 ML Teams.
