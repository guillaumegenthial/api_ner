import string


from model.ner_model import NERModel
from model.config import Config
from evaluate import align_data


def get_model_api():
    """Returns lambda function for api"""

    # 1. initialize model once and for all
    config = Config()
    model  = NERModel(config)
    model.build()
    model.restore_session("results/crf/model.weights/")


    def model_api(input_data):
        """
        Args:
            input_data: submitted to the API, raw string

        Returns:
            output_data: after some transformation, to be
                returned to the API

        """
        # 2. process input
        s = input_data.translate(string.maketrans("",""), string.punctuation)
        words_raw = s.strip().split(" ")

        # 3. call model predict function
        preds = model.predict(words_raw)

        # 4. process the output
        output_data = align_data({"input": words_raw, "output": preds})

        # 5. return the output for the api
        return output_data

    return model_api
