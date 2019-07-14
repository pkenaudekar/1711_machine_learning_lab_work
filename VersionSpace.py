set = {}
G = {}
G_temp = {}
S_temp = {}
positive = {}
positive_temp = {}
val = 5
numSet = 6
numCol = 6
iteration = 1
first_value = 0
G = {"1": "X1","2": "X2","3": "X3","4": "X4","5": "X5"}
S = {}

set[1] ={"Country": "Japan","Manufacturer": "Honda","Colour": "Blue","Year": 1980,"Type":"Economy", "Result":"Positive"}
set[2] ={"Country": "Japan","Manufacturer": "Toyota","Colour": "Green","Year": 1970,"Type":"Sports", "Result":"Negitive"}
set[3] ={"Country": "Japan","Manufacturer": "Toyota","Colour": "Blue","Year": 1990,"Type":"Economy", "Result":"Positive"}
set[4] ={"Country": "USA","Manufacturer": "Chrysler","Colour": "Red","Year": 1980,"Type":"Economy", "Result":"Negitive"}
set[5] ={"Country": "Japan","Manufacturer": "Honda","Colour": "White","Year": 1980,"Type":"Economy", "Result":"Positive"}

#Positive set
for i in range(1,numSet):
    if(set[i]["Result"]=="Positive"):
        l = 1
        if(first_value == 0): #Copying 1st positive value
            for value in set[i].values():
                positive_temp[str(l)] = value
                l += 1
            first_value = 1
        else:
            for value in set[i].values():
                if(positive[str(l)] != value):
                    positive_temp[str(l)] = "X"+str(l)
                else:
                    positive_temp[str(l)] = value
                l += 1
        positive = positive_temp.copy()
positive.popitem()
#print("Positive:", positive)

#Display Table
print("The table is:")
for i in range(1,numSet):
    print(set[i])

print("\nFor iteration: ",iteration)
print("G= ",G)
print("S= ",S)
iteration += 1
print("\nFor iteration: ",iteration)
for i in range(1,numSet):
    if(set[i]["Result"]=="Positive"):
        exclude = i
        i = 1
        for value in set[i].values():
            S[str(i)] = value
            i += 1
        S.popitem()
        print("G= ",G)
        print("S= ",S)
        break

for i in range(1,numSet ):
    if(i != exclude):
        iteration+= 1
        print("\nFor iteration: ",iteration)
        #for a positive value:
        if(set[i]["Result"]=="Positive"):
            #for x in (1,numCol):
            j = 1
            for set_key, set_value in set[i].items():
                if(j != len(set[i])):
                    #Changes to set G
                    if(set_value == G[str(j)]): #if both values are same
                        G_temp[str(j)] = set[i][set_key] #keep the value from set
                    else:
                        G_temp[str(j)] = "X"+str(j) #mark as X1,X2....Xn
                    #Changes to set S
                    if(set_value == S[str(j)]): #if both values are same
                        S_temp[str(j)] = set[i][set_key] #keep the value from set
                    else:
                        S_temp[str(j)] = "X"+str(j) #mark as X1,X2....Xn
                    
                    #print("G[g_key]= ",G[str(j)])
                    #print("set_value= ",set_value)
                    #print("S[g_key]= ",S[str(j)])
                    #print("set_value= ",set_value)
                    j+=1
                    #print("j:",j)
            #print("G_temp= ",G_temp)#
            #print("S_temp= ",S_temp)#
            G = G_temp.copy()
            S = S_temp.copy()
            print("G= ",G)#
            print("S= ",S)#
        #For a negative value:
        else:
            k = 1
            for set_key, set_value in set[i].items():
                if(k != len(set[i])):
                    #Changes to set G
                    if(set_value == S[str(k)] and set_value != G[str(k)]):
                        G_temp[str(k)] = "X"+str(k)
                    else:
                        G_temp[str(k)] = S[str(k)]
                                       
                    #print("G[g_key]= ",G[str(j)])
                    #print("set_value= ",set_value)
                    #print("S[g_key]= ",S[str(j)])
                    #print("set_value= ",set_value)
                    k+=1
            #print("G_temp= ",G_temp)#
            #print("S_temp= ",S_temp)#
            G = G_temp.copy()
            #S = S_temp.copy()
            print("G= ",G)#
            print("S= ",S)#
        
        #checking for convergence
        same = 1
        for g_key, g_value in G.items():
            if(g_value != S[g_key] or g_value != positive[g_key]):
                same = 0
                break
        
        if(same == 1):
            break
        
