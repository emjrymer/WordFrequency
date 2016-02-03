given_sentence = "This this zebra zebra is zebra ball ace ace ace that this wonderful."

new_words = given_sentence.lower().replace(".", "").split()

d = {}

for word in set(new_words):
    d[word] = new_words.count(word)
    print(word, new_words.count(word))

l = d.items()

def val_sort(val):
    return val[1]

d = sorted(l, key=val_sort)
print("Word Frequency: " + str(d))

top_twenty = (d[-5:])
print("Twenty most popular: " + str(top_twenty))