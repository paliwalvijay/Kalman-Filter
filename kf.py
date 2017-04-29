from numpy import *
from numpy import dot, sum, tile, linalg, random
from numpy.linalg import inv,det
from numpy.random import randn
import matplotlib.pyplot as plt


step = 1
N = 50
muT = array([[0.0], [0.1]])
sigmaX = diag((0.01,0.01))
F = array ([[1,1],[0,1]])
H = eye(F.shape[0])
sigmaZ = diag((0.1,0.1))
sigmaT = diag((0.01,0.01))
I = eye(F.shape[0])
K = zeros((2,2))
val = 0.0
obser = []
pred = []
for i in range(0,N):
	val = val+step
	Z = array([[0.5*randn(1)[0]+val],[0.0]]);
	K = dot(dot((dot(dot(F,sigmaT), F.T) + sigmaX), H.T), inv(dot( dot(H, dot(dot(F, sigmaT), F.T)), H.T)+sigmaZ))
	sigmaT = dot((I - dot(K,H)), (dot(dot(F, sigmaT), F.T)+ sigmaX))
	muT = dot(F, muT)+ dot(K, Z- dot(dot(H,F),muT))
	print str(muT[0])+" "+str(Z[0])
	obser.append(Z[0])
	pred.append(muT[0])
plt.plot(obser, pred)
plt.show()