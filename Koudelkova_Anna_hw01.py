import json

with open("alice.txt", encoding="utf-8") as file:
    complete_text = file.read()

dictionary = {}
for letter in complete_text:
    letter = letter.lower()
    if letter == " ":
        continue
    elif letter == "\n":
        continue
    elif letter in dictionary.keys():
        dictionary[letter] += 1
    else:
        dictionary.update({letter: 1})

dictionary = dict(sorted(dictionary.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(dictionary, output_file, ensure_ascii=False, indent=4)