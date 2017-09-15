# Simple Flask API for a Tensorflow Model

## Intro
To be hosted on Heroku (files `Procfile`, `requirements.txt` and `runtime.txt`).

To run locally,

```
python app.py
```

The model is from another repo (`sequence_tagging`) on my github and is in the `model` folder. The flask app is defined in `app.py` which contains generic logic. The model-specific logic for the API is in the `serve.py` file.

## Other Resources

- MNIST: https://github.com/sugyan/tensorflow-mnist/blob/master/main.py
- gCloud flexible: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/flexible/hello_world/main.py
- Flask: http://flask.pocoo.org/docs/0.12/quickstart/
- Floyd: https://github.com/floydhub/fast-style-transfer/blob/master/app.py

