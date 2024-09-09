import pygame
from collections import deque

class TextEditor:
    def __init__(self):
        self.text = deque()
        self.cursor_location = None
        
    def insert(self, char: str):
        self.text.append(char)
        
    