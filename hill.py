import numpy as nm

#Initialises matrices
keyMat =nm.zeros((2,2))
mes = nm.zeros((2,2))
ciphMat = nm.zeros((2,2))

#Translates key into numerics and puts into matrix
def KeyMatGen(ke):
    k = 0
    for i in range(2):
        for j in range (2):
            keyMat[i][j] = (ord(ke[k]) % 65)
            k += 1

#Multiplies the key and message matrices
def encryp():
    for i in range(2):
        for j in range(2):
            ciphMat[i][j] =0
            for x in range(2):
                ciphMat[i][j] += (keyMat[i][x] * mes[x][j])
            ciphMat[i][j] = ciphMat[i][j] % 26


message = "CAKE"


KeyMatGen("BAKE")
print(keyMat)
k=0
for i in range(2):
    for j in range(2):
        mes[j][i] = (ord(message[k])-65)%26
        k+=1

print(mes)

encryp()

ciphTex = []

#print(ciphMat)
for i in range(2):
    for j in range(2):
        ciphTex.append(chr(int(ciphMat[j][i])+ 65))

print(ciphTex)