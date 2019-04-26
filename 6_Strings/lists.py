
import pyperclip

text = pyperclip.paste()

newText = text.split('\n')

for i in range(len(newText)):
    newText[i] = '* ' + newText[i]

text = '\n'.join(newText)
print(text)
