import pickle
# Current model
import numpy as np

class MultinomialNB:
    def __init__(self):
        self.classes = None
        self.priors = None
        self.likelihoods = None

    def fit(self, X, y):
        self.classes = np.unique(y)
        # Count the occurrences of each class
        class_counts = np.array([np.sum(y == c) for c in self.classes])
        # Compute the priors
        self.priors = class_counts / len(y)
        # Count the occurrences of each word in each class
        word_counts = [np.array([np.sum(np.array(X)[y == c], axis=0) for c in self.classes])]
        # Compute the likelihoods
        print('word count is ' ,  np.sum(word_counts, axis=1, keepdims=True))
        self.likelihoods = word_counts + np.sum(word_counts, axis=1, keepdims=True)

    def predict(self, X):
        # Compute the log-likelihoods
        log_likelihoods = np.log(self.likelihoods)
        # Compute the log-priors
        log_priors = np.log(self.priors)
        # Compute the log-posteriors
        log_posteriors = log_likelihoods + log_priors
        # Find the class with the highest log-posterior
        predictions = self.classes[np.argmax(log_posteriors, axis=1)]
        return predictions

class CountVectorizers:
    def __init__(self):
        self.vocab = None

    def fit(self, text_docs):
        # Create a dictionary of unique tokens
        self.vocab = set([token for doc in text_docs for token in doc.split()])
        self.vocab = list(self.vocab)

    def transform(self, text_docs):
        # Create an empty matrix with the same number of rows as the number of documents and the same number of columns as the number of unique tokens
        # print('vocab is ' , self.vocab)
        token_counts = pd.DataFrame(0, index=range(len(text_docs)), columns=self.vocab)
        # print('token Counts is ' , token_counts)

        # Iterate through each document and token, and increment the corresponding cell in the matrix
        for i, doc in enumerate(text_docs):
            for token in doc.split():
                if token in self.vocab:
                    token_counts.at[i, token] += 1
        return token_counts


class C:
  def __init__(self , message ):
    self.message = message 
    self.obj = dict()
    self.model = None
  
  
  def train(self):
    signal = """
    ⚡️⚡️#OCEAN/USDT⚡️⚡️
    Signal Type: Long
    Leverage: Cross 20x
    Entry Targets: 0.2451 0.2350
    Take-Profit Targets: 
    1) 0.2465
    2) 0.2477
    3) 0.2489
    4) 0.2510
    5) 0.2535
    6) 0.2560
    7) 0.2585
    8) 0.2610

    Stop-Loss: 
    0.2250🚀🚀
    """

    entry_target = """
    Binance Futures, ByBit USDT
    #DYDX/USDT Entry target 1 ✅
    Average Entry Price: 1.361 💵

    """


    take_profit = """
    Binance Futures
    #OCEAN/USDT Take-Profit target 1 ✅
    Profit: 11.4239% 📈
    Period: 7 Minutes ⏰
    """
    vectorizer = CountVectorizers()
    text_data = [signal, entry_target, take_profit]
    labels = ["signal", "entry_target", "take_profit"]
    
    try:
      X = vectorizer.fit(text_data)
      X = vectorizer.transform(text_data)
      print("Fitted to vector properly")
      
      
      clf = MultinomialNB()
      clf.fit(X, labels)
      # print("Finished fitting....")
      new_text_vectorized = vectorizer.transform([self.message])
      # clf = joblib.load('xavier.pkl')
      # with open('xavier.pkl' , 'rb') as f:
      #   clf = pickle.load(f)
      
      predicted_label = clf.predict(new_text_vectorized)[0]
      print("pr " , predicted_label)
      # self.obj['message_type'] = predicted_label
      return vectorizer
    except Exception as e:
      return e

    
  def predict(self):
    return self.train()
    # return predicted_label
   

  def signal_classification(self):
    line_by = [single  for single in self.message.split('\n') if len(single) > 1]
    output = dict()
    output['message_type'] = 'Signal'
    # Signal Values
    output['coin'] = clean([s for s in line_by if "#" in s][0], no_emoji=True).replace('#','')
    output['signal_type'] = [s for s in line_by if "Signal" in s][0].replace('Signal Type: ' , '')
    output['leverage'] = [s for s in line_by if "Leverage" in s][0].replace('Leverage: ' , '')
    output['entry_target'] = [s for s in line_by if "Entry" in s][0].replace('Entry Targets: ' , '').split(' ')
    # output['take_profit_targets(with numbers)'] =  [line for  line in line_by if len(line) == 9]
    output['take_profit_targets'] =  [re.sub(r"\s*\d+\)\s*", "", line) for  line in line_by if len(line) == 9]

    # STOP LOSS
    stop_loss_index = line_by.index([s for s in line_by if "Stop-Loss" in s][0])
    output['stop_loss'] = clean(line_by[stop_loss_index+1],no_emoji=True)

    return output

  def entry_target_classification(self):
    output = dict()
    line_by = [m for m in self.message.split('\n') if len(m) > 1]
    output['message_type'] = 'Entry Target'
    output['coin'] = clean([s for s in line_by if "#" in s][0], no_emoji=True).replace('#','').split(' ')[0]
    output['entry_target'] = clean([s for s in line_by if "#" in s][0].replace('Entry target' , ''), no_emoji=True).replace('#','').replace(output['coin'] , '').replace(' ' , '')
    output['average_entry_price'] = clean([s for s in line_by if "Entry Price" in s][0], no_emoji=True).replace('Average Entry Price: '.lower() , '')
    return output
  def take_profit_classification(self):
    output = dict()
    line_by = [m for m in self.message.split('\n') if len(m) > 1]
    output['message_type'] = 'Take Profit'
    output['coin'] = clean([s for s in line_by if "#" in s][0], no_emoji=True).replace('#','').split(' ')[0]


    output['target'] = clean([s for s in line_by if "#" in s][0].replace('Take-Profit target' , ''), no_emoji=True).replace('#','').replace(output['coin'] , '').replace(' ' , '')
    output['profit'] = clean([s for s in line_by if "Profit" in s][1], no_emoji=True).replace('profit: ' ,'')
    output['period(minutes)'] = clean([s for s in line_by if "Period" in s][0], no_emoji=True).replace('period: ' ,'').replace(' minutes' , '')

    return output



  def output(self):
    message_type = self.predict()
    # if(message_type == 'signal'):
    #   return self.signal_classification()
    # elif(message_type == 'entry_target') :
    #   return self.entry_target_classification()
    # elif(message_type == 'take_profit') :
    #   return self.take_profit_classification()
    # else:
    return message_type

import pandas as pd


# Instantiate the class
# count_vec = CountVectorizers()

# # Fit the vectorizer on a set of text documents
# text_docs = ["This is the first document.", "This is the second document.", "And this is the third one."]
# count_vec.fit(text_docs)

# # Create the matrix of token counts
# token_counts = count_vec.transform(text_docs)

# print(token_counts)


