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

def send_question(client, chat_id, question):
    options = question["options"]
    question_text = question["question"]
    explanation = question.get("explanation", None)  # Get the explanation, if provided

    poll_options = [option for option in options]
    correct_option = question["correct_option"]  # 0-indexed correct option

    poll_message = client.send_poll(chat_id, question=question_text, options=poll_options, type="quiz", correct_option_id=correct_option)

    if explanation:
        # Wait for 30 seconds
        time.sleep(4)

        # Send the explanation as a message
        client.send_message(chat_id, explanation)

    return poll_message
    
group_chat_id = -1001814803421
# Function to send quiz questions at intervals
def send_quiz_questions():
  
        for question in questions:
            send_question(Client, chat_id, question)
            time.sleep(10)  # Wait for 10 seconds before sending the next question

# Call the function to send quiz questions
send_quiz_questions()
