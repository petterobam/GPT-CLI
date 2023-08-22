# Standard library
import json
import os.path as path

# Third party
from revChatGPT.V1 import Chatbot
from revChatGPT.V3 import Chatbot as ChatbotV3

# Local
from gchat.utilities.printers import prompt_user_for_credentials
from gchat.utilities.printers import prompt_user_for_credentials_v3

CONFIG_FP = path.join(path.expanduser("~"), ".gchat.json")

CONFIG_FP_KEY = path.join(path.expanduser("~"), ".gchat.key.json")


#########
# HELPERS
#########


def construct_query(language, error_message):
    # TODO: Create an class for mapping languages to exec commands
    language = "java" if language == "javac" else language
    language = "python" if language == "python3" else language
    language = "go" if language == "go run" else language

    query = f"Explain this {language} error message in brief and simple terms:"
    query += "\n```"
    query += f"\n{error_message}"
    query += "\n```"

    return query


def construct_query_v1(args):
    query = f"请帮忙用中文回答下面内容:"
    query += "\n```"
    query += " ".join(args)
    query += "\n```"

    return query

######
# MAIN
######


def is_user_registered():
    return path.exists(CONFIG_FP)

def is_user_registered_v3():
    return path.exists(CONFIG_FP_KEY)

def register_openai_credentials():
    email, password = prompt_user_for_credentials()
    config = {"email": email, "password": password}

    with open(CONFIG_FP, "w") as config_file:
        json.dump(config, config_file)
        
def register_openai_credentials_v3():
    api_key = prompt_user_for_credentials_v3()
    config = {"api_key": api_key}

    with open(CONFIG_FP_KEY, "w") as config_file:
        json.dump(config, config_file)

def get_chatgpt_res(args):
    config = json.load(open(CONFIG_FP))
    query = construct_query_v1(args)
    chatbot = Chatbot(config)
    
    # 定义prev_text变量，用于保存上一次对话的文本内容
    prev_text = ""
    # 定义一个数组
    messageArr = []
    # 通过ask方法向ChatGPT发送问题并获取回答
    for data in chatbot.ask(query):

        # 从回答数据中提取ChatGPT的回答，并去除前面已经输出过的文本部分
        message = data["message"][len(prev_text) :]

        # 将 Message 放进 messageArr
        messageArr.append(message)

        # 更新prev_text变量
        prev_text = data["message"]
    # 将 messageArr 作为返回值
    return messageArr

def get_chatgpt_res_v3(args):
    config = json.load(open(CONFIG_FP_KEY))
    query = construct_query_v1(args)
    chatbot = ChatbotV3(config)
    
    # 定义prev_text变量，用于保存上一次对话的文本内容
    prev_text = ""
    # 定义一个数组
    messageArr = []
    # 通过ask方法向ChatGPT发送问题并获取回答
    for data in chatbot.ask(query):

        # 从回答数据中提取ChatGPT的回答，并去除前面已经输出过的文本部分
        message = data["message"][len(prev_text) :]

        # 将 Message 放进 messageArr
        messageArr.append(message)

        # 更新prev_text变量
        prev_text = data["message"]
    # 将 messageArr 作为返回值
    return messageArr

def get_chatgpt_explanation(language, error_message):
    config = json.load(open(CONFIG_FP))
    query = construct_query(language, error_message)
    chatbot = Chatbot(config)
    return chatbot.get_chat_response(query)["message"].strip()

