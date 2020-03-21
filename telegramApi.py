import requests
import time


def callTelegram(text):
    base_url = "https://api.telegram.org/"
    call_type = "bot"
    caller_id = "1147116456:AAEaa8Knqpr7rbVgEKuoVV5UQa8eQooL5bg"
    verb = "/sendMessage"
    channel_id = "@limortacciForMyBot"

    url = base_url + call_type + caller_id + verb

    query = "?chat_id="+channel_id+"&text="+text
    r = requests.post(url = url+ query)
