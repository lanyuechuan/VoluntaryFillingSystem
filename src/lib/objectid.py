"""用于分布式环境中生成24个字符组成的不重复ID
"""

import os
import re
import hashlib
import time

class ObjectID():
    """
    Generate object id. 
    """
    def __init__(self,id=None):
        g = globals()
        if not '__objectid_global' in g:
            obj = {}
            obj["timestamp"] = 0
            obj["host"] = self.getHostID()
            obj["counter"] = 0
            obj["pid"] = "{:0>4x}".format(os.getpid())[:4]
            g['__objectid_global'] = obj
        self._gobj = g['__objectid_global']
        if id:
            self.parser(id)
        else:
            self.new()
        
    def parser(self,id):
        """
        Parser id to objectid.
        """
        if not isinstance(id,str) or not re.match('^[0-9a-fA-F]{24}$',id):
            raise ValueError('objectid is 12 bytes hex  str.')
        self.timestamp = int(id[:8],16)
        self.host = id[8:14]
        self.pid = id[14:18]
        self.count = int(id[18:24],16)
        
    def new(self):
        """
        Generate new id.
        """
        old_time = self._gobj["timestamp"]        
        self.timestamp = int(time.time())
        
        if old_time == self.timestamp:
            self._gobj["counter"] += 1
        else:
            self._gobj["counter"] = 0
        self._gobj["timestamp"] = self.timestamp    
        self.count = self._gobj["counter"]
        self.host = self._gobj["host"]
        self.pid = self._gobj["pid"]
        return self.__str__()
        
            
    def getHostID(self):
        systype = os.name
        host = 'Unkwon hostname'
        if systype == 'nt':
            host = os.getenv('computername')
        elif systype == 'posix':
            h = os.popen('echo $HOSTNAME')
            try:
                host = h.read()
            finally:
                h.close()
        m = hashlib.sha256()
        m.update(host.encode('utf-8'))
        d = m.hexdigest()
        return d[:6]
     
    def __str__(self):
        return "{0:08x}{1}{2}{3:06x}".format(self.timestamp,self.host,self.pid,self.count)


def create_objectid():
    return str(ObjectID())        
    