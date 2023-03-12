import json

# Dictionaries
listOfNotes = []
notes = {
    "name" : '',
    "mail" : '',
    "numbers" : ''
}
# Json to notes
def importNotes():
    global listOfNotes
    with open("database.json", "r") as read_file:
        listOfNotes = json.load(read_file)
    print('listOfNotes:')
    print(listOfNotes)
# Notes to Json
def exportNotes():
    global listOfNotes
    with open("database.json", "w") as write_file:
        json.dump(listOfNotes, write_file)
    print('write successfull')