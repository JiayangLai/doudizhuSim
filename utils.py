#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
rankStd={'3':0,'4':1,'5':2,'6':3,'7':4,'8':5,'9':6,'T':7,'J':8,'Q':9,'K':10,'A':11,'2':12,'S':13,'B':14}


# In[2]:


def sort_by_value(d): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort() 
    return [ backitems[i][1] for i in range(0,len(backitems))] 


# In[3]:


def sortInRanks(cardsin):
    dictin = {}
    for cardi in cardsin:
        dictin[cardi]=rankStd[cardi]
    
    return sort_by_value(dictin)


# In[4]:


def solos(cardsIn):
    cardsIn = list(set(cardsIn))
    cardsIn = sortInRanks(cardsIn)
    return(cardsIn)


# In[5]:


def pairs(cardsIn):
    listpair = []
    for i in cardsIn:
        if cardsIn.count(i)>=2:
            listpair = listpair + [i]
    listpair = list(set(listpair))
    return(sortInRanks(listpair))


# In[6]:


def trios(cardsIn):
    listpair = []
    for i in cardsIn:
        if cardsIn.count(i)>=3:
            listpair = listpair + [i]
    listpair = list(set(listpair))
    return(sortInRanks(listpair))


# In[7]:


def bomb(cardsIn):
    listpair = []
    for i in cardsIn:
        if cardsIn.count(i)==4:
            listpair = listpair + [i]
    listpair = list(set(listpair))
    return(sortInRanks(listpair))


# In[8]:


def rocket(cardsIn):
    if 'B' in cardsIn and 'S' in cardsIn:
        return ['SB']
    else:
        return []


# In[9]:


def cardsDistribution(seedin=None):
    list1 = ['A']*4
    list2 = ['2']*4
    list3 = ['3']*4
    list4 = ['4']*4
    list5 = ['5']*4
    list6 = ['6']*4
    list7 = ['7']*4
    list8 = ['8']*4
    list9 = ['9']*4
    listT = ['T']*4
    listJ = ['J']*4
    listQ = ['Q']*4
    listK = ['K']*4
    listB = ['S']
    listS = ['B']
    allcards = list1+list2+list3+list4+list5+list6+list7+list8+list9+listT+listJ+listQ+listK+listB+listS
    allcards
    if seedin:
        random.seed(seedin)
    dizhu = random.sample(allcards, 20)  
    for x in dizhu:
        allcards.remove(x)

    dizhuup = random.sample(allcards, 17)  
    for x in dizhuup:
        allcards.remove(x)

    dizhudown = random.sample(allcards, 17)  
    for x in dizhudown:
        allcards.remove(x)

    return sortWithDup(dizhu),sortWithDup(dizhuup),sortWithDup(dizhudown)

def sortWithDup(cards):
	cardsout=[]
	for cardi in sortInRanks(cards):
		if cardi in bomb(cards):
			cardsout=cardsout+[cardi]*4
			continue
		elif cardi in trios(cards):
			cardsout=cardsout+[cardi]*3
			continue
		elif cardi in pairs(cards):
			cardsout=cardsout+[cardi]*2
			continue
		else:
			cardsout=cardsout+[cardi]
	return cardsout
		
# In[10]:


def solosChains(solosList):
    if '2' in solosList:
        solosList.remove('2')
    if 'B' in solosList:
        solosList.remove('B')
    if 'S' in solosList:
        solosList.remove('S')
    lensolosList = len(solosList)
    solosChainsList=[]
    for lenth in [5,6,7,8,9,10,11,12]:
        if lenth<=lensolosList:
            listcount = list(range(lensolosList-lenth))
            if listcount==[]:
                listcount=[0]
            for i in listcount:
                if rankStd[solosList[i+lenth-1]]-rankStd[solosList[i]]==lenth-1:
                    solosChainsList=solosChainsList+[''.join(solosList[i:i+lenth])]
                
        else:
            break
    return solosChainsList


# In[11]:


