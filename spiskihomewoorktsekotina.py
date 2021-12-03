l = ["крот", "белка", "вухухоль"]
nl=[]
max=0
for e in l:
    x=len(e)
    if x>max:
        max=x
for e in l:
    nl.append(e.ljust(max,"_"))
print(nl)









#indeks_list=["1 – Tallinn"
           # "2 – Narva, Narva-Jõesuu"
           # "3 – Kohtla-Järve"
           # "4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
           # "5 – Tartu linn"
           # "6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
           # "7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
           # "8 – Pärnumaa"
           # "9 – Läänemaa, Hiiumaa, Saaremaa"]
#indeks_list=list(indeks)
#int(input"")

