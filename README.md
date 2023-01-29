# Sources
1. `new.txt` is a list of words used in businesses: https://www.vocabulary.com/lists/234528#view=list
2. `core.txt` is a list of words required for the College English Test in China: https://github.com/mahavivo/english-wordlists/blob/master/CET4_edited.txt
* The CET-4 is mandatory for university students in China who are not English majors. It is also a prerequisite for a bachelor's degree. Many employers in China prefer applicants with CET-4 or even CET-6 certification. (https://www.wikiwand.com/en/College_English_Test)

# Prompt Algorithm
1. Prompt GPT-3 x times for sentences containing `new.txt` words.
To do this generate set of prompts following the structure:
"Generate a ___business___ conversation containing the word ___"confined"___"

where business is the topic of the conversation and confined is the word to include.

2. Filter out the sentences that contains words not in `core.txt` or `new.txt`. 

```json
{
    "laborious": "Person 1: \"This project is proving to be quite laborious. We've been working on it for weeks and still haven't made much progress.\"\n\nPerson 2: \"I know, it's been a challenge. But I think if we keep at it, we'll eventually get there.\"",
    "inevitable": "Person 1: \"We need to start planning for the inevitable changes that will come with the new regulations.\"\n\nPerson 2: "Yes, it's inevitable that we'll have to make some adjustments. What do you think our first step should be?\""
}
```

# Dataflow
1. Start with the new words
2. Build prompts with each of the new words
3. Get responses from GPT-3 api
4. Parse the responses
```json
{
    "laborious": [
        {
            "synonoyms": ["a", "b", "c"],
            "chinese": "辛苦的",
            "examples": [
                "This project is proving to be quite laborious. We've been working on it for weeks and still haven't made much progress.",
                "I know, it's been a challenge. But I think if we keep at it, we'll eventually get there."
            ]
        },
        [
            "I can't believe how laborious this project is taking me. I thought it would be much easier!",
            "Yeah, it's definitely a lot more work than we anticipated. But I'm sure if we keep at it, we'll get it done eventually."
        ]
    ]
}
```
5. Sort them into two theoretical users

# Frontend

https://github.com/AlienKevin/L2Z_app
