# Review words:
#   Each word will have the prompt it is used in, list of words with high semantic distance
# word_dict = {
#       "prompt":  "prompt with ____",
#       "word" :  "word",
#       "high_words": ["a","b","c"]
#}
import spacy
import utils
import heapq
import json
from tqdm import tqdm
nlp = spacy.load('en_core_web_trf')
new_words = utils.load_vocab("new")

def generateDiffWords(word):
    sim_list = []
    for new_word in new_words:
        diff = nlp(word).similarity(new_word)
        sim_list.append((diff, new_word))
    heapq.heapify(sim_list)
    word_list = []
    for sim in sim_list[-3:]:
        word_list.append(sim[1])
    return word_list

def getReview(word, prompt):
    word_dict = {}
    diff_words = generateDiffWords(word)
    problem = prompt.replace(word, "____")
    word_dict["prompt"] = problem
    word_dict["word"] = word
    word_dict["diff_words"] = diff_words
    return word_dict
print(getReview("doctrine","Have you read the new company ____?" ))
'''
with open("conversations.json") as fp:
    ans_dict = json.load(fp)
words_dict = {}
for key in tqdm(ans_dict):
    if len(ans_dict[key]) != 0:
        if len(ans_dict[key][0]["examples"]):
            words_dict[key] = getReview(key, ans_dict[key][0]["examples"][0])
            '''
#with open("reviews.json", "w") as fp:
#    fp.write(json.dumps(words_dict, indent=4, ensure_ascii=False))
print("Done")

    
