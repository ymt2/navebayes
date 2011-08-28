#! /usr/bin/python
# -*- coding: utf-8 -*-

import MeCab

class Corpus:

    def __init__(self, wordclass=range(0,69), appear=0):
        self.m = MeCab.Tagger('-Ochasen')
        self.corpusnum = 0
        self.cdic = {}
        self.wordclass = set(wordclass)
        self.appear = appear
        self.nouns = 36 # All 0..68
        self.noune = 68
        
    def _setWordnode(self, corpus):
        try:
            return self.m.parseToNode(corpus)
        except:
            raise NavebayesError()
    
    def _setWordcount(self, node):
        t = ''
        node = node.next
        classes = set(range(self.nouns, self.noune)).union(self.wordclass)
        while node.next:
            if node.posid in classes:
                t = t + node.surface.lower()
            else:
                if '' != t:
                    self.cdic.setdefault(t, 0)
                    self.cdic[t] += 1
                    t = ''
            node = node.next

    def setCorpus(self, corpus):
        self.corpusnum += 1
        node = self._setWordnode(corpus)
        self._setWordcount(node)

    def getWordcountDic(self):
	return self.cdic
	
    def getWordcount(self, word):
        return self.cdic.setdefault(word, 0)
    
    def getCorpusnum(self):
        return self.corpusnum

if __name__ == '__main__':
    pass
