#! python3
import sys,traceback
import requests
import time
import json
import pymysql
import logging
import threading

usdt =['btc', 'bch', 'eth', 'ltc', 'xrp', 'dash', 'etc', 'eos', 'zec', 'omg', 'qtum']
btc = []
eth = []

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %（message)s')

def get_current_price(name):
    mes = None
    try:
        r = requests.get("https://api.huobi.pro/market/detail/merged?symbol=" + name + "usdt")
        if(r.status_code != 200):
            raise Exception("获取数据返回状态异常")
        mes = json.loads(r.text)
        print(mes)
    except Exception as e:
        logging.error(e)
    return mes

def save_data(db, data):
    if(type(data) != dict):
        logging.error("参数数据结构错误,终止数据处理，开始处理其他渠道")
        return
    try:
        cursor = db.cursor()
        param = data['status'],data['ch'],data['ts'],data['tick']['amount'],data['tick']['open'],data['tick']['close'],data['tick']['high'],data['tick']['id'],data['tick']['count'],data['tick']['low'],data['tick']['version'],data['tick']['ask'][0],data['tick']['ask'][1],data['tick']['vol'],data['tick']['bid'][0],data['tick']['bid'][1]
        sql = "insert into coin.c_e_usdt_detail(status,ch,ts,amount,open,close,high,id,count,low,version,askprice,askamount,vol,bidprice,bidamount) values"+str(param)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        logging.error(e)
        db.rollback()

def singlework(coin_name, db):
    current = get_current_price(coin_name)
    save_data(db, current)
    return db
    
        
def threadwork(coin_name, db):
    thread = threading.Thread(target=singlework, args=(coin_name, db))
    print("-" * 20  + thread.getName() + "-" * 20)
    thread.start()
    
    
if __name__ == "__main__":
    usdtdic = {}
    for coin_name in usdt:
        usdtdic[coin_name] = pymysql.connect("localhost","root","123456","coin")
        print("创建" + coin_name + "的数据库连接")

    while True:
        for coin_name in usdtdic:
            db = usdtdic[coin_name] 
            threadwork(coin_name, db)
        time.sleep(5)

    for coin_name in usdt:
        db = usdtdic[coin_name];
        db.close()
