# Simple Flask API for a Tensorflow Model

See the [blog post](https://guillaumegenthial.github.io/serving.html) covering the main steps.

To be hosted on Heroku (files `Procfile`, `requirements.txt` and `runtime.txt`).

To run locally,

```
python app.py
```

The model is from [another repo](https://github.com/guillaumegenthial/sequence_tagging) on my github and is in the `model` directory. The flask app is defined in `app.py` which contains generic logic. The model-specific logic for the API is in the `serve.py` file.

An example of client is in the `client` directory.
