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