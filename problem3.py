def printCombination(distincList,currList,currIndex,n,ansList):
    if(currIndex==len(distincList)):
        if(len(currList) == n):
            ansList.append(currList)
        return 
    else:
        listCopy= currList.copy()
        listCopy.append(distincList[currIndex])
        currIndex+=1
        printCombination(distincList,currList,currIndex,n,ansList)
        printCombination(distincList,listCopy,currIndex,n,ansList)

def numerOfPair(inputList,n):
    res=0
    dict={}
    for number in inputList:
        if(number not in dict):
            dict[number]=1
        else:
            dict[number]+=1
    distincList=[]
    for number,occurence in dict.items():
         distincList.append(number)
    ansList=[]
    printCombination(distincList,[],0,n,ansList)
    return ansList
#Test case 1:
inputList1= [1,2,3]
n=2
print(numerOfPair(inputList1,n)) #output [[2, 3], [1, 3], [1, 2]]
#Test case 2:
inputList2= [1,2,3,3,2,1]
n=2
print(numerOfPair(inputList2,n)) #output [[2, 3], [1, 3], [1, 2]]
#Test case 3:
inputList3= [1,2,3,4]
n=3
print(numerOfPair(inputList3,n)) #output [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]
