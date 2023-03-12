import json

# Dictionaries
listOfNotes = []
notes = {
    "name" : '',
    "mail" : '',
    "number" : ''
}
# Json to notes
def importNotes():
    global listOfNotes
    with open("database.json", "r") as read_file:
        listOfNotes = json.load(read_file)
    return listOfNotes
# Notes to Json
def exportNotes():
    global listOfNotes
    with open("database.json", "w") as write_file:
        json.dump(listOfNotes, write_file)
    print('write successfull')
