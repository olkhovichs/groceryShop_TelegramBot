from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot, start
from handlers import catalog_hand
import keyboards.inline.main_menu as menu


# main
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await(message.answer('''Hi! 👋\nThis is a universal bot store for the sale of any goods.'''))
    await message.reply("Choose an action:", reply_markup=menu.main_menu())
    

if __name__ == '__main__':
    start(dp)
