from pytrends.request import *
from pytrends import *

trend = TrendReq(hl="en-US")

last = 0

while True:
    word = input("Word: ")

    trend.build_payload([word], timeframe="today 1-m", cat=0)
    current = trend.interest_over_time()
    mean = current.mean()

    if last != 0:
        if float(mean[word]) > last:
            print("higher")
        else:
            print("lower")

    last = float(mean[word])