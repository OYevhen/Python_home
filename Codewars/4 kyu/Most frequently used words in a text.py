'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.
...
def top_3_words(text):
    return
'''
import re
from collections import Counter
import collections
# def top_3_words(text):

    # splited = text.split(" ")
    # splited2 = []
    # for i in splited:
    #     if i.isalpha() == False:
    #         continue
    #     else:
    #         splited2 += i
    # return splited2
    # clear_text = [elem for elem in text if elem.isalpha()]
    # return clear_text
    # clear_array = clear.split(" ")
    # counts = collections.Counter(clear)   #то же что и выше

import re
# def top_3_words(text):
#     clear = re.sub(r"[#/\\.:,]", "", text).lower().split(" ")  # удаление мусора
#
#     count = {i: clear.count(i) for i in clear if i != ""}
#
#     _count = sorted(count.values())
#     elem1 = _count.pop()
#     elem2 = _count.pop()
#     elem3 = _count.pop()
#     perem = ["", "", ""]
#     for k, v in count.items():
#         if v == elem1:
#             perem[0] = k
#         elif v == elem2:
#             perem[1] = k
#         elif v == elem3:
#             perem[2] = k
#
#         return perem


import re
'''
def top_3_words(text):
    clear_string = re.sub(r"[#/\\.:,']", "", text).lower().split(" ")

    dict_string = {i: clear_string.count(i) for i in clear_string if i != ""}
    # print("dict_string: ", dict_string)

    sorted_dict_string = sorted(dict_string.values())
    # print("sorted_dict_string:", sorted_dict_string)

    # print("max q-ty: ", max(sorted_dict_string))
    try:
        elem_1 = sorted_dict_string.pop()
        # print("elem_1: ", elem_1)
        elem_2 = sorted_dict_string.pop()
        elem_3 = sorted_dict_string.pop()
        # print("elem_3: ", elem_3)
    except ValueError:
        pass
    except IndexError:
        pass

    answer = ["","",""]
    for k, v in dict_string.items():
        if v == elem_1:
            answer[0] = k
            # print(answer)
        elif v == elem_2:
            answer[1] = k
            # print(answer)
        elif v == elem_3:
            answer[2] = k
            # print(answer)

    return answer

def test():
    if top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"]:
        print("OK")

test()

'''
from collections import Counter
import re
def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]


# print(top_3_words("a a a  b  c c  d d d d#/\.  e e e e e"))
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
# print(top_3_words("  , e   .. "))
# print(top_3_words("  '''  "))
# print(top_3_words("e bb bb e e"))
# print(top_3_words("a b c"))
print(top_3_words("  //wont won't won't "))
