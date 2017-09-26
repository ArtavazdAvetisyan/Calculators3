class Calculator:

    def __init__(self):
        pass


    def set_arguments(self, data):
        for param in data:
            setattr(self, param, data[param])
