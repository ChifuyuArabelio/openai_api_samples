# -*- coding: utf-8 -*-

# Python Default Modules
import sys

# Third Party Modules
from langchain_openai import ChatOpenAI
from langchain.schema import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)


"""
LangChain ChatOpenAI Sample.

GPT Model: gpt-4o-mini

Versions:
    python==3.12.2
    langchain==0.2.11
    langchain-openai==0.1.17
"""


# GPT Model
gpt_model: str = "gpt-4o-mini"

# Default Message Contents
system_message_content: str = ""
ai_message_content: str = ""


def chat_langchain(api_key: str, request_content: str) -> str:
    """Chat with LangChain

    Args:
        api_key (str): OpenAI API Key
        request_content (str): Request Content

    Returns:
        str: Response Message
    """
    try:
        llm = ChatOpenAI(
            model=gpt_model,
            api_key=api_key,
            temperature=1,
            max_tokens=1000,
            timeout=30,
            max_retries=2,
        )
        messages = [
            SystemMessage(content=system_message_content),
            HumanMessage(content=request_content),
            AIMessage(content=ai_message_content),
        ]
        response: BaseMessage = llm.invoke(messages)
        response_content: str = response.content
        return response_content
    except Exception as ex:
        return str(ex)


def main():
    """Main Function"""
    # OpenAI API Key
    api_key = sys.argv[1]
    # User Message
    message = input("Message: ")

    # Request to OpenAI API with LangChain
    response_message: str = chat_langchain(
        api_key=api_key,
        request_content=message,
    )
    print(response_message)


# Application Entry Point
if __name__ == "__main__":
    main()
