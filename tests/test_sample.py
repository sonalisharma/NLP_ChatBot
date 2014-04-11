# content of test_sample.py
import sys
sys.path.append('../')
import chat as c
from ourchat import *
import nltk
import pytest
from pairs import getpairs

chatbot = c.Chat(getpairs(), nltk.chat.eliza.reflections)


def test_getbigrams():
	tokens = chatbot.createBiGrams("test")
	assert "test" in tokens


def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5