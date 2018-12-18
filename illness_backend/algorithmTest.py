
from flask import Flask, request, jsonify,json


from algorithm import Algorithm
from remedies import Remedies
from verification import Verification

import numpy as np

            




x=[]
c=Verification()
x.append('chest_pain')
x.append('fast_heart_rate')
x.append('phlegm')
x.append('skin_rash')
x.append('continuous_sneezing')
#print(c.predict(x))
print(np.random.uniform(0.8, 0.99))


