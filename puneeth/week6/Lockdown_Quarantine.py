#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:15:40 2022

@author: puneeth

SIRS Model with Lockdown and Quarantine 

Infected compartment is divided into 2 quarantined, with prob q, and unquarantined, with prob 1-q, where q=1 means 
even the asymptomatics are quarantined (implying high and accurate testing) and q=0 means no one is quarantining. 

Quarantined individuals cannot cause new infections 

Lockdown is implemented as a period of zero infection rate. Two lockdown regimes are explored. 1. Single long lockdown 2. Three shorter ones but with breaks

Questions Answered:
    1. How long does the single lockdown have to be to eradicate the infection as a function of starting number of infections?
    2. How long does the multiple shorter lockdowns have to be to eradicate the infection as a function of starting number of infections?
    3. How does quarantine probability affect these times? 
    
See the Summary on Github for further details.
"""

import distributions as dst 
import matplotlib.pyplot as plt
import random as rnd



#SIRS Model with single lockdown
class SIRS_SLQ: 
    def __init__(self,b,v,u,g,w,q,ld_time,S,I,R):
        self.b = b #birth rate S += 1 
        self.v = v #infection rate S -> I
        self.u = u #death rate due to infection I -= 1 
        self.g = g #recovery rate I -> R
        self.q = q #quarantine probabiliy I -> Q
        self.w = w #immunity loss rate R -> S 
        self.ld_time = ld_time
        
        self.S_start = S #number of susceptible 
        self.uQ_start = I #number of unquarantined infected
        self.Q_start = 0 #number of quarantined infected 
        self.R_start = R #number of recoverd
    
    def path(self, time=30):
        t = 0
        S = self.S_start 
        Q = self.Q_start 
        uQ = self.uQ_start
        R = self.R_start
        I = Q + uQ
        D = 0 #number of deceased
        
        
        pop_size = {'t':[t], 's':[S], 'i':[I] , 'q':[Q], 'uq':[uQ], 'r':[R], 'd':[D]}
        
        exp_dst = dst.exponential(1.0) #Just initializing here. The rate is changed when required

        while I > 0:         
            #Decide if in lockdown or not. 
            if t < self.ld_time: 
                v_act = 0
            else: 
                v_act = self.v
                
            #Rates of different events. See below for what each rate is. 
            event_rates = [self.b*S, v_act*self.q*S*uQ, v_act*(1-self.q)*S*uQ, self.u*Q, self.u*uQ, self.g*Q, self.g*uQ,self.w*R]
            event_rate = float(sum(event_rates))
            
            #stop if no events are to happen 
            if event_rate == 0  : 
                pop_size['t'] += [t]
                pop_size['s'] += [ S ]
                pop_size['i'] += [ I ]
                pop_size['q'] += [ Q ]
                pop_size['uq'] += [ uQ ]
                pop_size['r'] += [ R ]
                pop_size['d'] += [ D ]
                break 
                
            #Deciding the time for the next event to happen 
            exp_dst.rate = event_rate
            t_diff = exp_dst.random_list(1)[0]
            t += t_diff
            pop_size['t'] += [t]
            
            #Deciding which event occurs
            event = rnd.choices([0,11,12,21,22,31,32,4],event_rates)[0] 
            #0-birth, 11-infection but quarantined, 12-infection w/o quarantine
            #21-death due to infection of quarantined ind, 22-death due to infection of unquarantined ind 
            #31-recovery of quarantined ind, 32-recovery of unquarantined ind
            #4-loss of immunity
            if event == 0 : 
                S += 1 
            elif event == 11: 
                S -= 1 
                Q += 1 
            elif event == 12: 
                S -= 1 
                uQ += 1 
            elif event == 21: 
                Q -= 1
                D += 1 
            elif event == 22: 
                uQ -= 1
                D += 1 
            elif event == 31: 
                Q -= 1 
                R += 1 
            elif event == 32: 
                uQ -= 1 
                R += 1 
            elif event == 4: 
                R -= 1
                S += 1
            I = Q + uQ
                
            pop_size['s'] += [ S ]
            pop_size['i'] += [ I ]
            pop_size['q'] += [ Q ]
            pop_size['uq'] += [ uQ ]
            pop_size['r'] += [ R ]
            pop_size['d'] += [ D ]
            
        return pop_size 
    
    #Computing different metrics (refer to Summary on Github for details.)
    def metrics(self , sample=100, time=30): 
        P_list = [] 
        D_list = []
        Time_to_Erad_list = []
        Eradication = []
        for sam in range(sample): 
            pop_sam = self.path()
            tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
            P_list += [tot_size]
            D_list += [ pop_sam['d'][-1] ]
            Time_to_Erad_list += [ pop_sam['t'][-1] ] 
            if pop_sam['i'][-1] == 0 and tot_size > 10: 
                Eradication += [1]
            else :
                Eradication += [0]
        
        mean_size = dst.mean(P_list)
        mean_deaths = dst.mean(D_list)
        mean_erad_time = dst.mean(Time_to_Erad_list)
        eradication_prob = sum(Eradication)/float(len(Eradication))

        return [mean_size, mean_deaths, mean_erad_time, eradication_prob]
    
    #Computing critical lockdown time for the given paramters (Refer to summary on Github for details.)
    def critical_ldtime(self, sample = 100, threshold = 0.80): 
        ld_time_org = self.ld_time #So as to not change the default value in case the user want to use some other method for the instance they created.
        ld_ti = 0
        eradication_prob = 0
        while eradication_prob < threshold:
            ld_ti += 10 #We first jump 10 units at a time and then fine tune it in the next loop to reduce run time. 
            self.ld_time = ld_ti
            Eradication = []
            for sam in range(sample): 
                pop_sam = self.path()
                tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
                if pop_sam['i'][-1] == 0 and tot_size > 10: 
                    Eradication += [1]
                else :
                    Eradication += [0]
            eradication_prob = sum(Eradication)/float(len(Eradication))
            
        ld_ti -= 11
        eradication_prob = 0
        while eradication_prob < threshold:
            ld_ti += 1 #Fine tuning the previous value. 
            self.ld_time = ld_ti
            Eradication = []
            for sam in range(sample): 
                pop_sam = self.path()
                tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
                if pop_sam['i'][-1] == 0 and tot_size > 10: 
                    Eradication += [1]
                else :
                    Eradication += [0]
            eradication_prob = sum(Eradication)/float(len(Eradication))
        
        self.ld_time = ld_time_org #Reseting the default value. 
        return ld_ti
        

#SIRS Model with multiple lockdowns (Refer to Summary on Github for details.)
class SIRS_MLQ: 
    def __init__(self,b,v,u,g,w,q,ld_time,S,I,R):
        self.b = b #birth rate S += 1 
        self.v = v #infection rate S -> I
        self.u = u #death rate due to infection I -= 1 
        self.g = g #recovery rate I -> R
        self.q = q #quarantine probabiliy I -> Q
        self.w = w #immunity loss rate R -> S 
        self.ld_time = ld_time
        
        self.S_start = S #number of susceptible 
        self.uQ_start = I #number of unquarantined infected
        self.Q_start = 0 #number of quarantined infected 
        self.R_start = R #number of recoverd
    
    def path(self, time=30):
        t = 0
        S = self.S_start 
        Q = self.Q_start 
        uQ = self.uQ_start
        R = self.R_start
        I = Q + uQ
        D = 0 #number of deceased
        
        
        pop_size = {'t':[t], 's':[S], 'i':[I] , 'q':[Q], 'uq':[uQ], 'r':[R], 'd':[D]}
        
        exp_dst = dst.exponential(1.0) #Just initializing here. The rate is changed when required
        sld_time = self.ld_time/3.0 #Computing the time of one period of lockdown (Refer to Summary on Github)
        
        while I > 0:         
            #Decide if in lockdown or not. 
            if t < sld_time or ( t > 2*sld_time and t < 3*sld_time ) or  ( t > 4*sld_time and t < 5*sld_time ) : 
                v_act = 0
            else: 
                v_act = self.v
                
            #Compute the rates of different events. See below for what each rate refers to    
            event_rates = [self.b*S, v_act*self.q*S*uQ, v_act*(1-self.q)*S*uQ, self.u*Q, self.u*uQ, self.g*Q, self.g*uQ,self.w*R]
            event_rate = float(sum(event_rates))
            
            #stop if no events are to happen 
            if event_rate == 0  : 
                pop_size['t'] += [t]
                pop_size['s'] += [ S ]
                pop_size['i'] += [ I ]
                pop_size['q'] += [ Q ]
                pop_size['uq'] += [ uQ ]
                pop_size['r'] += [ R ]
                pop_size['d'] += [ D ]
                break 
                
            #Computing the time for the next event 
            exp_dst.rate = event_rate
            t_diff = exp_dst.random_list(1)[0]
            t += t_diff
            pop_size['t'] += [t]
            
            #Deciding which event occurs
            event = rnd.choices([0,11,12,21,22,31,32,4],event_rates)[0] 
            #0-birth, 11-infection but quarantined, 12-infection w/o quarantine
            #21-death due to infection of quarantined ind, 22-death due to infection of unquarantined ind 
            #31-recovery of quarantined ind, 32-recovery of unquarantined ind
            #4-loss of immunity
            if event == 0 : 
                S += 1 
            elif event == 11: 
                S -= 1 
                Q += 1 
            elif event == 12: 
                S -= 1 
                uQ += 1 
            elif event == 21: 
                Q -= 1
                D += 1 
            elif event == 22: 
                uQ -= 1
                D += 1 
            elif event == 31: 
                Q -= 1 
                R += 1 
            elif event == 32: 
                uQ -= 1 
                R += 1 
            elif event == 4: 
                R -= 1
                S += 1
            I = Q + uQ
                
            pop_size['s'] += [ S ]
            pop_size['i'] += [ I ]
            pop_size['q'] += [ Q ]
            pop_size['uq'] += [ uQ ]
            pop_size['r'] += [ R ]
            pop_size['d'] += [ D ]
            
        return pop_size 
    
    # See the corresponding methods SIRS_SLQ class and Summary on Github for documentation. 
    def metrics(self , sample=100, time=30): 
        P_list = [] 
        D_list = []
        Time_to_Erad_list = []
        Eradication = []
        for sam in range(sample): 
            pop_sam = self.path()
            tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
            P_list += [tot_size]
            D_list += [ pop_sam['d'][-1] ]
            Time_to_Erad_list += [ pop_sam['t'][-1] ] 
            if pop_sam['i'][-1] == 0 and tot_size > 10: 
                Eradication += [1]
            else :
                Eradication += [0]
        
        mean_size = dst.mean(P_list)
        mean_deaths = dst.mean(D_list)
        mean_erad_time = dst.mean(Time_to_Erad_list)
        eradication_prob = sum(Eradication)/float(len(Eradication))
        return [mean_size, mean_deaths, mean_erad_time, eradication_prob]
    
    def critical_ldtime(self, sample = 100, threshold = 0.80): 
        ld_time_org = self.ld_time
        ld_ti = 0
        eradication_prob = 0
        while eradication_prob < threshold:
            ld_ti += 10
            self.ld_time = ld_ti
            Eradication = []
            for sam in range(sample): 
                pop_sam = self.path()
                tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
                if pop_sam['i'][-1] == 0 and tot_size > 10: 
                    Eradication += [1]
                else :
                    Eradication += [0]
            eradication_prob = sum(Eradication)/float(len(Eradication))
            
        ld_ti -= 11
        eradication_prob = 0
        while eradication_prob < threshold:
            ld_ti += 1
            self.ld_time = ld_ti
            Eradication = []
            for sam in range(sample): 
                pop_sam = self.path()
                tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
                if pop_sam['i'][-1] == 0 and tot_size > 10: 
                    Eradication += [1]
                else :
                    Eradication += [0]
            eradication_prob = sum(Eradication)/float(len(Eradication))
        self.ld_time = ld_time_org
        return ld_ti


        
    
if __name__ == "__main__": 

    
    """ Effect of increasing u """
    b = 0.05
    v = 0.2
    u = 0.1
    g = 0.1
    R = 0
    w = 0.2
    q = 0
    
    """ One run """
    I = 6
    S = 100-6
    sirs_lq = SIRS_SLQ(b,v,u,g,w,q,10,S,I,R)
    output = sirs_lq.path(100)
    plt.plot(output['t'],output['s'],label = 'S')
    plt.plot(output['t'],output['q'],label = 'Q')
    plt.plot(output['t'],output['uq'],label = 'uQ')
    plt.plot(output['t'],output['r'],label = 'R')
    plt.plot(output['t'],output['d'],label = 'D')
    plt.title('Example of Eradication (Single Lockdown) \n '+'b = ' + str(b) + ', v = ' + str(v) + ', u = ' + str(u) + ', g = ' + str(g)+ ', w = ' + str(w)+ ', q = ' + str(q) + ', ld_time = ' + str(10))
    plt.xlabel('Time')
    plt.ylabel('Pop Size')
    plt.legend()
    
    """ Effect of increasing lockdown time """
    I_range = dst.drange(0,20,4)
    ldtime_range = dst.drange(0,50,2)
    fig, ax = plt.subplots(1,4)
    for I in I_range:
        print(I)
        S = 100 - I
        erd_prob_list = []
        MP_list = []
        MD_list = []
        MT_list = []
    
        for ld_time in ldtime_range: 
            sirs_lq = SIRS_SLQ(b,v,u,g,w,q,ld_time,S,I,R)
            MP, MD, MT, erd_prob = sirs_lq.metrics(1000,100)
            erd_prob_list += [erd_prob]
            MP_list += [MP]
            MD_list += [MD]
            MT_list += [MT]
        
        
        ax[0].plot(ldtime_range, erd_prob_list, label = str(I))
        ax[1].plot(ldtime_range, MP_list, label = str(I))
        ax[2].plot(ldtime_range, MD_list, label = str(I))
        ax[3].plot(ldtime_range, MT_list, label = str(I))
    
    ax[0].set_ylabel('Eradication Probability')
    ax[1].set_ylabel('Mean Pop Size')
    ax[2].set_ylabel('Mean Deaths')
    ax[3].set_ylabel('Mean Time to Eradication')
    fig.supxlabel('Lockdown Time')
    
    """ Critical Lockdown time v/s I_start """
    S = 100
    I = 0
    I_range = range(0,100,10)
    q_range = dst.drange(0,1,0.2)
    color_list = ['blue','red','orange','green','yellow','black']
    i=0
    for q in q_range:
        sirs_lq = SIRS_SLQ(b,v,u,g,w,q,0,S,I,R)
        sirs_mlq = SIRS_MLQ(b,v,u,g,w,q,0,S,I,R)
        ld_critical_list = []
        mld_critical_list = []
        for I in I_range:
            print(q,I)
            sirs_lq.uQ_start = I 
            sirs_mlq.uQ_start = I 
            sirs_lq.S_start = 100-I
            sirs_mlq.S_start = 100-I
            ld_critical = sirs_lq.critical_ldtime(1000)
            mld_critical = sirs_mlq.critical_ldtime(1000)
            ld_critical_list += [ld_critical]
            mld_critical_list += [mld_critical]
        plt.plot(I_range,ld_critical_list,label = str(q) + ' SLD', color = color_list[i])
        plt.plot(I_range,mld_critical_list,label = str(q) + ' MLD',linestyle = '--', color = color_list[i])
        i += 1
    plt.xlabel('No. of infections at the start of lockdown')
    plt.ylabel('Critical LD time')
    plt.legend(title='Quarantine Prob')
#    Critical Lockdown time - minimum lockdown time to se atleast 80% eradication probability

    