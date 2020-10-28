
import json

with open('settings.json') as f:
    data = json.load(f)

def getPortNo():
    return (data["portdetails"]["portno"])
def getBrate():
    return (data["portdetails"]["brate"])
def getDataBits():
    return (data["portdetails"]["data_bits"])
def getParity():
    return (data["portdetails"]["parity"])
def getStopBits():
    return (data["portdetails"]["stop_bits"])
def getTimeout():
    return (data["portdetails"]["timeout"])
def getFolderURL():
    return (data["CodeFiles"]["FolderURL"])
