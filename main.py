from ZoriFileReader.ZoriMetroFileReader import ZoriMetroFileReader


def zoriMetroDriver():
    zoriMetroFileReader = ZoriMetroFileReader()
    fileHandle = zoriMetroFileReader.getFileHandle()
    dataDict = zoriMetroFileReader.getDataDictFromFile(fileHandle)
    print(dataDict)


def main():
    zoriMetroDriver()


main()
