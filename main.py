from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Кнопки
start_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Забрать план 💪", callback_data="get_plan"))
sub_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Я подписался ✅", callback_data="subscribed"))
ready_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Готово ✨", callback_data="ready"))
yes_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Да, хочу программу 🔥", callback_data="yes_program"))
buy_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти к оплате 💳", url="https://t.me/fake_payment_link"))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    text = "Привет!🤍\nЕсли ты здесь, значит ты готова перестать мечтать о красивой фигуре и наконец-то получить её.\n\nНажимай «Забрать план»!"
    await message.answer(text, reply_markup=start_kb)

@dp.callback_query_handler(lambda c: c.data == "get_plan")
async def get_plan(callback: types.CallbackQuery):
    await callback.message.answer(
        "Я Лиса, фитнес-тренер с 5-летним стажем. Записала для тебя видео с пошаговым планом. Получи его — подпишись на канал: https://t.me/fakechannel",
        reply_markup=sub_kb)

@dp.callback_query_handler(lambda c: c.data == "subscribed")
async def subscribed(callback: types.CallbackQuery):
    await callback.message.answer(
        "Отлично! После просмотра видео напиши 'Готово' и получишь бонус 🎁",
        reply_markup=ready_kb)

@dp.callback_query_handler(lambda c: c.data == "ready")
async def ready(callback: types.CallbackQuery):
    await callback.message.answer(
        "Вот и бонус: упражнения на мобильность тазобедренных суставов 💥
Убирают ушки на бедрах, снижают отёки, улучшают лимфоток.")
    await callback.message.answer(
        "Хочешь получить всю программу тренировок «Песочные часы»?
Напиши «Да» или нажми кнопку ниже.",
        reply_markup=yes_kb)

@dp.callback_query_handler(lambda c: c.data == "yes_program")
async def yes_program(callback: types.CallbackQuery):
    await callback.message.answer(
        "Программа «Песочные часы» — это:
• 8 недель тренировок с прогрессией
• Комплексы на живот
• Поддержка в чате
🔥 4500₽ вместо 5500₽ в течение 24 часов!",
        reply_markup=buy_kb)

@dp.message_handler(commands=["faq"])
async def faq(message: types.Message):
    await message.answer("Часто задаваемые вопросы:
1. Сколько длится курс?
2. Что входит в оплату?
3. Есть ли поддержка?

Напиши свой вопрос — я помогу!")

@dp.message_handler(commands=["help", "задатьвопрос"])
async def help_cmd(message: types.Message):
    await message.answer("Напиши свой вопрос сюда — я или моя команда скоро ответим 💬")

if __name__ == "__main__":
    executor.start_polling(dp)
