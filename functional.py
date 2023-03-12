import telebot
import funcFiles as funcF

from telebot import types
bot = telebot.TeleBot('5943870215:AAFnHMEvoRCrBMqt0wDLlaP0s8tNtErhKF0')
typeOfFunc = 0
iter = 0
index = 0

@bot.message_handler(commands=['start'])
def start(message):
    global typeOfFunc, iter
    # logic start
    init()
    # telebot start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.InlineKeyboardButton("Начинаем")
    markup.add(btn)
    bot.send_message(message.from_user.id, "Приветствую! Ты открыл справочную книгу! Начнем работу?", reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global typeOfFunc, iter, index

    if len(funcF.listOfNotes) != 0: # check data
        if message.text == 'Начинаем' or message.text == 'Продолжить':
            init()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Создать запись')
            btn2 = types.KeyboardButton('Отредактировать запись')
            btn3 = types.KeyboardButton('Поиск записи')
            btn4 = types.KeyboardButton('Удалить запись')
            btn5 = types.KeyboardButton('/start')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, 'Что будем делать?', reply_markup=markup) #ответ бота
        # MAIN functions menu :
        elif message.text == 'Создать запись':
            bot.send_message(message.from_user.id, 'Введите название записи')
            typeOfFunc = 1
        elif message.text == 'Отредактировать запись':
            bot.send_message(message.from_user.id, 'Какую запись отредактировать?')
            typeOfFunc = 2
        elif message.text == 'Поиск записи':
            bot.send_message(message.from_user.id, 'Введите имя записи, для поиска')
            typeOfFunc = 3
        elif message.text == 'Удалить запись':
            bot.send_message(message.from_user.id, 'Введите имя записи, для поиска')
            typeOfFunc = 4
            
            
        # Sub functions menu : 
        else :
                iter += 1
                if typeOfFunc == 1: # create note
                    if iter == 1:
                        new_note_name = str(message.text)
                        # check matches
                        flag = False
                        for n in range(len(funcF.listOfNotes)):
                            if new_note_name.lower() == funcF.listOfNotes[n]['name'].lower():
                                flag = True
                        if flag == False:
                            funcF.listOfNotes.append(funcF.notes)
                            funcF.listOfNotes[len(funcF.listOfNotes) - 1]["name"] = new_note_name
                            bot.send_message(message.from_user.id, 'Имя новой записи - ' + new_note_name)
                            bot.send_message(message.from_user.id, 'Введите почту')
                        else:
                            iter = 0
                            bot.send_message(message.from_user.id, 'Ошибка, такая запись уже имеется')
                            bot.send_message(message.from_user.id, 'Введите новое имя')
                        
                    elif iter == 2:
                        new_note_mail = str(message.text)
                        funcF.listOfNotes[len(funcF.listOfNotes) - 1]["mail"] = new_note_mail
                        bot.send_message(message.from_user.id, 'Введите номер телефона')
                    elif iter == 3:
                        new_note_number = str(message.text)
                        funcF.listOfNotes[len(funcF.listOfNotes) - 1]["number"] = new_note_number
                        print(funcF.listOfNotes[len(funcF.listOfNotes) - 1])
                        funcF.exportNotes()
                        typeOfFunc = 0
                        iter = 0
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn = types.InlineKeyboardButton("Продолжить")
                        markup.add(btn)
                        bot.send_message(message.from_user.id, "Новая запись сохранена", reply_markup=markup)
                    
                elif typeOfFunc == 2: # render
                    if iter == 1:
                        renote_name = str(message.text)
                        check_name = renote_name.lower()
                        bot.send_message(message.from_user.id, 'Редактируем запись - ' + renote_name)
                    
                        # check matches
                        print(funcF.listOfNotes)
                        flag = False
                        for n in range(len(funcF.listOfNotes)):
                            print(check_name)
                            print(funcF.listOfNotes[n]['name'].lower())
                            if check_name.find(funcF.listOfNotes[n]['name'].lower()) != -1:
                                flag = True
                                index = n
                                print('index-' + str(index))
                        if flag == True:
                            bot.send_message(message.from_user.id, 'Измените почту')
                        else:
                            typeOfFunc = 0
                            iter = 0
                            bot.send_message(message.from_user.id, 'Ошибка, такой записи нет')
                            
                    elif iter == 2:
                        new_note_mail = str(message.text)
                        funcF.listOfNotes[index]["mail"] = new_note_mail
                        bot.send_message(message.from_user.id, 'Измените номер телефона')
                    elif iter == 3:
                        new_note_number = str(message.text)
                        funcF.listOfNotes[index]["number"] = new_note_number
                        print(funcF.listOfNotes[index])
                        funcF.exportNotes()
                        typeOfFunc = 0
                        iter = 0
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        btn = types.InlineKeyboardButton("Продолжить")
                        markup.add(btn)
                        bot.send_message(message.from_user.id, "Запись обновлена", reply_markup=markup)
                        
                elif typeOfFunc == 3: # search note and print
                    search_note_name = str(message.text).lower()
                    bot.send_message(message.from_user.id, 'Ищем запись по имени - ' + search_note_name)
                    flag = False
                    for n in range(len(funcF.listOfNotes)):
                        check_name = funcF.listOfNotes[n]["name"].lower()
                        if search_note_name.find(check_name) != -1:
                            bot.send_message(message.from_user.id, 'Запись найдена')
                            bot.send_message(message.from_user.id, 'Имя - ' + funcF.listOfNotes[n]["name"])
                            bot.send_message(message.from_user.id, 'Почта - ' + funcF.listOfNotes[n]["mail"])
                            bot.send_message(message.from_user.id, 'Телефон - ' + funcF.listOfNotes[n]["number"])
                            flag = True
                    if flag != True:
                        bot.send_message(message.from_user.id, 'Запись не найдена')
                        print('Запись не найдена')
                    bot.send_message(message.from_user.id, 'Что еще требуется сделать?')
                    typeOfFunc = 0
                    iter = 0
                
                elif typeOfFunc == 4: # delete note
                    delete_note_name = str(message.text).lower()
                    bot.send_message(message.from_user.id, 'Удаляем запись - ' + delete_note_name)
                    flag = False
                    for n in range(len(funcF.listOfNotes)):
                        check_name = funcF.listOfNotes[n]["name"].lower()
                        print(delete_note_name.find(check_name))
                        if delete_note_name.find(check_name) != -1:
                            flag = True
                            funcF.listOfNotes.pop(n)
                            funcF.exportNotes()
                    if flag == True:
                        bot.send_message(message.from_user.id, 'Запись успешно удалена')
                    else:
                        bot.send_message(message.from_user.id, 'Ошибка, такой записи нет')
                    typeOfFunc = 0
                    iter = 0
                    
                elif typeOfFunc == 0:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn = types.InlineKeyboardButton("Продолжить")
                    markup.add(btn)
                    bot.send_message(message.from_user.id, "Ошибка, начать заново", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.InlineKeyboardButton("/start")
        markup.add(btn)
        bot.send_message(message.from_user.id, "Ошибка, начать заново", reply_markup=markup)
        
                         
def poll():
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        print('error timeout')
    print('please, restart!')
    
def startWord():
    print('Program has started')
    
def init():
    typeOfFunc = 0
    iter = 0
    print('start')
    funcF.importNotes()