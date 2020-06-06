# Define an iterator-type interface to get log messages?


class LogFetcher:
    def __init__(self, sourceType, sourceLocation):
        self.sourceType = sourceType
        self.sourceLocation = sourceLocation

        if(sourceLocation == 'local'):
            # initialize scanner obj to begin reading file upon initialization of class to simplify getNext() method
            self.fileObj = open(sourceLocation)
    
    def getNext(self):
        if sourceType == 'network':
            pass

        elif sourceType == 'local':
            return self.fileObj.readline()

