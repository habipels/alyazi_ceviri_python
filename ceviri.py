def ceviri(a):
    from googletrans import Translator
    trn = Translator()
    t = trn.translate(a,dest="tr")
    return t.text

file = open("1.vtt","r",encoding = "utf-8")

j = 0
for i in file.readlines():
        i = i.strip("\n")
        # liste.append(i.strip())
        # print(liste,"\n------")
        j = 1+j
        
        if j == 3 or j%3==0:
                t = i.strip()
                y = ceviri(t)
                with open("6. Legal considerations.vtt","a",encoding = "utf-8") as file:
                        file.writelines(y+"\n")
        else:
                with open("6. Legal considerations.vtt","a",encoding = "utf-8") as file:
                        file.writelines(i.strip()+"\n")
file.close


