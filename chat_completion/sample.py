# -*- coding: utf-8 -*-

# Python Modules
import sys

# Third Party Modules
from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessage


"""
OpenAI Chat Completion API Sample.

Use this script to request OpenAI Chat Completion API.
GPT Model: gpt-4o-mini

Versions:
    Ptython: 3.12.2
    openai: 1.37.1
"""


# GPT Model
gpt_model: str = "gpt-4o-mini"


def request_openai(
    api_key: str,
    user_message: str,
) -> str | None:
    """Request to OpenAI API

    Args:
        api_key (str): OpenAI API Key
        user_message (str): User Message

    Returns:
        str | None: Response Message
    """
    try:
        # OpenAI Client
        client = OpenAI(
            api_key=api_key,
        )

        # Request to OpenAI API
        chat_completion: ChatCompletion = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            max_tokens=50,
            temperature=0.7,
            n=1,
        )
        data = chat_completion.choices[0]
        message: ChatCompletionMessage = data.message
        content: str | None = message.content
        return content
    except Exception as ex:
        return str(ex)


def main():
    """Main Function"""
    # OpenAI API Key
    api_key: str = sys.argv[1]
    # User Message
    user_message: str = sys.argv[2]

    response_message: str | None = request_openai(
        api_key=api_key,
        user_message=user_message,
    )
    print(response_message)


# Application Entry Point
if __name__ == "__main__":
    main()
