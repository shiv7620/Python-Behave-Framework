import datetime
from pprint import pprint

import enum

class Status(enum.Enum):
    Pass = "Pass"
    Fail = "Fail"
    Info = "Info"
    WARN = "WARN"
    ERRO = "ERRO"

def ConsolePrint(status,*arg):

    if not isinstance(status, Status):
        raise TypeError('Invalid status: status must be an instance of Status Enum')

    print(datetime.datetime.now(), " | ",  status.value, " | ", *arg)