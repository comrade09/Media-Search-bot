from pyrogram import Client, filters
import time
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message
import os

import asyncio
import random

from pyrogram import Client, filters
import time

async def send_question(client, chat_id, question):
    options = question["options"]
    question_text = question["question"]
    correct_option = question["correct_option"]

    poll_options = [f"{index+1}. {option}" for index, option in enumerate(options)]
    explanation = question.get("explanation", None)

    poll_message = await client.send_poll(
        chat_id,
        question=question_text,
        options=poll_options,
        type="quiz",
        correct_option_id=correct_option,
        is_anonymous=False
    )

    if explanation:
        await asyncio.sleep(2)  # Wait for 30 seconds
        await client.send_message(chat_id, f"{explanation} \n this bot is made by @python_itachi ")

@Client.on_message(filters.command("quiz"))
async def start_quiz(client, message):
    chat_id = message.chat.id
    await client.send_message(chat_id, "Quiz has started! I will send you a question every 1 hour. Answer with the correct option.")

    for question in questions:
        await send_question(client, chat_id, question)
        await asyncio.sleep(10)  # Wait for 1 hour between questions

