# ///
# bot token: 8431004691:AAG4ApIuiN5vAC2-q7mKLHNRq5GHJwXxQ0s
# ///

import logging

from telegram import (
    Update,                 # /// Update - объект, который содержит всю информацию о входящем сообщении (текст, пользователь, чат и т.д.)
    ReplyKeyboardMarkup,    # /// ReplyKeyboardMarkup - создает клавиатуру с кнопками под полем ввода
    ReplyKeyboardRemove,     # /// ReplyKeyboardRemove - убирает кастомную клавиатуру, возвращая стандартную
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,            # /// Application - главный класс бота, управляет всеми процессами
    CommandHandler,         # /// CommandHandler - обрабатывает команды (например, /start)
    MessageHandler,         # /// MessageHandler - обрабатывает текстовые сообщения
    ContextTypes,           # /// ContextTypes - типы данных для контекста бота
    ConversationHandler,    # /// ConversationHandler - управляет многошаговыми диалогами
    filters,                 # /// filters - фильтры для отбора сообщений по типу
    CallbackQueryHandler,
)

# /// настройка логирования 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # /// шаблон вывода логов: время - имя логгера - уровень - сообщение
    level=logging.INFO                                              # /// записывать сообщения уровня INFO и выше (INFO, WARNING, ERROR)
)

BOT_TOKEN = "8431004691:AAG4ApIuiN5vAC2-q7mKLHNRq5GHJwXxQ0s"        # /// Токен от @BotFather

WELCOME, SECOND_STEP, ASK_INFO, ASK_INFO_2 = range(4)                                     # /// WELCOME = 0, SECOND_STEP = 1


