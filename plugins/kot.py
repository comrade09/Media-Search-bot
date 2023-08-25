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



from pyrogram import Client, filters
import time



@Client.on_message(filters.command("quiz") & filters.user(5496035221))
async def start_quiz(client, message):
    chat_id = message.chat.id
    await client.send_message(chat_id, "Quiz has started! I will send you a question every 30 seconds. Answer with the correct option.")

    while True:
        for question in questions:
            await send_question(client, chat_id, question)
            await asyncio.sleep(2)

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_option": 0,
        "explanation": "The capital of France is Paris."
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_option": 1,
        "explanation": "Mars is known as the 'Red Planet' due to its reddish appearance."
    },
    # Add more questions here
]

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
        correct_option_id=correct_option
    )

    if explanation:
        await asyncio.sleep(1)  # Wait for 30 seconds
        await client.send_message(chat_id, f"{explanation} \n bot by @python_itachi" ,  reply_to_message = poll_message)
