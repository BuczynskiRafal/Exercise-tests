class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"{__class__.__name__}{self.components}"