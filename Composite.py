#!/usr/bin/python
#coding:utf8

"""
Composite
"""

class Component:
    def __init__(self,strName):
        self.m_strName = strName
    def Add(self,com):
        pass
    def Display(self,nDepth):
        pass

class Leaf(Component):
    def Add(self,com):
        print "leaf can't add"
    def Display(self,nDepth):
        strtemp = "-" * nDepth
        strtemp=strtemp+self.m_strName
        print strtemp

class Composite(Component):
    def __init__(self,strName):
        self.m_strName = strName
        self.c = []
    def Add(self,com):
        self.c.append(com)
    def Display(self,nDepth):
        strtemp = "-"*nDepth
        strtemp=strtemp+self.m_strName
        print strtemp
        for com in self.c:
            com.Display(nDepth+2)

if __name__ == "__main__":
    p = Composite("Wong")
    p.Add(Leaf("Lee"))
    p.Add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.Add(Leaf("San"))
    p.Add(p1)
    p.Display(1);