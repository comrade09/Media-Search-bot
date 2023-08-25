from pyrogram import Client, filters
import time
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery , Message
import os
from bot import app
import asyncio
import random

from pyrogram import Client, filters
import time

chat_id = -1001814803421

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

# Create a Pyrogram client
app = Client("quiz_bot")  

# Function to send a quiz question
async def send_question(client, chat_id, question):
    options = question["options"]
    question_text = question["question"]
    explanation = question.get("explanation", None)  # Get the explanation, if provided

    poll_options = [option for option in options]
    correct_option = question["correct_option"]  # 0-indexed correct option

    poll_message = await client.send_poll(chat_id, question=question_text, options=poll_options, type="quiz", correct_option_id=correct_option)

    if explanation:
        # Wait for 30 seconds
        await asyncio.sleep(30)

        # Send the explanation as a message
        await client.send_message(chat_id, explanation)

    return poll_message

# Function to send quiz questions at intervals
async def send_quiz_questions():
    async with app:
        for question in questions:
            await send_question(app, chat_id, question)
            await asyncio.sleep(10)  # Wait for 10 seconds before sending the next question

# Call the function to send quiz questions
asyncio.run(send_quiz_questions())
