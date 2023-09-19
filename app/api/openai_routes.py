from flask import Blueprint, Flask, request
from flask_login import login_required, current_user
from app.models import Card,db,Set
import os
import openai
import re

openai_routes = Blueprint("openai", __name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@openai_routes.route("/quiz/<int:setId>",methods = ["POST"])
def createChat(setId):
    print("[openai.api_key]",openai.api_key)

    set = Set.query.get(setId)

    allCards = Card.query.filter(Card.setId == setId).all()

    def cardsString(cards):
        prompt = ""
        for x in range(0,len(cards)):
            prompt = prompt + f"card {x + 1}, question: {cards[x].question}, answer: {cards[x].answer}"
        return prompt



    prompt = f"You are an assistant for a user studying cards, based on the following cards I would like you to ask the user a question, and once they return a response see if its correct. If the answer isn't correct you should give them the answer. But either way give them another question that starts with Here's another question. {cardsString(allCards)}"

    print("[prompt]",prompt)

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "system", "content": prompt},{"role":"user","content":"quiz me"}],
        temperature=0.3
    )

    print("[chats-gpt response]",res)

    chatGPT_reply = res["choices"][0]["message"]["content"]


    return [{"role": "system", "content": prompt},{"role":"user","content":"quiz me"},{"role":"assistant","content":chatGPT_reply}]


@openai_routes.route("/quiz/<int:setId>/teach",methods = ["POST"])
def teachChat(setId):

    set = Set.query.get(setId)

    allCards = Card.query.filter(Card.setId == setId).all()

    def cardsString(cards):
        prompt = ""
        for x in range(0,len(cards)):
            prompt = prompt + f"card {x + 1}, question: {cards[x].question}, answer: {cards[x].answer}"
        return prompt



    prompt = f"You are an assistant for a user studying cards. You should teach them the ideas in the cards. For each card give them background knowledge you think would be helpful and then ask them a question to confirm their understanding of the card. If they are correct, move on to another card. If they are incorrect elaborate on your previous explanation and then repeat the question.Here are the cards you need to teach them, {cardsString(allCards)} "

    print("[prompt]",prompt)

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "system", "content": prompt},{"role":"user","content":"Teach me"}],
        temperature=0.3
    )

    print("[chats-gpt response]",res)

    chatGPT_reply = res["choices"][0]["message"]["content"]


    return [{"role": "system", "content": prompt},{"role":"user","content":"Teach me"},{"role":"assistant","content":chatGPT_reply}]


@openai_routes.route("/chat",methods = ["POST"])
def messageChat():

    print("[openai.api_key]",openai.api_key)

    pastMessages = request.json["pastMessages"]

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = pastMessages,
        temperature=0.1
    )

    print("[RES]",res)

    chatGPT_reply = res["choices"][0]["message"]["content"]

    index = chatGPT_reply.find("Here's another question")

    teachIndex = re.search("Card [1234567890]:",chatGPT_reply)

    if index > -1:
        pastMessages.append({"role":"assistant","content":chatGPT_reply[0:index]})
        pastMessages.append({"role":"assistant","content":chatGPT_reply[index::]})
    elif teachIndex:
        pastMessages.append({"role":"assistant","content":chatGPT_reply[0:teachIndex.start()]})
        pastMessages.append({"role":"assistant","content":chatGPT_reply[teachIndex.start()::]})
    else:
        pastMessages.append({"role":"assistant","content":chatGPT_reply})

    return pastMessages, 200