me = 535431808
hr = 7196767339
#/// обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int: # /// update - информационный объект, context - объект для хранения данных между вызовами функций, -> int - функция возвращает целое число (состояние диалога)
    welcome_text = "Мы рады, что Вы приняли оффер и вскоре присоединитесь к команде.😊\n\
В оговоренный день, будем ждать Вас на оформление в 10.00 по адресу:\
г. Минск, пр-т Дзержинского, 104, БЦ «Титан», средняя башня (ст. метро «Петровщина»), 18 этаж.\n\
Когда  будете внизу – позвоните HR-специалисту по номеру +375293670822, Вас встретят.\n\n\
Сейчас я расскажу, какие документы взять с собой.\
"
    keyboard = [
        ["Давай!"],
        ["Отмена"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,                       # /// keyboard - наш массив кнопок,   
        resize_keyboard=True            # /// resize_keyboard=True - автоматически подгонять размер кнопок
    )   

    await update.message.reply_text(    # /// await - ждем завершения отправки сообщения, update.message.reply_text() - отвечает на сообщение пользователя
        welcome_text,                   # /// welcome_text - текст сообщения
        reply_markup=reply_markup       # /// reply_markup=reply_markup - прикрепляем клавиатуру с кнопками
    )

    return WELCOME                      # /// Возвращаем состояние WELCOME, указывая что диалог перешел в этап приветствия


# /// Функция для обработки выбора пользователя
async def welcome_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:   # /// update - информационный объект, context - объект для хранения данных между вызовами функций, -> int - функция возвращает целое число (состояние диалога)
    user_choice = update.message.text   # /// Получаем текст сообщения, которое отправил пользователь
    if user_choice == "Давай!":
        second_text = "\
Пожалуйста, возьми с собой:\n\
•	Фото (1 шт маленькая)\n\
•	Паспорт / ID карта / Вид на жительство\n\
•	Карточка соц.страхования (зеленая)\n\
•	Дипломы\n\
•	Трудовая книжка\n\
•	Свидетельства о рождении детей (до 18 лет)\n\
•	Справка с места учебы ребенка (если более 18 лет)\n\
•	Сертификаты 1С (если есть)\n\
•	Военный билет (если есть)\n\
•	Счет БелВэб Банка (если есть).\n\
Ближайшее отделение банка к нашему офису: пр-т Дзержинского, 122. Специалисту банка скажите, \
что устраиваетесь на работу в ООО «Электронная экономика».\n\n\
У нас есть еще одна небольшая просьба 💙\
"
        keyboard = [
            ["Какая?"],
            ["В начало..."]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,                       # /// Массив кнопок                       
            resize_keyboard=True            # /// Подгоняем размер кнопок
        )

        await update.message.reply_text(
            second_text,                    # /// Текст сообщения для второй страницы
            reply_markup=reply_markup       # /// Крепим клавиатуру с кнопками
        )

        return SECOND_STEP                  # /// Переходим в состояние SECOND_STEP (второй шаг диалога)

    elif user_choice == "Отмена":      # /// Проверка на ввод
        await update.message.reply_text(  # /// Отправляем сообщение о прерывании
            "Возврат в главное меню. Отправь /start чтобы начать занаво.",
            reply_markup=ReplyKeyboardRemove()  # /// Убираем клавиатуру
        )
    
        return ConversationHandler.END      # /// Заврешаем диалог


# /// Функция для обработки SECOND_STEP
async def second_step_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_choice = update.message.text       # /// Получаем текст сообщения от пользователя

    if user_choice == "Какая?":        # /// Проверка на ввод
        await update.message.reply_text("\
Вышлите, пожалуйста, в ответном сообщении свою фотографию и небольшую самопрезентацию(Двумя сообщениями). \
Мы разместим эту информацию в корпоративном чате, чтобы представить Вас команде. 😊 \n\n\
Например:\n\
Всем привет! Меня зовут Ян, я уже 15 лет в IT. Начинал как бизнес-аналитик, затем стал менеджером проектов.\
Работая во франчайзи, я активно взаимодействовал с крупнейшими предприятиями РБ.\
В свободное время я увлекаюсь футболом, хайкингом и спортивным ориентированием.\
Люблю скорость и с удовольствием гоняю с друзьями на карте. Рад присоединиться к Команде!\
            ",
        reply_markup=ReplyKeyboardRemove(),
        )
        return ASK_INFO
    
    elif user_choice == "В начало...":      # /// Проверка на ввод
        await update.message.reply_text(    # /// Отправляем сообщение
            "Диалог завершен. Для начала нового диалога отправьте /start",
            reply_markup=ReplyKeyboardRemove()  # /// Убираем клавиатуру
        )
    
        return ConversationHandler.END      # /// Завершаем диалог


async def ask_info_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    message = update.message
    
    # Сохраняем текст
    if message.text:
        context.user_data["info_text"] = message.text

    # Сохраняем фото
    if message.photo:
        context.user_data["photo_id"] = message.photo[-1].file_id
        await message.reply_text("Фото получено ✅")

    # Если есть и текст, и фото — отправляем HR
    if "info_text" in context.user_data and "photo_id" in context.user_data:
        username = message.from_user.username
        uid = message.from_user.id
        target_chat_id = hr # 7196767339 - HR, 535431808 - me

        await context.bot.send_message(
            chat_id=target_chat_id,
            text=f"Новая информация от @{username} (ID: {uid}):\n{context.user_data['info_text']}"
        )

        await context.bot.send_photo(
            chat_id=target_chat_id,
            photo=context.user_data["photo_id"]
        )

        keyboard = [
            ["Какой?"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,                       # /// Массив кнопок                       
            resize_keyboard=True            # /// Подгоняем размер кнопок
        )

        await message.reply_text(
            "Спасибо! Всё отправлено HR 😊\nИ ещё один технический момент",
            reply_markup=reply_markup
        )

        context.user_data.clear()
        return ASK_INFO_2
    
    else:
        await message.reply_text(
            "Отлично! Теперь пришлите вторую часть: фото и текст нужны оба 📌"
        )
        return ASK_INFO


async def ask_info_2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_choice = update.message.text

    if user_choice == "Какой?":
        context.user_data.clear()
        await update.message.reply_text(
            "Чтобы мы могли подготовить к Вашему выходу корпоративную почту и доступы, напишите:\n" \
            "🔹 ФИО латиницей\n" \
            "🔹 Дата рождения (в формате ДД.ММ.ГГГГ)",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ASK_INFO_2
    
    context.user_data.clear()

    message = update.message

        # Сохраняем текст
    if message.text:
        context.user_data["info_text"] = message.text

    if "info_text" in context.user_data:
        username = message.from_user.username
        uid = message.from_user.id
        target_chat_id = hr # 7196767339 - HR, 535431808 - me

    await context.bot.send_message(
        chat_id=target_chat_id,
        text=f"Дополнительная информация от @{username} (ID: {uid}):\n{context.user_data['info_text']}"
    )

    keyboard_inline = InlineKeyboardMarkup([
            [InlineKeyboardButton("Первый", callback_data="Первый")],
            # [InlineKeyboardButton("Второй", callback_data="Второй")],
            # [InlineKeyboardButton("И напоследок 😊", callback_data="Третий")],
        ]
    )

    await update.message.reply_text(
        "Спасибо! Всё отправлено HR 😊\n" \
        "А теперь я расскажу несколько общих организационных моментов!\n\n",
        reply_markup=keyboard_inline,
    )

    # await update.message.reply_text(
    #     "Чтобы начать общение нажмите /start :)"
    # )

    return ConversationHandler.END
        

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(        # /// Отправляем сообщение
        "Диалог завершен. Чтобы продолжить введите в чат: /start",
        reply_markup=ReplyKeyboardRemove()  # /// Убираем клавиатуру
    )

    return ConversationHandler.END


# /// Функция-оброботчик неизвестных обращений
async def handle_unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(        # /// Отправляем сообщение
        "Используйте кнопки для навигации под чатом или напишите в чат: /start"
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()  # ответ Telegram, чтобы не было «часиков»

    if query.data == "Test":
        await query.message.reply_text(
            "Кнопка нажата! 🎉\nЧтобы начать заново — /start"
        )

    elif query.data == "Первый":
        await query.message.reply_text(
            "Обед в нашей компании с 13.00 до 14.00. У нас есть кухня с холодильником, чайником, микроволновкой. " \
            "Чай и кофе в офисе бесплатный и безлимитный.  А вот столовые приборы лучше принести свои. Кроме того, " \
            "на территории БЦ Титан и рядом с ним есть много кафе и точек общепита.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Второй", callback_data="Второй")]
            ])
        )

    elif query.data == "Второй":
        await query.message.reply_text(
            "В компании нет строгого дресс-кода, мы руководствуемся нормами приличия и пониманием " \
            "того, что мы приходим на работу в офис.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("И напоследок 😊", callback_data="Третий")]
            ])
        )

    elif query.data == "Третий":
        await query.message.reply_photo(
            open("Picture1.png", "rb")
        )
        await query.message.reply_text(        
            "Диалог завершен. Чтобы продолжить введите в чат: /start" 
        )
        return ConversationHandler.END

