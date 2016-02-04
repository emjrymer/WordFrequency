with open("sample.txt") as my_file:
    contents = my_file.read()

answer = input("Do you want to enter a sentence or run provided text? ")

if answer == "yes":
    given_sentence = input("What is your sentence? ")
    new_words = given_sentence.lower().replace(".", "").replace("'", "").replace("--", "").replace("/n", "").replace("-", "").replace(",", "").replace("!", "").replace("?", "").split()
else:
    new_words = contents.lower().replace(".", "").split()

d = {}

for word in set(new_words):
    d[word] = new_words.count(word)

l = d.items()

def val_sort(val):
    return val[1]

d = sorted(l, key=val_sort, reverse = True)

print("Word Frequency: " + str(d))

for _ in d[:20]:
    print(_)