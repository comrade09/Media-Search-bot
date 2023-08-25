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
import json

from pyrogram import Client, filters
import time



from pyrogram import Client, filters
import time



@Client.on_message(filters.command("quiz") & filters.user(1828345056))
async def start_quiz(client, message):
    chat_id = message.chat.id
    await client.send_message(chat_id, "Quiz has started! I will send you a question every 30 seconds. Answer with the correct option.")

    while True:
        for question in questions:
            await send_question(client, chat_id, question)
            await asyncio.sleep(3600)

questions = [
    
    {
        "question": "Which one is a primary sex organ?",
        "options": ["Scrotum", "Penis", "Testis", "Prostate gland"],
        "correct_option": 3,
        "explanation": "The primary sex organ in males is the testis, which produces sperm."
    },
    {
        "question": "Secondary sex organ is",
        "options": ["Testis", "Ovary", "Beard", "Vas deferens"],
        "correct_option": 4,
        "explanation": "Secondary sex organs are those structures that develop during puberty and are not directly involved in gamete production."
    },
    {
        "question": "Which acid occurs in semen?",
        "options": ["Citric acid", "Malic acid", "Oxaloacetic acid", "Succinic acid"],
        "correct_option": 1,
        "explanation": "Citric acid is one of the components found in semen."
    },
    {
        "question": "Vasa deferens is cut for",
        "options": ["Female sterilization","Male sterilization","Both of the above","Temporary sterilization"],
        "correct_option": 2,
        "explanation": "Vasa deferens is cut in male sterilization to prevent the passage of sperm."
    },
    {
        "question": "The function of seminal fluid is -",
        "options": ["sexual attraction","to provide stability to egg","to provide a medium for the movement of sperms","to provide acidic medium"],
        "correct_option": 3,
        "explanation": "Seminal fluid provides a medium for the movement of sperm cells and provides nutrients to support their viability."
    },
    {
        "question": "Vasa efferentia connect the",
        "options": [ "testes with epididymis", "kidneys with cloaca", "testes with urinogenital duct", "None of the above"],
        "correct_option": 1,
        "explanation": "Vasa efferentia connect the testes to the epididymis, facilitating the transport of sperm cells."
    },
    {
        "question": "In mammals, failure of testes to descend into scrotum is known as",
        "options": ["Paedogenesis","Castration","Cryptorchidism","Impotency"],
        "correct_option": 3,
        "explanation": "Cryptorchidism refers to the condition in which the testes do not descend into the scrotum, affecting fertility."
    },
    {
        "question": "Common duct formed by union of vas deferens and duct from seminal vesicle is",
        "options": ["urethra","tunica-vasculosa","ejaculatory duct","spermatic duct"],
        "correct_option": 3,
        "explanation": "The common duct formed by the union of vas deferens and the duct from seminal vesicle is known as the ejaculatory duct."
    },
    {
        "question": "Scrotum communicates with abdominal cavity through",
        "options": ["urethra","inguinal canal","vas deferens","epididymis"],
        "correct_option": 2,
        "explanation": "The scrotum communicates with the abdominal cavity through the inguinal canal."
    },
    {
        "question": "Tunica albuinea is the covering around",
        "options": ["Oviduct","Testis","Kidney","Heart"],
        "correct_option": 2,
        "explanation": "Tunica albuginea is the fibrous covering around the testis."
    },

]

async def send_question(client, chat_id, question):
    options = question["options"]
    question_text = question["question"]
    correct_option = question["correct_option"]

    poll_options = [f"{index+1}. {option}" for index, option in enumerate(options)]
    explanation = question.get("explanation", None)

    poll_message = await client.send_poll(
        chat_id="-1001814803421",
        question=question_text,
        options=json.dumps(poll_options),
        type="quiz",
        is_anonymous=False,
        correct_option_id =correct_option
        
        
    )

    if explanation:
        await asyncio.sleep(1800)  # Wait for 30 seconds
        await client.send_message(chat_id, f"{explanation} \n bot coded by @python_itachi" )
