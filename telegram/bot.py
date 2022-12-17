import telebot


def bot_message(data):
    botToken = "5902264915:AAGG-fHUI0sZpiO6NRbArXVpjY93tCt2V0Y"
    bot = telebot.TeleBot(botToken)
    chat_id = "245495541"
    return bot.send_message(chat_id=chat_id, text=data)


def send_order_to_telegram(obj, adress, name):
    sold = ""
    check = 0
    for item in obj.items.all():
        cost = item.quantity * item.item.price
        sold += str(item) + "-" + str(cost) + ", "
        check += item.get_final_price()
    # sold += f'. Всього {check}'
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
    message = ""
    ingredients = ()
    for field in form:
        if str(field).split()[-1] == "checked>":
            ingredients += (
                str(field.label_tag().split(">")[1].split("<")[0]).strip(":"),
            )
        elif str(field).split()[1].split('"')[1] == "text":
            message += (
                str(field).strip("<>").split("value=")[1].split("maxlength=")[0] + "*"
            )
        elif str(field).split()[1].split('"')[1] == "message":
            text = str(field).strip("<>").split(">")[1].split("<")[0]
    new_message = [word[1 : len(word) - 2] for word in message.split("*")]
    name, phone, color, wishes = new_message
    bot_message(
        f"""У тебе новий запит на створення композиції: 
{name}
{phone}
Кольорова гама: {color}
Побажання/призначення: {text.lstrip()}
Бажані ігрідієнти: {ingredients}
    """
    )


def send_callback_number_to_telegram(number):
    bot_message(f"На сайті замовили зворотній виклик, передзвони: {number}")


if __name__ == "__main__":
    bot_message("test")
