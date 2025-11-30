class Cow:
    def __init__(self, name):
        self._name = name
        self._image = None

    def get_name(self):
        return self._name

    def get_image(self):
        return self._image

    def set_image(self, image):
        self._image = image
