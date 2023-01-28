# Инкапсуляция
class WithoutSymbols:
    def __init__(self):
        self._punktuation = ".,!"

    def __is_punktuation(self, char):
        return char in self._punktuation

    def get_clean_string(self, _text):
        clear_text = ""
        for char in _text:
            if self.__is_punktuation(char):
                continue
            else:
                clear_text += char
        return clear_text


text = "hello, world !.!"
p = WithoutSymbols()
print(p.get_clean_string(text))

class TextLoader:
    def __init__(self):
        self.__text_processor = WithoutSymbols()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is: {}".format(self.__clean_string))
        return self.__clean_string

class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts

di = DataInterface()
t = ["Hello, how its. going!"]
ct = di.process_texts(t)