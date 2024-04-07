from OutputHandler.OutputHandler import OutputHandler


class FileOutputHandler(OutputHandler):
    def __init__(self, filename: str):
        self.filename = filename

    def outputListData(self, listData: list):
        file = open(self.filename, "w")
        for lst in listData:
            if type(lst) is list:
                for index, val in enumerate(lst):
                    file.write(val)
                    if index < len(lst) - 1:
                        file.write("\t")
                file.write("\n")
                continue
            file.write(str(lst) + "\n")
        file.close()
