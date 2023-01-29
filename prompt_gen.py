with open("new.txt", "r") as fp:
    topic = "business"
    prompts = []
    for word in fp:
        base_prompt = f"Generate a {topic} conversation containing the word {word}."
        prompts.append(base_prompt)
