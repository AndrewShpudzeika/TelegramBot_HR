# ///
# bot token: 8431004691:AAG4ApIuiN5vAC2-q7mKLHNRq5GHJwXxQ0s
# ///

import logging

from telegram import (
    Update,                 # /// Update - объект, который содержит всю информацию о входящем сообщении (текст, пользователь, чат и т.д.)
    ReplyKeyboardMarkup,    # /// ReplyKeyboardMarkup - создает клавиатуру с кнопками под полем ввода
    ReplyKeyboardRemove     # /// ReplyKeyboardRemove - убирает кастомную клавиатуру, возвращая стандартную
)

from telegram.ext import (
    Application,            # /// Application - главный класс бота, управляет всеми процессами
    CommandHandler,         # /// CommandHandler - обрабатывает команды (например, /start)
    MessageHandler,         # /// MessageHandler - обрабатывает текстовые сообщения
    ContextTypes,           # /// ContextTypes - типы данных для контекста бота
    ConversationHandler,    # /// ConversationHandler - управляет многошаговыми диалогами
    filters                 # /// filters - фильтры для отбора сообщений по типу
)

# /// настройка логирования 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # /// шаблон вывода логов: время - имя логгера - уровень - сообщение
    level=logging.INFO                                              # /// записывать сообщения уровня INFO и выше (INFO, WARNING, ERROR)
)

BOT_TOKEN = "8431004691:AAG4ApIuiN5vAC2-q7mKLHNRq5GHJwXxQ0s"        # /// Токен от @BotFather

WELCOME, SECOND_STEP = range(2)                                     # /// WELCOME = 0, SECOND_STEP = 1


#/// обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int: # /// update - информационный объект, context - объект для хранения данных между вызовами функций, -> int - функция возвращает целое число (состояние диалога)
    welcome_text = """
        Добро пожаловать в нашего бота!
    Это приветственное сообщение c основной информацией o боте.
    Нажмите 'Далее' чтобы продолжить или 'Отмена' чтобы выйти.
    """
    keyboard = [
        ["Далее"]
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
    if user_choice == "Далее":
        second_text = """
            Это второе сообщение!
        Здесь может быть дополнительная информация, 
        инструкции или следующий шаг процесса.
        """
        keyboard = [
            ["Назад"],
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

    elif user_choice == "В начало...":      # /// Проверка на ввод
        await reply_markup.message.reply_text(  # /// Отправляем сообщение о прерывании
            reply_markup=ReplyKeyboardRemove()  # /// Убираем клавиатуру
        )
    
        return ConversationHandler.END      # /// Заврешаем диалог


# /// Функция для обработки SECOND_STEP
async def second_step_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_choice = update.message.text       # /// Получаем текст сообщения от пользователя

    if user_choice == "Назад":        # /// Проверка на ввод
        return await start(update, context) # /// Вызываем функцию start()
    
    elif user_choice == "В начало...":      # /// Проверка на ввод
        await update.message.reply_text(    # /// Отправляем сообщение
            reply_markup=ReplyKeyboardRemove()  # /// Убираем клавиатуру
        )
    
        return ConversationHandler.END      # /// Завершаем диалог
    

# /// Функция для отмены диалога
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(        # /// Отправляем сообщение
        "Диалог завершен. Чтобы продолжить введите в чат: /start",
        reply_markup=ReplyKeyboardRemove()  # /// Убираем клавиатуру
    )

    return ConversationHandler.END


# /// Функция-оброботчик неизвестных обращений
async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(        # /// Отправляем сообщение
        "Используйте кнопки для навигации под чатом или напишите в чат: /start"
    )


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()    # /// Создаем объект Application, Application.builder() - начинаем сборку приложения, .token(BOT_TOKEN) - передаем токен бота, .build() - завершаем сборку и создаем объект

        

