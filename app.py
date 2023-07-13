from flask import Flask
import re
from datetime import datetime
from model import CountVectorizers , C
from flask import Flask
import joblib
app = Flask(__name__)


message = """
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
import pickle
take_profit = """
Binance Futures
#OCEAN/USDT Take-Profit target 1 ✅
Profit: 11.4239% 📈
Period: 7 Minutes ⏰
"""
@app.route("/")
def home():
    # c.fit(text_data)
    # cc = c.transform(message)
    # clf = joblib.load('Xavi89.sav')
    # pickled_model = pickle.load(open('Xavi89.sav', 'rb'))
    
    # print(clf.predict(cc)[0])
    out = C(take_profit).output()
    print('out is ' , out)
    return f"Loaded succusfully and"

if __name__ == '__main__':
    app.run(debug=True)