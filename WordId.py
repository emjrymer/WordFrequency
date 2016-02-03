with open("sample.txt") as my_file:
    contents = my_file.read()

answer = input("Do you want to enter a sentence or run provided text? ")

if answer == "yes":
    given_sentence = input("What is your sentence? ")#"This this zebra zebra is zebra ball ace ace ace that this wonderful."
    new_words = given_sentence.lower().replace(".", "").split()
else:
    new_words = contents.lower().replace(".", "").split()

d = {}

for word in set(new_words):
    d[word] = new_words.count(word)
    #print(word, new_words.count(word)) #don't need to print this list or it will take forever

l = d.items()

def val_sort(val):
    return val[1]

d = sorted(l, key=val_sort)
print("Word Frequency: " + str(d))

top_twenty = (d[-5:])
print("Twenty most popular: " + str(top_twenty))