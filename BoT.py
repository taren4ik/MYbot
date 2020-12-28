import config
import telebot
import os
from telebot import types


#token = '1460014098:AAE7DNyazA0xwGpKTXdu0iQ0EKXSBeDz5hU'  # bot_rfj
bot = telebot.TeleBot(config.token) 

list_user  = []
@bot.message_handler(func=lambda message: True, content_types=['text'])
    
def get_text_messages(message):

    if message.text == "/start":
        
      
        keyboard = types.InlineKeyboardMarkup() 
        key_yes = types.InlineKeyboardButton(text='YES', callback_data='yes') 
        #keyboard.add(key_yes)
        key_no= types.InlineKeyboardButton(text='No', callback_data='no');
        #keyboard.add(key_no);
        keyboard.row( key_yes, key_no)

        bot.send_message(message.from_user.id, text='Do you have important information?', reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes": 
                bot.send_message(call.message.chat.id, 'Please write your request')
                #keyboard_enter = types.InlineKeyboardMarkup() 
                #key_enter = types.InlineKeyboardButton(text='Enter', callback_data='enter')
                #keyboard_enter.add(key_enter)                              
                    
            elif call.data == "no":
                bot.send_message(call.message.chat.id, 'Thank you for contacting us')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "To get started, write /start")
    else:
       
        bot.send_message(message.from_user.id, 'Thank you for your message')
        bot.send_message(config.owner_id, 'ID:' + str(message.from_user.id) + '\n' + 'NAME: '+ message.from_user.first_name  + '\n'  + 'Information: '+ message.text + '\n') #пересылка сообщения нужному пользователю
        #print(message.from_user.first_name  + '  ' +   '  ' + str(message.from_user.id) +  '  '  + message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)