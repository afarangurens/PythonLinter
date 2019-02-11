import sys
from antlr4 import *
from Python3Parser import Python3Parser
from Python3Listener import Python3Listener

class TestContextListener(Python3Listener):
    def __init__(self):
        print("initializing context test with listener...")

    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        print("classdef rule : ", ctx.NAME())

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        print("classdef rule done...")


