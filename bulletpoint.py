#! /usr/bin/env python
#Add bullet points in front of each line of the copied text and copied back to the clipboard
import pyperclip 

text=pyperclip.paste()
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='*'+lines[i]
final_text='\n'.join(lines)
pyperclip.copy(final_text)
