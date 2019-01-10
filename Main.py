                # COMPLEX NETWORKS PROJECT CODE
#_____________________________________________________________________
#MEMBER 1: KARN VADALIYA (201501116)
#MEMBER 2: KUSH PATEL (201501250)
#MEMBER 3: LUV PATEL (201501459)
#_____________________________________________________________________





#Importing Libraries
import networkx as nx
from networkx.algorithms.community.quality import modularity
import matplotlib.pyplot as plt
import numpy as np
import community
#import snap


  
print("\n\n______________________________________________________________________________________\n")
print("\n")
s = "\t\t***  WELCOME TO THE GAME OF NODES  ***"
s.center(40)
print(s)
#print("\n\n________")
print("\n\n______________________________________________________________________________________\n\n\n\n")

# Reading from Input Dataset.

f =  open("got.txt", "r")
content = f.readlines()
content = [x.strip() for x in content]




# Creating Graph
G = nx.Graph()

for x in content:
    line =  x.split(',')
    G.add_edge((line[0]), (line[1]), weight=int(line[2]))
    
print ("Number of Nodes in the Network: ", G.number_of_nodes())
print ("Number of Edges in the Network: ", G.number_of_edges())
print()



print("Average Clustering Co-effecient = ", nx.average_clustering(G),".\n\n")








#____________________________________________________________



print ("\n___________________________________\n\nDegree Centrality\n")
#print ("Degree Centrality")
degree_centrality = nx.degree_centrality(G)
listt=[]

for x in degree_centrality:
   #print(x, "-->", degree_centrality[x])
   listt.append([x,round(degree_centrality[x],4)])
   

mat_vals = np.vstack(listt)
#mat_vals[0]=int(mat_vals[0])
#mat_vals.sort()
tere=sorted(mat_vals,key=lambda x: (x[1]), reverse=True)
#print(tere)
#print("___________________________")
#print(sorted(mat_vals[0][0],key=lambda x: (x[1]), reverse=True))

print("\nTop 10:\n_______")

for i in range(10):
    print(tere[i][0], " -> ", tere[i][1])

firstname=[]
for kk in range(10):
    firstname.append(tere[9-kk][0])

secondname=[]
for kk in range(10):
    secondname.append(tere[9-kk][1])


index = np.arange(len(firstname))
index=9-index
plt.bar(index, secondname)
plt.xlabel('Character', fontsize=10)
plt.ylabel('Degree Centrality', fontsize=10)
plt.xticks(index, firstname, fontsize=10, rotation=30)
plt.title('Bar Graph representing Degree Centrality of Top 10 Characters.')
plt.show()

#____________________________________________________________










print ("\n\n __________________________________________________________\n")
print ("\nCloseness Centrality:")
closeness_centrality = nx.closeness_centrality(G)
    
close_listt=[]

for x in closeness_centrality:
   #print(x, "-->", degree_centrality[x])
   close_listt.append([x,round(closeness_centrality[x],4)])
   

close_mat_vals = np.vstack(close_listt)
#mat_vals[0]=int(mat_vals[0])
#mat_vals.sort()
close_tere=sorted(close_mat_vals,key=lambda x: (x[1]), reverse=True)
#print(close_tere)
#print("___________________________")
#print(sorted(mat_vals[0][0],key=lambda x: (x[1]), reverse=True))

print("\nTop 10:\n________")

for i in range(10):
    print(close_tere[i][0]," -> ",close_tere[i][1])

close_firstname=[]
for kk in range(10):
    close_firstname.append(close_tere[9-kk][0])

close_secondname=[]
for kk in range(10):
    close_secondname.append(close_tere[9-kk][1])


close_index = np.arange(len(close_firstname))
close_index=9-close_index
plt.bar(close_index, close_secondname, color=(0.8, 0.2, 0.1, 0.9))
plt.xlabel('Character', fontsize=10)
plt.ylabel('Closeness Centrality', fontsize=10)
plt.xticks(close_index, close_firstname, fontsize=10, rotation=30)
plt.title('Bar Graph representing Closeness Centrality of Top 10 Characters.')
plt.show()

#print("__________________________________________________________________")
#_________________________________________________________________________________











print ("\n __________________________________________________________\n")
print ("\nBetweenness Centrality:")
betweenness_centrality = nx.betweenness_centrality(G, normalized=True)
#closeness_centrality = nx.closeness_centrality(G)
    
between_listt=[]

for x in betweenness_centrality:
   #print(x, "-->", degree_centrality[x])
   between_listt.append([x,round(betweenness_centrality[x],4)])
   

between_mat_vals = np.vstack(between_listt)
#mat_vals[0]=int(mat_vals[0])
#mat_vals.sort()
between_tere=sorted(between_mat_vals,key=lambda x: (x[1]), reverse=True)
#print(close_tere)
#print("___________________________")
#print(sorted(mat_vals[0][0],key=lambda x: (x[1]), reverse=True))

print("\nTop 10:\n________")

for i in range(10):
    print(between_tere[i][0]," -> ",between_tere[i][1])

between_firstname=[]
for kk in range(10):
    between_firstname.append(between_tere[9-kk][0])

between_secondname=[]
for kk in range(10):
    between_secondname.append(between_tere[9-kk][1])


between_index = np.arange(len(between_firstname))
between_index=9-between_index
plt.bar(between_index, between_secondname, color=(0.2, 0.3, 0.3, 0.9))
plt.xlabel('Character', fontsize=10)
plt.ylabel('Betweenness Centrality', fontsize=10)
plt.xticks(between_index, between_firstname, fontsize=10, rotation=30)
plt.title('Bar Graph representing Betweenness Centrality of Top 10 Characters.')
plt.show()

