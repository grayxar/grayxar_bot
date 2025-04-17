
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "7266450737:AAFZJ5EUCq7BIuT3877D75bWkd2Lhgz8WiQ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Бесплатные схемы", "Платные схемы", "О проекте"]
    keyboard.add(*buttons)
    await message.answer(
        "Привет, ты попал в серую приватку grayxarb — здесь схемы, которые не объяснит ни один блогер.

Выбери, с чего хочешь начать:",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == "Бесплатные схемы")
async def free_schemes(message: types.Message):
    text = "1. Быстрый заработок на Binance P2P:
Регистрируешься на Binance → Ищешь монеты с разницей в цене между покупкой и продажей → Делаешь сделки вручную и снимаешь спред в $2–5 за цикл.

2. Авито + крипта:
Берёшь дешёвые товары (до 300 руб) на Авито, просишь оплату в USDT → Сливай в крипту и продавай P2P."
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "Платные схемы")
async def paid_schemes(message: types.Message):
    await message.answer("Доступ к платным схемам доступен после оплаты. Оформите подписку через @CryptoBot и вернитесь сюда.")

@dp.message_handler(lambda message: message.text == "О проекте")
async def about(message: types.Message):
    await message.answer("grayxarb — это проект, где собраны рабочие серые схемы по P2P, арбитражу, обналу и крипте.

Контакты: @grayxar")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