# /// Функция main() - главная функция бота
def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()    # /// Создаем объект Application, Application.builder() - начинаем сборку приложения, .token(BOT_TOKEN) - передаем токен бота, .build() - завершаем сборку и создаем объект
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],              # /// entry_points - точки входа в диалог (команда /start вызывает функцию start)
    
        states={
            WELCOME: [
                MessageHandler(filters.Text(["Давай!", "Отмена"]), welcome_handler)  # /// В состоянии WELCOME обрабатываем только тексты "Далее" и "Отмена" функцией welcome_handler
            ],
            SECOND_STEP: [
                MessageHandler(filters.Text(["Какая?","В начало..."]), second_step_handler)  # /// В состоянии SECOND_STEP обрабатываем только тексты "Назад" и "В начало..." функцией second_step_handler
            ],
            ASK_INFO: [
                MessageHandler(filters.TEXT | filters.PHOTO & ~filters.COMMAND, ask_info_handler)
            ],
            ASK_INFO_2: [
                MessageHandler(filters.TEXT, ask_info_2_handler)
            ]
        },

        fallbacks=[CommandHandler("cancel", cancel)]    # /// Обработчик для выхода из диалога 
    )
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(conv_handler)   # /// Добавляем обработчик диалога в приложение(application)
    application.add_handler(MessageHandler(filters.ALL, handle_unknown))    # /// Добавляем обработчик для всех остальных дилогов в приложение(application)
    print("Bot is starting...")
    application.run_polling()   # /// Запускаем приложение в режиме поллинг(Постоянный опрос сервера Telegram)

if __name__ == "__main__":
    main()

        

