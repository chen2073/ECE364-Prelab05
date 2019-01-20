from collections import namedtuple, Counter, OrderedDict


def get_distinct_words(words):
    duplicate_list = []
    for word in words:
        if word not in duplicate_list:
            duplicate_list.append(word)
            yield word


WordPosition = namedtuple('WordPosition', ['word', 'idx'])


def get_first_appearances(words):
    for word in get_distinct_words(words):
        yield WordPosition(word=word, idx=words.index(word))


def get_word_to_first_idx(words):
    lookup_table = {}
    for word in list(get_first_appearances(words)):
        lookup_table[word.word] = word.idx
    return lookup_table


def get_word_to_frequency(words):
    return dict(Counter(words))


def get_word_to_frequency_ordered_by_first_idx(words):
    order_dict = OrderedDict()
    for word in words:
        order_dict[word] = Counter(words)[word]
    return order_dict


if __name__ == "__main__":
    words = ("au", "bu", "cu", "cu", "cu", "du", "du", "du", "du", "du", "eu", "eu", "eu")
    #print(list(get_distinct_words(words)))
    # a = WordPosition(word=4,idx=5)
    # print(a)
    # print(a.word)
    # print(a[0])
    #print(list(get_first_appearances(words)))
    #print(list(get_distinct_words(words)))
    #print(list(get_first_appearances(words)))
    #print(get_word_to_first_idx(words))
    #print(get_word_to_frequency_ordered_by_first_idx(words))
    pass