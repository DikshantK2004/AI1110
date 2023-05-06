import numpy as np
import matplotlib.pyplot as plt


simlen = 10000

pX = pY = np.ones(6)
pX = pY = pX/6
pZ = np.array([ 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36 ])
possible = np.arange(1,7)
possible_Z = np.arange(2, 13)
X= np.random.choice(possible, simlen, p=pX)
Y= np.random.choice(possible, simlen, p=pY)
cdfY = np.cumsum(pY)
Z = X + Y

simX, simpX = np.unique(X , return_counts= True)
simZ, simpZ = np.unique(Z , return_counts= True)
simY, simpY = np.unique(Y , return_counts= True)

simpX = simpX/simlen
simpY = simpY/simlen
simpZ = simpZ/simlen

simp_cdfY = np.cumsum(simpY)
# for Question1,
p1theo = cdfY[5] - cdfY[3]
p1sim = simp_cdfY[5] - simp_cdfY[3]

print("Theoretical value of probability of getting sum > 9 given X>5 is: " + str(p1theo))
print("Actual value of probability of getting sum > 9 given X>5 is: " + str(p1sim))


print("----------")
#for Question2,
p2theo = (pX[2]*pY[4] + pX[1]*pY[5])/cdfY[3]
p2sim = (simpX[2]*simpY[4] + simpX[1]*simpY[5])/simp_cdfY[3]

print("Theoretical value of probability of getting sum = 8 given Y < 4 is: " + str(p2theo))
print("Actual value of probability of getting sum = 8 given Y < 4 is: " + str(p2sim))

#plotting

fig,axes = plt.subplots(2,figsize = (12,10))
#plot-1
axes[0].set_title("Plot for probabilites of Z")
axes.flat[0].set(xlabel = 'Z' , ylabel = 'pZ')
axes[0].stem(possible_Z , simpZ , label = 'Actual', markerfmt = 'ro' , basefmt = 'g-' ,linefmt = 'b')
axes[0].plot(possible_Z , pZ , 'yo',label = 'Theoretical')
axes[0].legend()

#plot-2
axes[1].set_title("Plot for verifying current problem")
axes.flat[1].set(xlabel = 'Questions' , ylabel = 'Answers')
axes[1].stem([1, 2] , [p1theo,p2theo] , label = 'Actual', markerfmt = 'ro' , basefmt = 'g-' ,linefmt = 'b')
axes[1].plot([1, 2] , [p1sim, p2sim], 'yo',label = 'Theoretical')
axes[1].legend()
plt.show()



