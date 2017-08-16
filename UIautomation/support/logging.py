# -*-coding=utf-8-*-
import time


class Log(object):

    OutFilePath=r'D:\UI\PythonUIautomation\TestResult'
    LogTime=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())

    @staticmethod
    def LogAction(detial):
        Log.__AppendLogFile(detial)

    @staticmethod
    def LogException(message):
        Log.__AppendLogFile(message)

    @staticmethod
    def __AppendLogFile(value):
        fileName=Log.LogTime+'-log.txt'
        fileName=Log.OutFilePath+'\\'+fileName
        with(open(fileName,'wb'))as fw:
            fw.write(Log.LogTime+':'+value)

if __name__=='__main__':
    Log.__AppendLogFile('test')



