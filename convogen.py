"""
Use OpenAI API to generate fake conversations using our vocabulary so far.
"""
import openai

# query openai api
openai.api_key = open("oaikey.txt", "r").read().strip()

know = open("convonotes.md", 'r').read()

TEMPLATE = """
Generate a conversation in Korean. Only incorporate the concepts I've learned about so far. I am attaching my study notes below.

MY NOTES:
""".strip()

prompt = TEMPLATE + "\n" + know

for i in range(5):

    resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    # we want to extract the content from the response
    result = resp["choices"][0]["message"]["content"]

    print(result)

    # write result to file
    print(i+1)
    with open(f"convos/convo{i+1}.txt", 'w') as f:
        f.write(result)
