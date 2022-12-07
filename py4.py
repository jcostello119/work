import random
sentence = "Look that animal is *adj today, look at that *noun it is cool."
sentence = sentence.split()
adjectives = ["beautiful", "handsome", "pretty",
              "warm", "fantastic"]
nouns = ["dog", "cat", "mouse", "pear", "lemon"]

indexCount = 0
for word in sentence:
    if word == "*adj":
        wordChoice = random.choice(adjectives)
        sentence[indexCount] = wordChoice

    indexCount += 1

indexCount = 0
for word in sentence:
    if word == "*noun":
        wordChoice = random.choice(nouns)
        sentence[indexCount] = wordChoice

    indexCount += 1
print(sentence)

#Better way to join list into a string
sentence =  " ".join(sentence)
print(sentence)

