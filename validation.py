from OpenAiClient import request_openai


# ChatGPTを使ってメッセージを検証する
async def validate_massage_by_chatgpt(message: str) -> bool:
    prompt = f"Output 1 if the following text is part of a Japanese conversation\n" \
             f"\n" \
             f"{message}\n" \
             f"\n" \
             f"Output:"

    response = await request_openai(prompt)
    response_message = response['choices'][0]['message']['content']

    # レスポンスメッセージに'1'が含まれている場合はTrueを返す
    return '1' in response_message
