#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 07:48:19 2018

@author: fabien
"""
from IPython.display import display, Math, Latex, clear_output
import  random
import matplotlib.pyplot as plt
import fractions
import numpy as np

def input_coord(point):
    """récupère un tuple (x;y) contenant les coordonnées d'un point dont le 
    nom est passé en argument"""
    coord_txt=input("Donnez des coordonnées au point {} : ".format(point))
    coord_txt=coord_txt.replace("(","").replace(")","").replace(" ","")
    try :
        return tuple([int(i) for i in coord_txt.split(";")])
    except ValueError:
        print("Les valeurs saisies ne sont pas entières, on obtient donc des float")
        try :
            return tuple([float(i) for i in coord_txt.split(";")])
        except :
            print("unable to convert data to float")
    except :
        print("something wrong happened...")
        
def Trace_droite(xA,yA,xB,yB,place=True):
    fig=plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    minx,maxx=int(min(xA,xB,0)-2),int(max(xA,xB,0)+2)
    
    #a=fractions.Fraction(yB-yA,xB-xA)
    #b=yB-a*xB
    #miny,maxy=int(a*minx+b),int(a*maxx+b)+1
    miny,maxy=int(min(yA,yB,0)-2),int(max(yA,yB,0)+2)
    
    plt.gca().set_xlim(minx,maxx)
    plt.gca().set_ylim(miny,maxy)
    plt.xticks(np.arange(minx,maxx,1))
    plt.yticks(np.arange(miny,maxy,1))
    ax.grid(color='r', linestyle='-', linewidth=2)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    if xA!=xB :
        a=fractions.Fraction(yB-yA,xB-xA)
        b=yB-a*xB
        plt.plot([minx,maxx],[a*minx+b,a*maxx+b], 'r-', lw=2)
    else :
        plt.plot([xA,xA],[miny,maxy], 'r-', lw=2)
    
    if place :
        plt.plot([xA,xB], [yA,yB], 'ro')
        plt.text (xB, yB+0.5, "B" )
    else :
        plt.plot(xA,yA,'ro')
    plt.text (xA, yA+0.5, "A" ) 
    
     
    plt.show()    
        
def Exemples_calculs():
    """Lance plusieurs exemples de calculs de coefficients directeurs"""
    while True :
        (xA,yA)=input_coord("A")
        while True :
            (xB,yB)=input_coord("B")
            if xB!=xA or yB!=yA :
                break
            else :
                display("Il faut deux points distincts pour faire une droite ! Recommencez !")

        intro=Latex("""Nous allons calculer le coefficient directeur de la droite (AB) avec 
                A( {} ; {} ) et B( {} ; {} )""".format(xA,yA,xB,yB))
        if xA==xB :
            
            calcul=Latex("""Les droites parallèles à l'axe des ordonnées n'ont pas de coefficient directeur !
                    Il faut donc que vos points n'aient pas la même abscisse :""")
        else :    
            frac=fractions.Fraction((yB-yA),(xB-xA))
            if frac==int(frac): 
                frac=str(int(frac))
            else :
                frac="\dfrac{{{numerator}}}{{{denominator}}}".format(numerator=frac.numerator,denominator=frac.denominator)
            calcul=Math("m= \dfrac{{y_B-y_A}}{{x_B-x_A}}= \dfrac{{{yB}-{yA}}}{{{xB}-{xA}}}= \dfrac{{{yByA}}}{{{xBxA}}}={frac}"
                                     .format(xA=xA,yA=yA,xB=xB,yB=yB,yByA=yB-yA,xBxA=xB-xA,frac=frac))
        Trace_droite(xA,yA,xB,yB)    
        display(intro,calcul)
        s=input("Voulez-vous recommencer ?(o/n)")
        if s.lower() in ['n','non','no'] :
            break
        else :
            clear_output()

def _Trouve_Coeff(totalquestion,taux,trace=True):
    score=0
    while (score/totalquestion)<taux :
        nbquestion=0
        while nbquestion<totalquestion :
            xA,yA=random.randint(-10,10),random.randint(-10,10)
            while True :
                xB,yB=random.randint(-10,10),random.randint(-10,10)
                if xA!=xB: break
            display(Latex("""Nombre de questions : {quest}
            Score :{sco:.0%}""".format(quest=nbquestion,sco=score/totalquestion)))
            if trace : Trace_droite(xA,yA,xB,yB)
            display(Latex(" Déterminer le coefficient directeur de la droite (AB) avec A({xA};{yA}) et B({xB};{yB}) :".format(xA=xA,yA=yA,xB=xB,yB=yB)))
            m=fractions.Fraction(input("Le coefficient directeur :"))
            
            gr=fractions.Fraction((yB-yA),(xB-xA))
            
            if m==gr :
                score=score+1
                display(Latex("Bravo !"))
            else :
                display(Latex("Raté ! La bonne réponse  était {}".format(gr)))
            if (nbquestion<totalquestion-1) :
                s=input("Continuer ?")
                clear_output()
            elif score>=taux :
                display(Latex("Bravo ! Votre score est de {:.0%}.Vous pouvez passer à l'exercice suivant !".format(score/totalquestion)))
            nbquestion=nbquestion+1
        if score/totalquestion<taux :
            display(Latex("Votre score de {:.0%} est insuffisant ! Veuillez recommencer !"
                .format(score/totalquestion)))
        
    

def Trouve_Coeff_ES1():
    _Trouve_Coeff(10,0.8)
def Trouve_Coeff_ES2():
    _Trouve_Coeff(5,0.8,trace=False)
    
def Exo_point(totalquestion, taux,trace=True):
    score=0
    while score/totalquestion<taux :
        nbquestion=0
        while nbquestion<totalquestion :
            xA,yA=random.randint(-10,10),random.randint(-10,10)
            while True :
                xB,yB=random.randint(-10,10),random.randint(-10,10)
                if xA!=xB: break
            try :
                a=fractions.Fraction((yB-yA),(xB-xA))
                b=yB-a*xB
            except :
                pass
            display(Latex("Score :{:.0%}".format(score/totalquestion)))
            if trace :Trace_droite(xA,yA,xB,yB,place=False)
            display(Latex("Déterminer les coordonnées d'un point B de cette droite sachant que le point A a pour coordonnées"+
                          "({xA};{yA}) et que le coefficient directeur de cette droite est {c}"
                          .format(xA=xA,yA=yA,c=fractions.Fraction(yB-yA,xB-xA))))
            repx,repy=input_coord("Donnez les coordonnées du point B :")
            if repy==a*repx+b :
                score=score+1
                display(Latex("Bravo !"))
            else :
                display(Latex("Raté ! Une bonne réponse  était B({};{})".format(xB,yB)))
            if (nbquestion<totalquestion-1) :
                s=input("Continuer ?")
                clear_output()
            elif score>=taux :
                display(Latex("Bravo ! Votre score est de {:.0%}.Vous pouvez passer à l'exercice suivant !".format(score/totalquestion)))
            nbquestion=nbquestion+1
        if score/totalquestion<taux :
            display(Latex("Votre score de {:.0%} est insuffisant ! Veuillez recommencer !"
                .format(score/totalquestion)))
        
                
                
            
        
def Exo_point_ES1() :
    Exo_point(10,0.8)
def Exo_point_ES2() :
    Exo_point(10,0.8,trace=False)
