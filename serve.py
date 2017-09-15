from model.ner_model import NERModel
from model.config import Config


def align_data(data):
    """Given dict with lists, creates aligned strings

    Adapted from Assignment 3 of CS224N

    Args:
        data: (dict) data["x"] = ["I", "love", "you"]
              (dict) data["y"] = ["O", "O", "O"]

    Returns:
        data_aligned: (dict) data_align["x"] = "I love you"
                           data_align["y"] = "O O    O  "

    """
    spacings = [max([len(seq[i]) for seq in data.values()])
                for i in range(len(data[list(data.keys())[0]]))]
    data_aligned = dict()

    # for each entry, create aligned string
    for key, seq in data.items():
        str_aligned = ""
        for token, spacing in zip(seq, spacings):
            str_aligned += token + " " * (spacing - len(token) + 1)

        data_aligned[key] = str_aligned

    return data_aligned


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
        punc = [",", "?", ".", ":", ";", "!", "(", ")", "[", "]"]
        s = "".join(c for c in input_data if c not in punc)
        words_raw = s.strip().split(" ")

        # 3. call model predict function
        preds = model.predict(words_raw)

        # 4. process the output
        output_data = align_data({"input": words_raw, "output": preds})

        # 5. return the output for the api
        return output_data

    return model_api
