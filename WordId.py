with open("sample.txt") as my_file:
    contents = my_file.read()

with open("IgnoredText.txt") as ignored_file:
    ignored_words = ignored_file.read()

def val_sort(val):
    return val[1]

hard_mode_activated = False
keep_playing = True
new_words = contents.lower().replace(".", "").replace("'", "").replace("--", "").replace("/n", "").replace("-", "").replace(",", "").replace("!", "").replace("?", "").split()
ignored_words_list = ignored_words.lower().replace("/n", "").replace(",", " ").split()

decision = input("Please enter the secret file name to activate hard mode: ")

if decision == "python word_frequency.py sample.txt":
    hard_mode_activated = True

while hard_mode_activated:
    print("You have entered Hard Mode.  Here is the histogram for the words in the provided text.  ")
    filtered_words = [item for item in new_words if item not in ignored_words_list]

    f = {}

    for word in set(filtered_words):
        f[word] = filtered_words.count(word)
    k = f.items()

    f = sorted(k, key=val_sort, reverse = True)

    n = 0
    for item in f[:20]:
        trunk_num = (f[n+1][1])
        n += 1
        mult_fact = trunk_num/10
        print(str(f[n+1]) + str("#" * int(mult_fact)))
        hard_mode_activated = False

while keep_playing:
    want_to = input("Do you want to continue outside of Hard Mode? ")
    if want_to.lower() == "no":
        break

    answer = input("Do you want to enter a sentence or run provided text? ")

    if answer == "yes":
        given_sentence = input("What is your sentence? ")
        new_words = given_sentence.lower().replace(".", "").replace("'", "").replace("--", "").replace("/n", "").replace("-", "").replace(",", "").replace("!", "").replace("?", "").split()

    d = {}

    for word in set(new_words):
        d[word] = new_words.count(word)

    l = d.items()

    d = sorted(l, key=val_sort, reverse = True)

    print("Word Frequency: " + str(d))

    for _ in d[:20]:
        print(_)

print("Thanks for playing, sucker!")