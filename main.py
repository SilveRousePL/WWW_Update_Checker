import urllib.request
import time
import os


url = "https://kpz.pwr.edu.pl/"
file = "kpz"
refresh_time = 5


def saveFile(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()


def loadFile(filename):
    file = open(filename, 'r')
    try:
        result = file.read()
    finally:
        file.close()
    return result


def fileExist(filename):
    if os.path.isfile(filename):
        return True
    return False


def downloadSite(url):
    request = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    htmlSource = response.read()
    return htmlSource


def updateAction():
    print(time.time(), ": ZAKTUALIZOWANO!!!")


def noAction():
    print(time.time(), ": Brak aktualizacji!")


if not fileExist(file):
    saveFile(file, "")
while True:
    data_file = loadFile(file)
    data_www = downloadSite(url).decode("utf-8")
    print(data_file)
    print("\n")
    print(data_www)
    if data_file != data_www:
        saveFile(file, data_www)
        updateAction()
    else:
        noAction()

    # print(htmlSource)
    time.sleep(refresh_time)
