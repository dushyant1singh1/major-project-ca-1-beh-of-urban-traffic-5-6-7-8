from django.shortcuts import render
from django.http import HttpResponse
import operator
import numpy as np
from project_code import hello
import math

def home(request):
    
    return render (request,'home.html')

def implimentation(request):
    # physics=list(request.GET['h_physics','h_math','h_chemistry','h_biology','h_business','h_accountancy','h_pe','h_cs','h_history','h_georaphy',
    #                             'h_politics','h_economy','h_literature','h_language','h_art'])
    physics=request.GET['h_physics']
    math=request.GET['h_math']
    chemistry=request.GET['h_chemistry']
    biology=request.GET['h_biology']
    business=request.GET['h_business']
    accountancy=request.GET['h_accountancy']
    pe=request.GET['h_pe']
    cs=request.GET['h_cs']
    history=request.GET['h_history']
    geography=request.GET['h_geography']
    politics=request.GET['h_politics']
    economy=request.GET['h_economy']
    literature=request.GET['h_literature']
    language=request.GET['h_language']
    art=request.GET['h_art']
    
    all_subject=[int(physics),int(math),int(chemistry),int(biology),int(business),int(accountancy),
        int(pe),int(cs),int(history),int(geography),int(politics),int(economy),int(literature),int(language),int(art)]
    diction=(hello.rulesset(all_subject))
    diction=dict(diction)
    for key in diction:
        diction[key]=int(diction[key]*100)
    return render(request,'showresult.html',{"data":diction})

