from ex4 import count_words

count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"}) == 3
count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"}) == 2
count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {u"sum", u"hamlet", u"infinity", u"anything"}) == 1, "Weird text"

