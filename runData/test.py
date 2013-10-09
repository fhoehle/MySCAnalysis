class test(object):
  def __init__(self,l):
    from copy import deepcopy
    self.listR = deepcopy(l)
  def listOfMins(self):
    self.listR.sort(key=lambda r:r.min)
    self.mins=list(set([ r.min for r in self.listR]));self.mins.sort()
    self.maxs=list(set([ r.max for r in self.listR]));self.maxs.sort();
    self.openRanges = [r for r in self.listR if r.min==self.mins[0]]
    for r in self.openRanges:
      self.listR.remove(r)
    #print ([r.__dict__ for r in self.openRanges])
    print "maxs ",self.maxs
    print "mins ",self.mins
    self.lowerLimit=self.mins.pop(0)
    self.borders=list(set(self.mins+self.maxs));self.borders.sort();lastLower=None
    self.ranges=[]
    print "borders ",self.borders
    while len(self.borders) != 0:
      print "test ",self.borders[0],",",self.mins,",",self.maxs," lowerLimit ",self.lowerLimit
      if (len(self.mins) and self.borders[0] == self.mins[0]) or (self.borders[0] == self.maxs[0]):
        if len(self.mins) and self.borders[0] == self.mins[0]:
          print "lowerLimit  ",self.lowerLimit," min -1 ",self.mins[0] - 1
          for r in self.listR:
            if r.min == self.borders[0]:
              self.openRanges.append(r)
              self.listR.remove(r) 
          self.ranges.append([self.lowerLimit,self.mins[0] - 1])
          self.lowerLimit = int(self.mins[0])
          self.mins.remove(self.mins[0])
        if self.borders[0] == self.maxs[0]:
          print "lowerLimit  ",self.lowerLimit," max ",self.maxs[0]
          for r in self.openRanges:
	    if r.max ==  self.borders[0]:
	      self.openRanges.remove(r)
              #self.lowerLimit = min( self.openRanges, key=lambda r:r.min).min 
          self.ranges.append([self.lowerLimit,self.maxs[0]])  
          self.lowerLimit= self.maxs[0]+1
          if len(self.openRanges) == 0 and len(self.mins):
            self.lowerLimit =  self.mins[0];self.mins.remove(self.mins[0])
          self.maxs.remove(self.maxs[0])
          print "not"
      else:
        print "something failed"
      print "lowerLimit ",self.lowerLimit
      self.borders.pop(0)
class runRange(object):
  def __init__(self,min,max):
    self.min=min;self.max=max
import copy
r1 = runRange(165, 178)
r2 = runRange(180, 190)
r3 = runRange(167, 182)
r4 = runRange(200, 220)
r5 = runRange(182, 183)
runRanges = [r1,r2,r3,r4,r5]
t=test(runRanges)
t.listOfMins()

