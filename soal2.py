kluba = []
klubb = []

na = input("Klub A : ")
nb = input("Klub B : ")

a = 1
while a >= 1:
    skor = input("Skor Pertandingan : ")
    skor = skor.split()
    skora = int(skor[0])
    skorb = int(skor[1])
    if skora < 0 or skorb < 0:
        break
    kluba.append(skora)
    klubb.append(skorb)

print(kluba)
print(klubb)

for i in range(len(kluba)):
    if kluba[i] > klubb[i]:
        print("Hasil ",i,": ",na)
    elif kluba[i] < klubb[i]:
        print("Hasil ",i,": ",nb)
    elif kluba[i] == klubb[i] :
        print("Hasil ",i,": SERI")

print("Pertandingan SELESAI.....")