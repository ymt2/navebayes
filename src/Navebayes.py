#! /usr/bin/python
# -*- coding: utf-8 -*-

import Corpus

class Navebayes:
    
    def __init__(self, target, good, bad, bias=2):
        self.target = target
        self.good = good
        self.bad = bad
        self.bias = bias
        self.pdefault = 0.4
        self.pmax = 0.99
        self.pmin = 0.01
        self.wnum = 15
        self.pdic = {}
        
    def _setWordprobability(self):
        revise = lambda p: min(max(p, self.pmin), self.pmax)
        wc = lambda w: self.good.getWordcount(w)*2 + self.bad.getWordcount(w)
        gp = lambda w: float(self.good.getWordcount(w)*2) / float(self.good.getCorpusnum())
        bp = lambda w: float(self.bad.getWordcount(w)) / float(self.bad.getCorpusnum())
        for w, n in self.target.cdic.items():
            if 5 < wc(w):
                self.pdic[w] = revise(bp(w) / (gp(w) + bp(w)))
            else:
                self.pdic[w] = self.pdefault
                
    def _getPeculiarWordsProbability(self):
        import math
        wl = [w for w in sorted(self.pdic.items(), key=lambda x: math.fabs(0.5-x[1]))]
        return wl[0:self.wnum]

    def getProbability(self):
        self._setWordprobability()
        wl = self._getPeculiarWordsProbability()
        tp = [p for w, p in wl]
        tip = [float(1-p) for w, p in wl]
        product = lambda l: reduce(lambda x, y: x*y, l)
        return float(product(tp)) / (float(product(tp)) + float(product(tip)))
    
    def getWordprobabilityDic(self):
	self._setWordprobability()
        return self.pdic
    
    def getWordprobability(self, word):
	self._setWordprobability()
        return self.pdic[word]
            
class NavebayesError(Exception):
    
    """SomeError"""
    pass

if __name__ == '__main__':
    pass
