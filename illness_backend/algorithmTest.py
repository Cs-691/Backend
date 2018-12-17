
from flask import Flask, request, jsonify,json


from algorithm import Algorithm
from remedies import Remedies
from verification import Verification


            




x=[]
c=Verification()
x.append('chest_pain')
x.append('fast_heart_rate')
x.append('phlegm')
x.append('skin_rash')
x.append('continuous_sneezing')
print(c.predict(x))



