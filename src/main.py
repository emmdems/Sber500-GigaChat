import os
from langchain.chat_models.gigachat import GigaChat

# Получение переменной окружения
giga_chat_client_id = os.getenv("GigaChat_Client_ID")

chat = GigaChat(model="GigaChat-Lite", credentials=giga_chat_client_id, verify_ssl_certs=False);

print(chat.get_num_tokens("Сколько токенов в этой строке"));