def pairsChains(pairsList):
    if '2' in pairsList:
        pairsList.remove('2')
    if 'B' in pairsList:
        pairsList.remove('B')
    if 'S' in pairsList:
        pairsList.remove('S')
    lenpairsList = len(pairsList)
    pairsChainsList=[]
    for lenth in [3,4,5,6,7,8,9,10]:
        if lenth<=lenpairsList:
            listcount = list(range(lenpairsList-lenth))
            if listcount==[]:
                listcount=[0]
            for i in listcount:
                if rankStd[pairsList[i+lenth-1]]-rankStd[pairsList[i]]==lenth-1:
                    pairsList2 = pairsList[i:i+lenth]
                    pairsList2 = sortInRanks(pairsList2)
                    for i in pairsList2:
                        pairsList2[pairsList2.index(i)]=i+i
                        
                    pairsChainsList=pairsChainsList+[''.join(pairsList2)]
                
        else:
            break
    return pairsChainsList


# In[12]:


def triosChains(triosList):
    if '2' in triosList:
        triosList.remove('2')
    if 'B' in triosList:
        triosList.remove('B')
    if 'S' in triosList:
        triosList.remove('S')
    lentriosList = len(triosList)
    triosChainsList=[]
    for lenth in [2,3,4,5,6]:
        if lenth<=lentriosList:
            listcount = list(range(lentriosList-lenth))
            if listcount==[]:
                listcount=[0]
            for i in listcount:
                if rankStd[triosList[i+lenth-1]]-rankStd[triosList[i]]==lenth-1:
                    triosList2 = triosList[i:i+lenth]
                    triosList2 = sortInRanks(triosList2)
                    for i in triosList2:
                        triosList2[triosList2.index(i)]=i+i+i
                        
                    triosChainsList=triosChainsList+[''.join(triosList2)]
                
        else:
            break
    return triosChainsList


# In[13]:


def triosSolo(triosList,solosList):
    triosSoloList = []
    for t in triosList:
        newSolos = solosList[:]
        newSolos.remove(t)
        for s in newSolos:
            triosSoloList = triosSoloList+[t+t+t+s]
    return triosSoloList


# In[14]:


def triosPair(triosList,pairsList):
    triosPairList = []
    for t in triosList:
        newPairs = pairsList[:]
        newPairs.remove(t)
        for p in newPairs:
            triosPairList = triosPairList+[t+t+t+p+p]
    return triosPairList


# In[15]:


def triosSoloChains(triosChainsList,solosList):
    triosSoloChainsList=[]
    for chaini in triosChainsList:
        chainiList = list(set(list(chaini)))
        chainiList = sortInRanks(chainiList)
        newSolos = solosList[:]
        for t in chainiList:
            newSolos.remove(t)
        
        if len(chainiList)==2:
            listcn2 = cn2(newSolos)
            for cn2i in listcn2:
                triosSoloChainsList = triosSoloChainsList+[chaini+cn2i[0]+cn2i[1]]
        if len(chainiList)==3:
            listcn3 = cn3(newSolos)
            for cn3i in listcn3:
                triosSoloChainsList = triosSoloChainsList+[chaini+cn3i[0]+cn3i[1]+cn3i[2]]
        if len(chainiList)==4:
            listcn4 = cn4(newSolos)
            for cn4i in listcn4:
                triosSoloChainsList = triosSoloChainsList+[chaini+cn4i[0]+cn4i[1]+cn4i[2]+cn4i[3]]
        if len(chainiList)==5:
            listcn5 = cn5(newSolos)
            for cn5i in listcn5:
                triosSoloChainsList = triosSoloChainsList+[chaini+cn5i[0]+cn5i[1]+cn5i[2]+cn5i[3]+cn5i[4]]
            
            
            
    return triosSoloChainsList


# In[54]:


def triosPairChains(triosChainsList,pairList):
    triosPairChainsList=[]
    for chaini in triosChainsList:
        chainiList = list(set(list(chaini)))
        chainiList = sortInRanks(chainiList)
        newPairs = pairList[:]
        for t in chainiList:
            newPairs.remove(t)
        
        if len(chainiList)==2:
            listcn2 = cn2(newPairs)
            for cn2i in listcn2:
                triosPairChainsList = triosPairChainsList+[chaini+cn2i[0]*2+cn2i[1]*2]
        if len(chainiList)==3:
            listcn3 = cn3(newPairs)
            for cn3i in listcn3:
                triosPairChainsList = triosPairChainsList+[chaini+cn3i[0]*2+cn3i[1]*2+cn3i[2]*2]
        if len(chainiList)==4:
            listcn4 = cn4(newPairs)
            for cn4i in listcn4:
                triosPairChainsList = triosPairChainsList+[chaini+cn4i[0]*2+cn4i[1]*2+cn4i[2]*2+cn4i[3]*2]
        if len(chainiList)==5:
            listcn5 = cn5(newPairs)
            for cn5i in listcn5:
                triosPairChainsList = triosPairChainsList+[chaini+cn5i[0]*2+cn5i[1]*2+cn5i[2]*2+cn5i[3]*2+cn5i[4]*2]
            
            
            
    return triosPairChainsList


