text = input("Text: ")
splitText = text.split()
last = splitText[0]


for word in splitText:
    if word[0] >= last[0]:
        last = word

print("Last: " + last)