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
    request_content: str,
) -> str | None:
    """Request to OpenAI API

    Args:
        api_key (str): OpenAI API Key
        request_content (str): Request Content

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
            messages=[
                {
                    "role": "user",
                    "content": request_content,
                },
            ],
            model=gpt_model,
            max_tokens=70,
            n=2,
            stop=None,
            temperature=1,
        )
        print(chat_completion)

        # Response Content
        response_content = ""
        for _choice in chat_completion.choices:
            _message: ChatCompletionMessage = _choice.message
            _content: str | None = _message.content
            response_content += _content
        return response_content
    except Exception as ex:
        return str(ex)


def main():
    """Main Function"""
    # OpenAI API Key
    api_key: str = sys.argv[1]
    # User Message
    message: str = sys.argv[2]

    response_message: str | None = request_openai(
        api_key=api_key,
        request_content=message,
    )
    print(response_message)


# Application Entry Point
if __name__ == "__main__":
    main()
