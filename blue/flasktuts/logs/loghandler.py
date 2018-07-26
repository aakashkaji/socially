""" This file is used for logging purpose"""

import datetime as dt
import logging

""""
Example formate of generated bson document
"""
try:
    from pymongo import MongoClient as Connection
except ImportError:
    from pymongo import Connection

from pymongo.collection import Collection
from pymongo.errors import OperationFailure,PyMongoError
import pymongo

"""
{

format example
'thread':,
'thread_name':'',
'level':'ERROR',
'timestamp': ,
'message':'',
'module':'',
'file_name': '',
'linenumber':int,
'method': '',
'logger_name':'',
'exception':{}
}

"""
_connection = None

class MongoFormatter(logging.Formatter):

    DEFAULT_PROPERTIES = logging.LogRecord(
        '', '', '', '', '', '', '', '').__dict__.keys()
    def format(self, record):
        """Formats LogRecord into python dictionary."""

        # Standard document

        document = {
            'timestamp': dt.datetime.utcnow(),
            'level': record.levelname,
            'thread': record.thread,
            'threadName': record.thread_name,
            'message': record.getMessage(),
            'loggerName': record.name,
            'fileName': record.pathname,
            'module': record.module,
            'method': record.func_name,
            'lineNumber': record.lineno
        }


mongoFormatter = MongoFormatter()

print(mongoFormatter.DEFAULT_PROPERTIES)