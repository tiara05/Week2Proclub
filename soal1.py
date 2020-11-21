arrBerat = []
bMin = 0
bMax = 0

def hitungMax(arrBerat):
    iMax = arrBerat[0]
    for i in range(1, len(arrBerat)):
       if(arrBerat[i] > iMax):
            iMax = arrBerat[i]
    return iMax
    
def hitungMin(arrBerat):
    iMin = arrBerat[0]
    for i in range(1, len(arrBerat)):
       if(arrBerat[i] < iMin):
            iMin = arrBerat[i]
    return iMin

def rerata(arrBerat):
    rerata = sum(arrBerat) / n
    return rerata

print('Masukkan Banyak Data Berat Balita : ', end=" ")
n = int(input())

for i in range(n):
    masuk = float(input((f'Masukkan Berat Balita Ke-{i+1} : ')))
    arrBerat.append(masuk)
    
print("Berat Balita Maximum : ", hitungMax(arrBerat))
print("Berat Balita Minimum : ", hitungMin(arrBerat))
print("Rerata Berat Balita : ", rerata(arrBerat))