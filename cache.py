from ZODB.FileStorage import FileStorage
import ZODB as zodb
from persistent import Persistent
import transaction as zodb_transact


class CacheDB(object):
    """
    A caching ZODB
    """
    def __init__(self, filename):
        filename = str(filename)
        self.__storage = FileStorage(filename)
        self.__db = zodb.DB(self.__storage)
        self.__connection = self.__db.open()

    @property
    def storage(self):
        return self.__storage

    @property
    def db(self):
        return self.__db

    @property
    def connection(self):
        return self.__connection

    @property
    def root(self):
        return self.connection.root

    def commit(self):
        zodb_transact.commit()

    def close(self):
        self.__connection.close()
        self.__db.close()
        self.__storage.close()
        self.__connection = None
        self.__db = None
        self.__storage = None



class CachedItem(Persistent):
    def __init__(self, key, obj, ttl=None):
        self.key = self.key
        self.obj = self.obj
        self.ttl = ttl