#print("__________________________________________________________________")
#_________________________________________________________________________________









print ("\n __________________________________________________________\n")
print ("\n PageRank Centrality:")
pgrank_centrality = nx.pagerank(G,weight=G.get_edge_data)
#closeness_centrality = nx.closeness_centrality(G)
    
pgrank_listt=[]

for x in pgrank_centrality:
   #print(x, "-->", degree_centrality[x])
   pgrank_listt.append([x,round(pgrank_centrality[x],4)])
   

pgrank_mat_vals = np.vstack(pgrank_listt)
#mat_vals[0]=int(mat_vals[0])
#mat_vals.sort()
pgrank_tere=sorted(pgrank_mat_vals,key=lambda x: (x[1]), reverse=True)
#print(close_tere)
#print("___________________________")
#print(sorted(mat_vals[0][0],key=lambda x: (x[1]), reverse=True))

print("\nTop 10:\n________")

for i in range(10):
    print(pgrank_tere[i][0]," -> ",pgrank_tere[i][1])

pgrank_firstname=[]
for kk in range(10):
    pgrank_firstname.append(pgrank_tere[9-kk][0])

pgrank_secondname=[]
for kk in range(10):
    pgrank_secondname.append(pgrank_tere[9-kk][1])


pgrank_index = np.arange(len(pgrank_firstname))
pgrank_index=9-pgrank_index
plt.bar(pgrank_index, pgrank_secondname, color=(0.2, 0.8, 0.3, 0.9))
plt.xlabel('Character', fontsize=10)
plt.ylabel('Pagerank', fontsize=10)
plt.xticks(pgrank_index, pgrank_firstname, fontsize=10, rotation=30)
plt.title('Bar Graph representing Pagerank Value of Top 10 Characters.')
plt.show()

#print("__________________________________________________________________")
#_________________________________________________________________________________










print ("\n __________________________________________________________\n")
print ("Eigenvector Centrality")
eigen_centrality = nx.eigenvector_centrality(G,weight=G.get_edge_data)

eigen_listt=[]

for x in eigen_centrality:
   #print(x, "-->", degree_centrality[x])
   eigen_listt.append([x,round(eigen_centrality[x],4)])
   

eigen_mat_vals = np.vstack(eigen_listt)
#mat_vals[0]=int(mat_vals[0])
#mat_vals.sort()
eigen_tere=sorted(eigen_mat_vals,key=lambda x: (x[1]), reverse=True)
#print(close_tere)
#print("___________________________")
#print(sorted(mat_vals[0][0],key=lambda x: (x[1]), reverse=True))

print("\nTop 10:\n________")

for i in range(10):
    print(eigen_tere[i][0]," -> ",eigen_tere[i][1])

eigen_firstname=[]
for kk in range(10):
    eigen_firstname.append(eigen_tere[9-kk][0])

eigen_secondname=[]
for kk in range(10):
    eigen_secondname.append(eigen_tere[9-kk][1])

'''
#axes.set_xlim([xmin,xmax])
 
# Plot
plt.scatter(eigen_firstname, eigen_secondname, alpha=0.5)
plt.ylim(-1, 1)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(0, 10)

plt.show()




plt.plot(eigen_firstname,eigen_secondname,color='r')
x1,x2,y1,y2 = plt.axis()
plt.axis((0,1,y1,y2))
plt.show()
'''


eigen_index = np.arange(len(eigen_firstname))
eigen_index=9-eigen_index
plt.bar(eigen_index, eigen_secondname, color=(0.9, 0.8, 0.1, 0.7))
plt.xlabel('Character', fontsize=10)
plt.ylabel('Eigenvector Centrality', fontsize=10)
plt.xticks(eigen_index, eigen_firstname, fontsize=10, rotation=30)
plt.title('Bar Graph representing Eigenvector Centrality of Top 10 Characters.')
plt.show()

print("__________________________________________________________________")
#_________________________________________________________________________________















#_________________________________________________________________________________

# COMMUNITY DETECTION

print("\n\n______________________")
print(" COMMUNITY DETECTION ")
print("______________________")

print("")
partition=community.best_partition(G)
#c=list(greedy_modularity_communities(G,weight=G.get_edge_data))
#sorted(c[0])


cmap=['g','r','b','c','m','y','k','k','y','y','m','c','y','r','b','g','m','r','b']
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0
for com in set(partition.values()) :
    #print(com)
    count += 1
    list_nodes = [nodes for nodes in partition.keys()
                                      if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                      node_color = cmap[com])

nx.draw_networkx_edges(G, pos, edge_color='k',alpha=0.5)
plt.show()



#_____________________________________________________________________________








# TO KNOW WHICH CHARACTER LIES IN WHICH CLASS PARTITION, WE CAN RUN THE BELOW CODE. 

part=[]

for key, value in partition.items():
    temp = [key,value]
    part.append(temp)

part_mat_vals = np.vstack(part)
#mat_vals[0]=int(mat_vals[0])
#mat_vals.sort()

#print(close_tere)
#print("___________________________")
#print(sorted(mat_vals[0][0],key=lambda x: (x[1]), reverse=True))
part_tere=sorted(part_mat_vals,key=lambda x: (x[1]), reverse=True)



# INPUT THE CLASS INDEX FOR WHICH YOU WANT THE CHARACTERS. IN OUR CASE, ITS CLASS/PARTITION NO: 1.

'''
for i in range(0, len(part_tere)):
    if int(part_tere[i][1])==1:
        print(part_tere[i][0])
'''


