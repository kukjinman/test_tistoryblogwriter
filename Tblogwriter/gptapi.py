from openai import OpenAI

def sendchatGPT(text):

    mygptkey = "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"

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=mygptkey,
    )
    messages = [
        {
            "role": "system",
            "content": "제일 첫째 줄에는 해당 포스트 견해에 대한 블로그 제목을 줘",
        },
        {
            "role": "system",
            "content": "해당 기사의 내용을 개인적인 사람의 의견처럼 견해와 리뷰를 한국어로 작성해줘",
        },
        {
            "role": "system",
            "content": "자연스럽게 정보를 전달하는 블로그 글처럼 개인적인 사람의 견해와 리뷰를 한국어로 너가 답변할 수 있는 최대 토큰만큼 써줘",
        },
        {
            "role": "system",
            "content": "한국인의 글을 잘쓰는 블로거 처럼 글을 한국어로 써줘",
        },
        {
            "role": "system",
            "content": "이런 글이 처음 읽었다는 사람의 기준에서 해당 내용과 직접적인 경험이 없다는 간주하에 써줘",
        },
        {
            "role": "system",
            "content": "견해에 대해서 글이 기승전결이 잘 들어나서 리뷰글을 써줘",
        }
    ]

    # Add each paragraph as a user message
    for idx, paragraph in text.items():
        tag_name, body = paragraph
        messages.append({
            "role": "user",
            "content": f"{tag_name}:::{body}"
        })
    print(messages)

    #        model="gpt-3.5-turbo",
    #        model="gpt-4",

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        # stream=True,

    )

    print(chat_completion.choices[0].message.content)
    print("Prompt tokens used: ", chat_completion.usage.prompt_tokens)
    print("Completion tokens used: ", chat_completion.usage.completion_tokens)
    return chat_completion.choices[0].message.content.split('.')
