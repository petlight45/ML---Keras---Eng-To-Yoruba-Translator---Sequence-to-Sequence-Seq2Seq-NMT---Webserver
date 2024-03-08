import pickle
import numpy as np
from utils.ml.helpers.config import MLHelperConfig
import os
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

MODEL = None


class MLHelperUtils:
    class Pickle:
        @classmethod
        def load_obj_from_file(cls, path):
            with open(path, 'rb') as handle:
                return pickle.load(handle)

    class Tokenizer:
        __slots__ = ['_type', '_tokenizer_obj', "_max_sentence_length"]

        def __init__(self, type: str, max_sentence_length: int):
            self._type: str = type
            self._tokenizer_obj = None
            self._max_sentence_length = max_sentence_length

        @property
        def _tokenizer_file_path(self):
            return os.path.join(MLHelperConfig.RESOURCE_PATH, f"tokenizers/{self._type}_tokenizer.pickle")

        @property
        def tokenizer_obj(self):
            if not self._tokenizer_obj:
                self._tokenizer_obj = MLHelperUtils.Pickle.load_obj_from_file(self._tokenizer_file_path)
            return self._tokenizer_obj

        def _get_word(self, word_index):
            return self.tokenizer_obj.index_word.get(word_index)

        def encode_sequences(self, sequence: np.array):
            seq = self.tokenizer_obj.texts_to_sequences(sequence)
            seq = pad_sequences(seq, maxlen=self._max_sentence_length, padding='post')
            return seq

        def decode_sequences(self, sequence: np.array):
            preds_text = []
            for i in sequence:
                temp = []
                for j in range(len(i)):
                    t = self._get_word(i[j])
                    if j > 0:
                        if (t == self._get_word(i[j - 1])) or (t is None):
                            temp.append('')
                        else:
                            temp.append(t)
                    else:
                        if t is None:
                            temp.append('')
                        else:
                            temp.append(t)
                preds_text.append(' '.join(temp))
            return preds_text

    class Model:
        @classmethod
        def _get_model(cls):
            global MODEL
            if not MODEL:
                MODEL = load_model(os.path.join(MLHelperConfig.RESOURCE_PATH, 'model/model.h1.7_mar_24'))
            return MODEL

        @classmethod
        def load(cls):
            cls._get_model()

        @classmethod
        def predict(cls, encoded_sequence):
            model = cls._get_model()
            return np.argmax(
                model.predict(encoded_sequence.reshape((encoded_sequence.shape[0], encoded_sequence.shape[1]))),
                axis=-1)
