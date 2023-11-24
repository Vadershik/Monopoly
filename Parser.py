import random


class Parser:

    tasks = []


    def __init__(self):
        self.readFromFile()

    def readFromFile(self):
        try:
            file = open('tasks.txt')
        except IOError:
            print('FileError: File tasks.txt is not exists in directory')
        else:
            with open('tasks.txt', 'r') as file:
                self.tasks = file.readlines()
        return self.tasks

    def getTask(self):
        return random.choice(self.tasks)

