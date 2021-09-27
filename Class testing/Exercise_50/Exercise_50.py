import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now() \
            .strftime('%m-%d-%Y %H:%M:%S')