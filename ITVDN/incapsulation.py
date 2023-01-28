public
_protected
__private
#
# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, Name):
#         self.__name = Name
#
#
# Pit = User("Petia")
# print(Pit.name)
#
# Pit.name = "Piter"
# print(Pit.name)
class TextProcessor:
    def __init__(self):
        self.symbols = ".,!?"

    def __is_punctuation(self, symbol):
        return symbol in self.symbols

    def get_clean_string(self, string):
        clean_text = ""
        for char in string:
            if self.__is_punctuation(char):
                continue
            clean_text += char
        return clean_text


# text = TextProcessor()
# print(text.get_clean_string("Hello, how it's going?"))

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is {}".format(self.__clean_string))
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_text(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ['Hello, John', "hey, how are you?"]
di.process_text(t)
