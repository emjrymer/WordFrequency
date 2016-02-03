given_sentence = "This this is zebra zebra zebra ball ace ace ace that this wonderful."

#print(given_sentence.lower().replace(".", "").split())

given_sentence = given_sentence.lower().replace(".", "").split()

#print(set(given_sentence))

d = {}

for character in set(given_sentence):
    d[character] = given_sentence.count(character)
    #print(character, given_sentence.count(character))

#print(d.items())

l = d.items()

def val_sort(val):
    return val[1]

d = sorted(l, key=val_sort)
print(d)
#d = dict(d)# Don't have to turn back into dictionary
#print(d)
#d = d.sort(reverse=True)
#print(d)
