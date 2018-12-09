from flask import Flask, request, jsonify,json

class Response():
    
    illness=""
    remedy=""
    probability=1
    
    def __init__(self,illness,remedy,probability):
          self.illness=illness
          self.remedy=remedy
          self.probability=probability
    
    def __repr__(self):
        return f"Illness('{self.illness}', '{self.probability})"
          
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)