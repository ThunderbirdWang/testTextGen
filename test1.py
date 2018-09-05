#coding:utf-8
from textgenrnn import textgenrnn

txtgen=textgenrnn()

txtgen.generate(5,temperature=1,prefix='computer')