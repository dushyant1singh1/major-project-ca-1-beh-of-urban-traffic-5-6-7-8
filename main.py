#importing library

import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# adding antecedent function
Physics = ctrl.Antecedent(np.arange(0,101,1),'Physics')
Maths = ctrl.Antecedent(np.arange(0,101,1),'Maths')
Chemistry = ctrl.Antecedent(np.arange(0,101,1),'Chemistry')
Biology = ctrl.Antecedent(np.arange(0,101,1),'Biology')


#using trapmf(Trapizoidal membership Function)
Physics['Excellent'] = fuzzy.trapmf(Physics.universe,[70,85,100,100])
Physics['Good'] = fuzzy.trapmf(Physics.universe,[55,70,75,75])
Physics['Average'] = fuzzy.trapmf(Physics.universe,[38,55,60,60])
Physics['Poor'] = fuzzy.trapmf(Physics.universe,[25,30,40,40])
Physics['Very_Poor'] = fuzzy.trapmf(Physics.universe,[0,15,25,25])

Maths['Excellent'] = fuzzy.trapmf(Maths.universe,[70,85,100,100])
Maths['Good'] = fuzzy.trapmf(Maths.universe,[55,70,75,75])
Maths['Average'] = fuzzy.trapmf(Maths.universe,[38,55,60,60])
Maths['Poor'] = fuzzy.trapmf(Maths.universe,[25,30,40,40])
Maths['Very_Poor'] = fuzzy.trapmf(Maths.universe,[0,15,25,25])

Chemistry['Excellent'] = fuzzy.trapmf(Chemistry.universe,[70,85,100,100])
Chemistry['Good'] = fuzzy.trapmf(Chemistry.universe,[55,70,75,75])
Chemistry['Average'] = fuzzy.trapmf(Chemistry.universe,[38,55,60,60])
Chemistry['Poor'] = fuzzy.trapmf(Chemistry.universe,[25,30,40,40])
Chemistry['Very_Poor'] = fuzzy.trapmf(Chemistry.universe,[0,15,25,25])

Biology['Excellent'] = fuzzy.trapmf(Biology.universe,[70,85,100,100])
Biology['Good'] = fuzzy.trapmf(Biology.universe,[55,70,75,75])
Biology['Average'] = fuzzy.trapmf(Biology.universe,[38,55,60,60])
Biology['Poor'] = fuzzy.trapmf(Biology.universe,[25,30,40,40])
Biology['Very_Poor'] = fuzzy.trapmf(Biology.universe,[0,15,25,25])


#Adding Profession and their consequrnt function
Engineering = ctrl.Consequent(np.arange(0,1.1,0.1),'Engineering')
Medicine = ctrl.Consequent(np.arange(0,1.1,0.1),'Medicine')
Management = ctrl.Consequent(np.arange(0,1.1,0.1),'Management')
Hospitality = ctrl.Consequent(np.arange(0,1.1,0.1),'Hospitality')
Chief = ctrl.Consequent(np.arange(0,1.1,0.1),'Chief')
Teacher = ctrl.Consequent(np.arange(0,1.1,0.1),'Teacher')
Researcher = ctrl.Consequent(np.arange(0,1.1,0.1),'Researcher')
Architect = ctrl.Consequent(np.arange(0,1.1,0.1),'Architect')
Artist = ctrl.Consequent(np.arange(0,1.1,0.1),'Artist')
Athlete = ctrl.Consequent(np.arange(0,1.1,0.1),'Athlete')
