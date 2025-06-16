import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Забрать план 💪", callback_data="get_plan"))
sub_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Я подписался ✅", callback_data="subscribed"))
ready_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Готово ✨", callback_data="ready"))
yes_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Да, хочу программу 🔥", callback_data="yes_program"))
buy_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти к оплате 💳", url="https://t.me/fake_payment_link"))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет!🤍\nНажимай «Забрать план»!", reply_markup=start_kb)

@dp.callback_query_handler(lambda c: c.data == "get_plan")
async def get_plan(callback: types.CallbackQuery):
    await callback.message.answer("Подпишись на канал: https://t.me/fakechannel", reply_markup=sub_kb)

@dp.callback_query_handler(lambda c: c.data == "subscribed")
async def subscribed(callback: types.CallbackQuery):
    await callback.message.answer("Напиши 'Готово' и получишь бонус 🎁", reply_markup=ready_kb)

@dp.callback_query_handler(lambda c: c.data == "ready")
async def ready(callback: types.CallbackQuery):
    await callback.message.answer("Вот и бонус: упражнения на мобильность ТБС 💥")
    await callback.message.answer("Хочешь полную программу? Напиши «Да» или нажми кнопку ниже.", reply_markup=yes_kb)

@dp.callback_query_handler(lambda c: c.data == "yes_program")
async def yes_program(callback: types.CallbackQuery):
    await callback.message.answer("Программа «Песочные часы»: 8 недель, поддержка, живот, цена — 4500₽ 🔥", reply_markup=buy_kb)

@dp.message_handler(commands=["faq"])
async def faq(message: types.Message):
    await message.answer("Часто задаваемые вопросы: ...")

@dp.message_handler(commands=["help", "задатьвопрос"])
async def help_cmd(message: types.Message):
    await message.answer("Задай свой вопрос — я помогу 💬")

if __name__ == "__main__":
    executor.start_polling(dp)
