

class Remedies():
    remedies = None
    
    def getRemedies(self,illness):
        print(illness)
        
        if illness in self.remedies:
            return self.remedies[illness]
        else:
             return self.remedies['gerd']
        
    def __init__(self):
        
        self.remedies = {};
        
        
       
        self.remedies['gerd'] = ("this is a very GERD"
      "long string too"
      "for sure ..."
     )
        
        self.remedies['allergy'] = ("this is a very Alleery"
      "long string too"
      "for sure ..."
     )
        
     