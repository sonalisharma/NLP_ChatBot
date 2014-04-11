# content of test_sample.py
import sys
sys.path.append('../')

import chat as c
import ourchat as o
import nltk

chatbot = c.Chat(o.pairs, nltk.chat.eliza.reflections)


def test_getbigrams():
	tokens = chatbot.createBiGrams("test")
	assert "test" in tokens


def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5