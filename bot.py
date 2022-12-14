import telebot

def bot_message(data):
    botToken = '5902264915:AAGG-fHUI0sZpiO6NRbArXVpjY93tCt2V0Y'
    bot = telebot.TeleBot(botToken)
    chat_id ='245495541'
    return bot.send_message(chat_id=chat_id, text=data)

def send_message_to_telegram(obj, adress, name):
    sold = ''
    check = 0
    for item in obj.items.all():
        cost = item.quantity * item.item.price
        sold += str(item) + '-' + str(cost) + ', '
        check += item.get_final_price()
    sold += f'. Всього {check}'
    pay = 'готівкою' if adress == 'C' else 'на картку'
    bot_message(f'{adress.zip}, {name.first_name}, оплата {pay}: {sold}')


if __name__ == "__main__":
    bot_message("test")