import emoji

text = input("Input: ")

emote = emoji.emojize(text, language='alias')

print("Output:  " , emote)