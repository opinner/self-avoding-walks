import numpy as np
import matplotlib.pyplot as plt


# SAW kann keine Sackgassen wirklich erkennen und auch keine Randbedingungen
def bad_saw(N, x=50, y=50):
    
    deadend = 0
    count = 0

    lattice = np.zeros((100,100))
    neighbours = np.asarray([[0,1],[0,-1],[1,0],[-1,0]])

    way = np.asarray([[x,y]])
    lattice[x][y] = 1
    
    print("start")
    for k in range(1,N+1):
        
        if count !=0: 
            print("sackgasse")
            break 

        while True:
            direction = neighbours[np.random.choice(len(neighbours))]

            next_step = way[-1]+direction

            #deadend = np.all([lattice[x+1,y],lattice[x-1,y],lattice[x,y+1],lattice[x,y-1]]==1)
            #print(deadend)

            #Soll Sackgassen erkennen (erster dreckiger Versuch, später mehr)
            if count > 40:
                break      
    
            elif lattice[next_step[0]][next_step[1]] == 1:
                count += 1
                continue 

            else:
                count = 0
                way = np.concatenate((way, [next_step]))
                lattice[next_step[0]][next_step[1]] = 1
                
                break


    print("Ende \t")
    return way


way = bad_saw(100)

#print(way)

plt.plot(way[:,0],way[:,1],50,50,"rD")
plt.grid()
plt.axis('equal')
plt.show()