# In[78]:


def fourDualSolos(fourList,soloList):
    fourDualSolosList=[]
    for fouri in fourList:
        newSolos = soloList[:]
        for t in fourList:
            newSolos.remove(t)
        listcn2 = cn2(newSolos)
        for cn2i in listcn2:
            fourDualSolosList = fourDualSolosList + [fouri*4+cn2i[0]+cn2i[1]]
    return fourDualSolosList


# In[82]:


def fourDualPairs(fourList,pairList):
    fourDualPairsList=[]
    for fouri in fourList:
        newPairs = pairList[:]
        for t in fourList:
            newPairs.remove(t)
        listcn2 = cn2(newPairs)
        for cn2i in listcn2:
            fourDualPairsList = fourDualPairsList + [fouri*4+cn2i[0]*2+cn2i[1]*2]
    return fourDualPairsList


# In[83]:


def cn2(lista):
    listcn2=[]
    listb=lista[:]
    for i in lista:
        listb.remove(i)
        for j in listb:
            listcn2 = listcn2+[[i,j]]
    return listcn2

def cn3(lista):
    listcn3=[]
    listb=lista[:]
    for i in lista:
        listb.remove(i)
        listc=listb[:]
        for j in listb:
            listc.remove(j)
            for k in listc:
                listcn3 = listcn3+[[i,j,k]]
    return listcn3

def cn4(lista):
    listcn4=[]
    listb=lista[:]
    for i in lista:
        listb.remove(i)
        listc=listb[:]
        for j in listb:
            listc.remove(j)
            listd=listc[:]
            for k in listc:
                listd.remove(k)
                for l in listd:
                    listcn4 = listcn4+[[i,j,k,l]]
    return listcn4

def cn5(lista):
    listcn5=[]
    listb=lista[:]
    for i in lista:
        listb.remove(i)
        listc=listb[:]
        for j in listb:
            listc.remove(j)
            listd=listc[:]
            for k in listc:
                listd.remove(k)
                liste=listd[:]
                for l in listd:
                    liste.remove(l)
                    for m in liste:
                        listcn5 = listcn5+[[i,j,k,l,m]]
    return listcn5


# In[100]:


def allWays(cards):
    allWays = solos(cards)
    for p in pairs(cards):
        allWays = allWays + [p*2]
    for t in trios(cards):
        allWays = allWays + [t*3]
    for f in bomb(cards):
        allWays = allWays + [f*4]
    allWays = allWays + rocket(cards)+ solosChains(solos(cards)) + pairsChains(pairs(cards)) + triosChains(trios(cards)) +    triosSolo(trios(cards),solos(cards)) + triosPair(trios(cards),pairs(cards))+triosSoloChains(triosChains(trios(cards)),solos(cards))+    triosPairChains(triosChains(trios(cards)),pairs(cards))+fourDualSolos(bomb(cards),solos(cards))+fourDualPairs(bomb(cards),pairs(cards))
    return allWays
    


# In[101]:

if __name__ == '__main__':
	dizhu,dizhuup,dizhudown = cardsDistribution(seedin=None)
	print(solos(dizhu))
	print(pairs(dizhu))
	print(trios(dizhu))
	print(solosChains(solos(dizhu)))
	print(pairsChains(pairs(dizhu)))
	print(triosChains(trios(dizhu)))
	print(bomb(dizhu))
	print(rocket(dizhu))
	print(triosSolo(trios(dizhu),solos(dizhu)))
	print(triosPair(trios(dizhu),pairs(dizhu)))
	print(triosSoloChains(triosChains(trios(dizhu)),solos(dizhu)))
	print(triosPairChains(triosChains(trios(dizhu)),pairs(dizhu)))
	print(fourDualSolos(bomb(dizhu),solos(dizhu)))
	print(fourDualPairs(bomb(dizhu),pairs(dizhu)))
	print(allWays(dizhu))


# In[ ]:




