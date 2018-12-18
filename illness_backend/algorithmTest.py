
from flask import Flask, request, jsonify,json


from algorithm import Algorithm
from remedies import Remedies
from verification import Verification

import numpy as np

            




x=[]
c=Verification()
x.append('spinning_movements')
x.append('loss_of_balance')
x.append('unsteadiness')
x.append('nausea')
#x.append('continuous_sneezing')
print(c.predict(x))
print(np.random.uniform(0.8, 0.99))


