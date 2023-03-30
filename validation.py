import re


# 日本語のひらがな、カタカナ、漢字を除外する正規表現
def extract_non_japanese(text: str) -> str:
    non_japanese_pattern = re.compile(r'[^\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]')
    non_japanese_text = non_japanese_pattern.findall(text)
    return ''.join(non_japanese_text)


# non_japanese_textの文字数がallowed_chars以下の場合はTrueを返す
def length_of_non_japanese_text_is_less_than(text: str, allowed_chars: int) -> bool:
    non_japanese_text = extract_non_japanese(text)

    return len(non_japanese_text) <= allowed_chars


# non_japanese_textの文字数がallowed_chars以下の場合はTrueを返す
# そのほかのルールも追加する場合は新しく関数を作成し、ここで呼び出す
def validate_massage_rule(text: str, allowed_chars: int) -> bool:
    return length_of_non_japanese_text_is_less_than(text, allowed_chars)
