The project was built using a Sequence-to-Sequence (Seq2Seq) neural machine translation (NMT) model using the Keras library with a focus on translating English sentences to Yoruba. Here's a high-level explanation of the code:
Data Preprocessing:
The code starts by importing necessary libraries and setting up some utility functions for saving and loading objects, reading text files, and splitting sentences.
Raw text data is read from an English-Yoruba text file and processed to create an array of sentence pairs.

Text Cleaning:
Punctuation is removed from both English and Yoruba sentences, and all text is converted to lowercase.


Exploratory Data Analysis (EDA):
Sentence lengths for both English and Yoruba are visualized using histograms to understand the distribution of sentence lengths in the dataset.


Tokenization:
The sentences are tokenized using the Keras Tokenizer class, which converts the sentences into sequences of integers. Separate tokenizers are created for English and Yoruba.


Model Building:
The Seq2Seq model architecture is defined, comprising an Embedding layer and an LSTM layer as the encoder, and another LSTM layer followed by a Dense layer as the decoder.
RMSprop optimizer is used, and the model is compiled with 'sparse_categorical_crossentropy' as the loss function.
The training data is split into training and validation sets.


Model Training:
The model is trained for 30 epochs with a batch size of 45. ModelCheckpoint is used to save the best model based on validation loss, and EarlyStopping is employed to stop training if the validation loss doesn't improve.
Tokenizers and Model Saving:
The trained tokenizers for English and Yoruba are saved to files, and the trained model is saved as well.


Making Predictions:
The saved model is loaded, and predictions are made on the test set.
The predictions are converted back to Yoruba text using the Yoruba tokenizer.

User Testing:
The user is prompted to input an English sentence for translation.
The input sentence is tokenized and fed into the trained model to generate the corresponding Yoruba translation.
The result is displayed to the user.