import pandas as pd

url = 'https://rate.bot.com.tw/gold?Lang=zh-TW'


def getBotGoldPrice():
    bot_gold = pd.read_html(url)
    df = bot_gold[0]
    bot_sell_price = df['單位：新臺幣元']['1 公克'][0]
    bot_buy_price = df['單位：新臺幣元']['1 公克'][1]

    return bot_sell_price, bot_buy_price