# Unit 60
# a = []
# dir(a) shows the list of all functions

# while True:
#     words = input("Say something: ")
#     a.append(words)
#     if "\end" in a:
#         a.remove("\end")
#         print(*a, sep='. ')
#         break


def sentence_maker(phrase):
    interrogatives =("how", "what", "why")
    capitalitzed = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalitzed)
    else:
        return "{}".format(capitalitzed)


# print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))