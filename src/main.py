import os
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Получение переменной окружения
#F5 для запуска, чтобы переменная из json подтянулась
giga_chat_auth = os.getenv("GigaChat_Auth")
#data=[Model(id_='GigaChat', object_='model', owned_by='salutedevices'), 
#Model(id_='GigaChat-Plus', object_='model', owned_by='salutedevices'), 
#Model(id_='GigaChat-Pro', object_='model', owned_by='salutedevices')] object_='list'
chat = GigaChat(model="GigaChat", credentials=giga_chat_auth, temperature=1.2, max_tokens=600, profanity_check=True);

#print(chat.get_num_tokens("Сколько токенов в этой строке"));

messages = [
    AIMessage(
        content="Ты бот-писатель детективных и приключенческих историй. \n" + 
        "Ты на переданное тебе предложение \n" +
        "пишешь красочное, детальное продолжение истории с количеством не больше 90 слов. \n" +
        "История происходит только в одной локации и повествование ведется от главного героя. \n" + 
        "Главный герой был задан в переданном тебе тексте, если нет, то ты его создаешь сам. \n" + 
        "В конце твоего рассказа история никогда не заканчивается, а ты ставишь многоточии."
    )
]

messages_2 = [
    SystemMessage(
        content="Ты должен предложить 3 коротких варианта на выбор продолжения текста. Не больше 10 слов."
    )
]

while(True):
    res = ""
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    print("Bot: ", res.content)
    messages_2.append(HumanMessage(content=res.content))
    res = chat(messages_2)
    print("Varients: ", res.content)