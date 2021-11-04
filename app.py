# from flask import Flask, request, jsonify
# from flask.logging import create_logger
# import logging
import yfinance as yf
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import bs4 as bs


import pandas as pd
# from sklearn.externals import joblib
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# LOG = create_logger(app)
# LOG.setLevel(logging.INFO)

# def scale(payload):
#     """Scales Payload"""
    
#     LOG.info(f"Scaling Payload: \n{payload}")
#     scaler = StandardScaler().fit(payload.astype(float))
#     scaled_adhoc_predict = scaler.transform(payload.astype(float))
#     return scaled_adhoc_predict

app = FastAPI()

templates = Jinja2Templates(directory="/app/templates")

def get_sp_symbols():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    sp_symbols = []

    for row in table.findAll('tr')[1:]:
        sp_symbol = row.findAll('td')[0].text
        sp_symbols.append(sp_symbol)

    sp500 = list(map(lambda s: s.strip(), sp_symbols))

    return sp500

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.get("/stocks", response_class=HTMLResponse)
def stocks(request: Request):
    symbols = get_sp_symbols()
    return templates.TemplateResponse("stocks.html",{"request": request, "symbols": symbols})
    
# @app.route("/<symbol>")
# def stocks(symbol):
#     # html = f"<h3>Stocks</h3>"
#     data = yf.Ticker(symbol)
#     print(data.info)
#     return data
    
# if __name__ == "__main__":
#     # load pretrained model as clf
#     app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
