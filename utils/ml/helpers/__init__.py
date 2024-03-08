from utils.ml.helpers.config import MLHelperConfig
from utils.ml.helpers.utils import MLHelperUtils
import numpy as np


class MLHelper:
    @classmethod
    def translate(cls, word: str):
        eng_tokenizer_instance = MLHelperUtils.Tokenizer(type=MLHelperConfig.TokenizerType.ENGLISH,
                                                         max_sentence_length=MLHelperConfig.MaxSentenceCount.ENGLISH)
        yor_tokenizer_instance = MLHelperUtils.Tokenizer(type=MLHelperConfig.TokenizerType.YORUBA,
                                                         max_sentence_length=MLHelperConfig.MaxSentenceCount.YORUBA)
        encoded_sequence = eng_tokenizer_instance.encode_sequences(np.array([word]))
        prediction_sequence = MLHelperUtils.Model.predict(encoded_sequence)
        decoded_prediction = yor_tokenizer_instance.decode_sequences(prediction_sequence)
        if decoded_prediction:
            return decoded_prediction[0].strip()
