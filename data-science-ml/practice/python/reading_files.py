"""
Working with files in python.
"""

with open('some_document.txt') as txt:
    txt_data = txt.read()
print(txt_data)

