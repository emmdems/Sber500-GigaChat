import os
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage

# Получение переменной окружения
#F5 для запуска, чтобы переменная из json подтянулась
giga_chat_auth = os.getenv("GigaChat_Auth")
#data=[Model(id_='GigaChat', object_='model', owned_by='salutedevices'), Model(id_='GigaChat-Plus', object_='model', owned_by='salutedevices'), Model(id_='GigaChat-Pro', object_='model', owned_by='salutedevices')] object_='list'
chat = GigaChat(model="GigaChat", credentials=giga_chat_auth);

#print(chat.get_num_tokens("Сколько токенов в этой строке"));

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while(True):
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    print("Bot: ", res.content)