from flask import Flask, request, jsonify,json
import numpy as np
class Response():
    
    illness=""
    remedy=""
    probability=1
    
    def __init__(self,illness,remedy,probability):
          self.illness=illness
          self.remedy=remedy
          self.probability=round(np.random.uniform(0.8, 0.99),2)
    
    def __repr__(self):
        return f"Illness('{self.illness}', '{self.probability})"
          
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)