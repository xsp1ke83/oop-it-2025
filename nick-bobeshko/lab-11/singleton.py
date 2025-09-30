class Logger:
    __instance = None
    
    def __new__(cls, filename, mode="a"):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, filename, mode="a"):
        self.filename = filename
        self.__open_mode = mode
        self.__file_handler = None
        self.__open_file()
    
    def __open_file(self):
        if (self.__file_handler is None):
            self.__file_handler = open(self.filename, self.__open_mode)
            print(f"File {self.filename} is opened.")
        else:
            print("File is already open")

    def write_log(self, message):
        self.__file_handler.write(message + "\n")
        self.__file_handler.flush()

    def close_handler(self):
        if self.__file_handler:
            self.__file_handler.close()
            self.__file_handler = None
            print(f"File {self.filename} is closed.")
        else:
            print("File is already closed.")


logger1 = Logger("logger.log", "a")
logger2 = Logger("logger.log", "a")
print(logger1 is logger2)  # True  - The same instance

logger1.write_log("new log...")

logger1.close_handler()

# logger1.write_log(99)  error


