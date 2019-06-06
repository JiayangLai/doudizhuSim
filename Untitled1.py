#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from utils import cardsDistribution,allWays,allMains
rankStd={'3':0,'4':1,'5':2,'6':3,'7':4,'8':5,'9':6,'T':7,'J':8,'Q':9,'K':10,'A':11,'2':12,'S':13,'B':14}


# In[2]:


class player:
    def __init__(self,cardsList,playerNo):
        self.cardsList=cardsList
        self.playerNo=playerNo
    def ranking(self,lastPlayOut,thisPlayOut):
        if thisPlayOut[0]=='SB':
            return True
        else:
            if lastPlayOut[1] in ['solo','pair','bomb','triosolo','triopair','fourdualsolos','fourdualpairs']:
                if rankStd[thisPlayOut[0][0]]>rankStd[lastPlayOut[0][0]]:
                    return True
                else:
                    return False
            elif lastPlayOut[1] in ['soloschain','pairschain','trioschain']:
                if rankStd[thisPlayOut[0][-1]]>rankStd[lastPlayOut[0][-1]]:
                    return True
                else:
                    return False
            elif lastPlayOut[1]=='triosolochains':
                Chainlen = int(len(lastPlayOut[0])/4)
#                 print(Chainlen)
                if rankStd[thisPlayOut[0][-Chainlen-1]]>rankStd[lastPlayOut[0][-Chainlen-1]]:
                    return True
                else:
                    return False
            elif lastPlayOut[1]=='triopairchains':
                Chainlen = int(len(lastPlayOut[0])/5)
                if rankStd[thisPlayOut[0][-Chainlen-1]]>rankStd[lastPlayOut[0][-Chainlen-1]]:
                    return True
                else:
                    return False
                
    def activateRandomPlay(self,cardsFlowStr):
#         print(self.playerNo,'active',self.cardsList)
        allWaysList = allWays(self.cardsList)
        playOut = random.sample(allWaysList, 1)[0]
        for cardout in playOut[0]:
            self.cardsList.remove(cardout)
        return playOut,cardsFlowStr+str(self.playerNo)+','+playOut[0]+';'
    def passiveRandomPlay(self,cardsFlowStr,outCards):
#         print(self.playerNo,'passive',self.cardsList)
        allWaysList = [['','pass']]+allWays(self.cardsList)
        category = outCards[1]
        while 1:
            playOut = random.sample(allWaysList, 1)[0]
            if playOut[0]=='':
                return playOut,cardsFlowStr
            else:
                if playOut[1]=='rocket' or (playOut[1]=='bomb' and outCards[1]!='bomb'):
                    for cardout in playOut[0]:
                        self.cardsList.remove(cardout)
                    return playOut,cardsFlowStr+str(self.playerNo)+','+playOut[0]+';'
                else:
                    if playOut[1]==category and len(playOut[0])==len(outCards[0]) and self.ranking(outCards,playOut):
                        for cardout in playOut[0]:
                            self.cardsList.remove(cardout)
                        return playOut,cardsFlowStr+str(self.playerNo)+','+playOut[0]+';'
                    else:
                        allWaysList.remove(playOut)

    def modedPlayRandom(self,cardsFlowStr,outCards=None):
        if not outCards:
            return self.activateRandomPlay(cardsFlowStr)
        else:
            if cardsFlowStr.split(';')[-2].split(',')[0]==str(self.playerNo):
                return self.activateRandomPlay(cardsFlowStr)
            else:
                return self.passiveRandomPlay(cardsFlowStr,outCards)
                


# In[3]:

awl = allWays(list(rankStd.keys())*4)
DW=0
NW=0
for i in range(1):
#     if i%500==0:
#         print(i)
    D,DU,DD=cardsDistribution()
    dz = player(D,0)
    dd = player(DD,1)
    du = player(DU,2)
    cardsFlowStr=''
    outCards=None
    while 1:
        print(dz.cardsList)
        print(cardsFlowStr)
        cards = input("input cards: ")

        if cards!='':
            for ii in awl:
                if cards==ii[0]:
                    category=ii[1]
                    break
        #category = input("input category: ")
            outCards=[cards,category]
            cardsFlowStr = cardsFlowStr+str(dz.playerNo)+','+cards+';'
            for i in outCards[0]:
                dz.cardsList.remove(i)
        else:
            outCards=['','pass']
			
#         outCards,cardsFlowStr = dz.modedPlayRandom(cardsFlowStr,outCards)
    #     print(outCards)
#         print(cardsFlowStr)
    #     print()
        if dz.cardsList==[]:
            DW=DW+1
            break
        outCards,cardsFlowStr = dd.modedPlayRandom(cardsFlowStr,outCards)
        print('ddrest',len(dd.cardsList))
    #     print(outCards)
#         print(cardsFlowStr)
    #     print()
        if dd.cardsList==[]:
            NW=NW+1
            break
        outCards,cardsFlowStr = du.modedPlayRandom(cardsFlowStr,outCards)
        print('durest',len(du.cardsList))

    #     print(outCards)
#         print(cardsFlowStr)
    #     print()
        if du.cardsList==[]:
            NW=NW+1
            break
# print(DW,NW)
print('ddrest',dd.cardsList)
print('durest',du.cardsList)
print(cardsFlowStr)


# In[4]:


# allWays(list(rankStd.keys())*4)


# In[ ]:




