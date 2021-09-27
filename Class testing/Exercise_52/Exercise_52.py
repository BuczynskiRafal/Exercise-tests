import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S')

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note(content))

    def search(self, value):
        return [note.content for note in self.notes if note.find(value)]