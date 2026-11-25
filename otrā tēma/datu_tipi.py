a = "5"
b = 5
c = 5.5
print(type(a))
print(type(b))
print(type(c))
print(a + a)
vards = input("Ievadi varoņa vārdu: ")
punkti = int(input("Ievadi bāzes punktus: "))
reizinatajs = float(input("Ievadi reizinātāju: "))
kopa = punkti * reizinatajs
print(vards, "ieguva", kopa, "punktus")


# ValueError atrodas 9. rindā.
# ValueError notiek, jo nepieņem komatu.
# Tas kalpo kā atdalītājs lai uzskaitītu vairākus elementus sarakstos, funkciju argumentos vai izveidotu datu struktūru, ko sauc par kortežu.