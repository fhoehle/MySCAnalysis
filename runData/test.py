class test(object):
  def __init__(self,l):
    self.listR = l
  def listOfMins(self):
    self.listR.sort(key=lambda r:r.min)
    self.mins=list(set([ r.min for r in self.listR]))
    self.openRanges = [r for r in self.listR if r.min==self.mins[0]]
    for r in self.openRanges:
      self.listR.remove(r)
    #print ([r.__dict__ for r in self.openRanges])
    self.maxs=[ r.max for r in self.listR];self.maxs.sort();self.maxs=list(set(self.maxs))
    self.lowerLimit=self.mins.pop(0)
    self.borders=list(set(self.mins+self.maxs));self.borders.sort();lastLower=None
    while len(self.borders) != 0:
      print "test ",self.borders[0],",",self.mins[0],",",self.maxs[0]
      if self.borders[0] == self.mins[0]:
        print "lowerLimit  ",self.lowerLimit," min -1 ",self.mins[0] - 1
        for r in self.listR:
          if r.min == self.borders[0]:
            self.openRanges.append(r)
            self.listR.remove(r) 
      elif self.borders[0] == self.maxs[0]:
        print "lowerLimit  ",self.lowerLimit," max ",self.maxs[0]
        for r in self.openRanges:
	  if r.max ==  self.borders[0]:
	    self.openRanges.remove(r)
            self.lowerLimit = min( self.openRanges, key=lambda r:r.min).min 
          
        print "not"
      else:
        print "something failed"
      print "lowerLimit ",self.lowerLimit
      self.borders.pop(0)
class runRange(object):
  def __init__(self,min,max):
    self.min=min;self.max=max
r1 = runRange(165209, 178419)
r2 = runRange(167914, 999999)
runRanges = [r1,r2]
t=test(runRanges)
t.listOfMins()

