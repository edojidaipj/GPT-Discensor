import httpx as httpx
from config import openai_api_key


async def request_openai(prompt):
    endpoint = 'https://api.openai.com/v1/chat/completions'
    headers = {
            'Content-Type':  'application/json',
            'Authorization': f"Bearer {openai_api_key}"
    }
    data = {
            'model':    'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': prompt}]
    }
    timeout = 10  # 10秒でタイムアウト

    # httpxを使ってOpenAIのAPIにリクエストを送る
    async with httpx.AsyncClient() as openai_client:
        # リクエストを送る
        response = await openai_client.post(
                endpoint,
                json = data,
                headers = headers,
                timeout = timeout
        )

        # エラーが発生した場合は例外を発生させる
        response.raise_for_status()

        return response.json()
