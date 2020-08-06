from datetime import datetime
from ratebot import gold_rate
from ratebot.slack_message import SlackMessage

dt_now = datetime.now()
dt_str = dt_now.strftime("%Y-%m-%d %H:%M")

gold_sell, gold_buy = gold_rate.getBotGoldPrice()

text = f'------\n⏰ {dt_str}\n台銀買進價格：{gold_buy:,}\n台銀賣出價格：{gold_sell:,}\n------'

slack = SlackMessage()
slack.send_message(text)