import telebot
from bs4 import BeautifulSoup
from . import config


def bot_message(data):
    botToken = config.botToken
    bot = telebot.TeleBot(botToken)
    chat_id = config.chat_id
    
    return bot.send_message(chat_id=chat_id, text=data)


def send_order_to_telegram(obj, adress, name):
    sold = ""
    check = 0
    
    for item in obj.items.all():
        cost = item.quantity * item.item.price
        sold += str(item) + "-" + str(cost) + ", "
        check += item.get_final_price()
        
    pay = "готівкою" if adress.payment_option == "C" else "на картку"
    
    bot_message(
        f"""
У тебе нове замовлення: 
{adress.zip} 
{name.first_name} 
оплата {pay}: 
{sold}
Всього: {check}
    """
    )


def send_composition_to_telegram(form):
    with open("message.txt", "w+", encoding="UTF-8") as outf:
        outf.write(str(form))
        outf.seek(0)

        params = []
        ingredients = ()

        for line in outf:
            soup = BeautifulSoup(line, "lxml")
            if soup.label:
                name = soup.label.string[:-1]
            if soup.input:
                if soup.input.get("type") == "checkbox":
                    if soup.input.get("checked") == "":
                        ingredients += (name,)
                elif soup.input.get("type") == "text":
                    params.append((name, soup.input.get("value")))

        outf.seek(0)

        hit = BeautifulSoup(outf, "lxml")
        message = hit.find(attrs={"id": "id_message"}).contents

    bot_message(
        f""" У тебе новий запит на створення композиції: 
{params[0][0]}:  {params[0][1]}
{params[1][0]}:  {params[1][1]}
{params[2][0]}:  {params[2][1]}
Бажані складові:  {ingredients}
Побажання/призначення: {message[0].strip()}"""
    )


def send_callback_number_to_telegram(number):
    bot_message(f"На сайті замовили зворотній виклик, передзвони: {number}")


if __name__ == "__main__":
    bot_message("test")
