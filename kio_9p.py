#!/usr/bin/python2 
# -*- coding: utf-8 -*-

''' generic functions '''
''' TODO: remove useless imports '''
import os
import site
import sys
import socket
import stat
import os.path
import copy
import time
import pwd
import grp
import inspect
import getopt
import getpass
import code
import readline
import atexit
import fnmatch

''' py9p module '''
import py9p

''' Qt and KDE bindings '''
from PyQt4.QtCore import QByteArray, QDataStream, QFile, QFileInfo, QString, \
               QStringList, IO_ReadOnly, IO_WriteOnly, SIGNAL
from PyKDE4.kio import KIO
from PyKDE4.kdecore import KURL
from pyKDE4.dnsd import publicservice, remoteservice



''' some sort of fail-safe measure '''
class OperationFailed(py9p.Error): pass

''' __init__ '''    
class SlaveClass(KIO.SlaveBase):

    def __init__(self, pool, app):
    
        KIO.SlaveBase.__init__(self, 9p, pool, app)

''' parsing url in utf-8 '''        
def parse_url(self, url):
    
        file_path = unicode(url.path())        
        
''' setHost'''        
def setHost(self, host, port, user, passwd):

    if unicode(host) != u"":
    
        self.error(KIO.ERR_MALFORMED_URL, host)
        return
        
'''stat'''        
def stat(self, url):

    try:
    
        name, obj = self.find_object_from_url(url)
    
    except OperationFailed:
    
        self.error(KIO.ERR_DOES_NOT_EXIST, url.path())
        return
entry = self.build_entry(name, obj)

if entry != []:

    self.statEntry(entry)
    self.finished()

else:

    self.error(KIO.ERR_DOES_NOT_EXIST, url.path())
    
