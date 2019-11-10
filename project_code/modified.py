import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import pickle
def rulesset(raw_list):
    pickle_in=open("fuzzy_model.pickle",'rb')
    system=pickle.load(pickle_in)

    i = raw_list[0]
    if i >= 40:
       system.input['Physics']= i
    else:
       system.input['Physics']= 40

    i = raw_list[1]
    if i >= 40:
       system.input['Maths']= i
    else:
       system.input['Maths']= 40

    i = raw_list[2]
    if i >= 40:
       system.input['Chemistry']= i
    else:
       system.input['Chemistry']= 40

    i = raw_list[3]
    if i >= 40:
       system.input['Biology']= i
    else:
       system.input['Biology']= 40

    i = raw_list[4]
    if i >= 40:
       system.input['Business']= i
    else:
       system.input['Business']= 40

    i = raw_list[5]
    if i >= 40:
       system.input['Accountancy']= i
    else:
       system.input['Accountancy']= 40

    i = raw_list[6]
    if i >= 40:
       system.input['PE']= i
    else:
       system.input['PE']= 40

    i = raw_list[7]
    if i >= 40:
       system.input['CS']= i
    else:
       system.input['CS']= 40

    i = raw_list[8]
    if i >= 40:
       system.input['History']= i
    else:
       system.input['History']= 40

    i = raw_list[9]
    if i >= 40:
       system.input['Geography']= i
    else:
       system.input['Geography']= 40

    i = raw_list[10]
    if i >= 40:
       system.input['Politics']= i
    else:
       system.input['Politics']= 40

    i = raw_list[11]
    if i >= 40:
       system.input['Economy']= i
    else:
       system.input['Economy']= 40

    i = raw_list[12]
    if i >= 40:
       system.input['Literature']= i
    else:
       system.input['Literature']= 40

    i = raw_list[13]
    if i >= 40:
       system.input['Language']= i
    else:
       system.input['Language']= 40

    i = raw_list[14]
    if i >= 40:
       system.input['Art']= i
    else:
       system.input['Art']= 40
    system.compute( )
    l=system.output
    return l