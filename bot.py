import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "7331924888:AAHA4l-Z20U-uDMc_c3nlpnjpA9P33jwbBM"
bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📁 Наши услуги")],
            [KeyboardButton(text="📝 Оформить заявку")],
            [KeyboardButton(text="📞 Контакты")],
            [KeyboardButton(text="❓ Помощь")]
        ],
        resize_keyboard=True
    )
    return keyboard

@dp.message(Command("start"))
async def start_handler(message: Message):
    welcome_text = """Добро пожаловать в бот бухгалтерских услуг!

Мы поможем вам с:
• Ведением учета
• Налоговыми консультациями
• Подготовкой отчетности
• Регистрацией бизнеса

Выберите нужный раздел:""" 
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@dp.message(F.text == "📁 Наши услуги")
async def services_handler(message: Message):
    services_text = """📁 Наши услуги:

• Ведение учета - от 5000₽/месяц
• Налоговые консультации - от 1000₽
• Подготовка отчетности - от 3000₽
• Регистрация ИП/ООО - от 15000₽
• Восстановление учета - от 10000₽"""
    await message.answer(services_text)

@dp.message(F.text == "📝 Оформить заявку")
async def order_handler(message: Message):
    order_text = """📝 Для оформления заявки напишите:

1. Ваше имя
2. Контактный телефон  
3. Какая услуга нужна
4. Дополнительная информация

Или свяжитесь с нами по телефону: +7 (xxx) xxx-xx-xx"""
    await message.answer(order_text)

@dp.message(F.text == "📞 Контакты")
async def contacts_handler(message: Message):
    contacts_text = """📞 Наши контакты:

📱 Телефон: +7 (xxx) xxx-xx-xx
📧 Email: info@example.com
🌐 Сайт: www.example.com
📍 Адрес: г. Москва, ул. Примерная, д. 1

⏰ Время работы:
Пн-Пт: 9:00 - 18:00
Сб-Вс: выходные"""
    await message.answer(contacts_text)

@dp.message(F.text == "❓ Помощь")
async def help_handler(message: Message):
    help_text = """❓ Помощь:

Как пользоваться ботом:
• Выберите нужный раздел в меню
• Следуйте инструкциям
• Для заказа услуги нажмите "📝 Оформить заявку"

По всем вопросам пишите @your_username
или звоните +7 (xxx) xxx-xx-xx"""
    await message.answer(help_text)
    
async def main(): 
    await dp.start_polling(bot) 

if __name__ == "__main__": 
    asyncio.run(main())