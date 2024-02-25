class Logger:
    def __init__(self):
        self.dict = {}
        print(self.dict)


    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dict.keys():
            self.dict[message] = timestamp + 10
            return True
        elif message in self.dict.keys() and self.dict[message] <= timestamp:
            self.dict[message] = timestamp + 10
            return True
        else:
            return False

logger  = Logger()
print(logger.shouldPrintMessage(0,"A"))
print(logger.shouldPrintMessage(0, "B"))
print(logger.shouldPrintMessage(0, "C"))
print(logger.shouldPrintMessage(0, "A"))
print(logger.shouldPrintMessage(0, "B"))
print(logger.shouldPrintMessage(0, "C"))
print(logger.shouldPrintMessage(11, "A"))
print(logger.shouldPrintMessage(11, "B"))
print(logger.shouldPrintMessage(11, "C"))
print(logger.shouldPrintMessage(11, "A"))