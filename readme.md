# Purpose
I developed this program to classify Telegram Crypto signals and extract values from Telegram messages.

# Signal Classification and Entity Extraction

This repository contains code for a Signal Classification and Entity Extraction system. It utilizes the scikit-learn library's Multinomial Naive Bayes model for classifying the type of signal and extracting entities from a given message.

## Model Implementation

The main code consists of the following classes:

### MultinomialNB
- `fit(X, y)`: Fits the Multinomial Naive Bayes model to the given features `X` and labels `y`.
- `predict(X)`: Predicts the class labels for the given features `X`.

### CountVectorizers
- `fit(text_docs)`: Fits the CountVectorizer on a set of text documents.
- `transform(text_docs)`: Transforms the text documents into token count matrices.

### C
- `train()`: Trains the Multinomial Naive Bayes model on the provided data.
- `predict()`: Predicts the message type using the trained model.
- `signal_classification()`: Extracts signal-related information from the message.
- `entry_target_classification()`: Extracts entry target-related information from the message.
- `take_profit_classification()`: Extracts take profit-related information from the message.
- `output()`: Returns the extracted information from the message.

## Usage

1. Set up the required dependencies and ensure the scikit-learn library is installed.
2. Import the necessary modules and classes from the code.
3. Prepare the data and instantiate the necessary classes.
4. Train the model using the provided data.
5. Use the model to predict the message type and extract relevant information.

Feel free to explore and adapt this code to your specific use case!

