alphabet = "abcdefghijklmnopqrstuvwxyz"
lettertonummapping = {}
numtolettermapping = {}
i = 1
for j in range (1):
    for letter in alphabet:
        print(letter + "->" + str(i) )
        numtolettermapping[i] = letter
        lettertonummapping[letter] = i
        i+=1



print(lettertonummapping)
msg1 = "LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl".lower()
msg2 = "WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs".lower()
msg3 = "UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg".lower()
msg4 = "LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu".lower()
msg5 = "LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp".lower()
# Word 1 - word 2
def checkWord(word1, word2):
    string = ""
    i = 0
    for letter in word1:
        if i > len(word1)-1 or i > len(word2)-1:
            break
        index = (lettertonummapping[letter] - lettertonummapping[word2[i]]) % 26
        if index == 0:
            index = 26
        print(numtolettermapping[index], end='')
        string += numtolettermapping[index]
        i+=1

    print("")
    return string
string = checkWord("lpa", "the")
print(string)
# returns eve -> every? Thus we should try see 
string = checkWord("wda", string)
# returns rhvnw
string = checkWord("wdafv", "every")
#returns can yo
string = checkWord("uijml", "rhvnw")
#assume "can you" -> returns rhvnwy
string = checkWord("uijmlt", "canyou")
#returns everyo -> assume everyone
string = checkWord(msg2, string)
# rhvnwynx
string = checkWord(msg2, "everyone")
#returns can you pl -> assume please
string = checkWord(msg3, string)
string = checkWord(msg3, "canyouplease")
#string = checkWord(msg3, string)
string = checkWord(msg1, string) # the secretto
string = checkWord(msg1, string)
string = checkWord(msg2, string) # everyone dese? #everyone deserves?
string = checkWord(msg2, string+"rves")
string = checkWord(msg1, string) # the secret to winni (ng)
string = checkWord(msg1, string + "ng") # the secret to winni (ng)
string = checkWord(msg5, string) # the price of bitcoin i(s)
string = checkWord(msg5, string + "s") # the price of bitcoin i(s)
string = checkWord(msg4, string) # the most important per(son)
string = checkWord(msg4, string + "son")
string = checkWord(msg2, string)  #everyone deserves a hippo(potamus?)
string = checkWord(msg2, string + "potamus")  #everyone deserves a hippo(potamus?) yes
string = checkWord(msg4, string) #in the wo(rld)
string = checkWord(msg4, string + "rld") 
string = checkWord(msg2, string)  #whe(nthey)
string = checkWord(msg2, string +"nthey") 
string = checkWord(msg3, string) #can you please help oliver find the flux capacitor
string = checkWord(msg3, string + "citor")


otp = "rhvnwynxzttsmipsvgkzyzpyokjsnozwxaxzddlhwo"
msg1decode = checkWord(msg1, otp)
msg2decode = checkWord(msg2, otp)
msg3decode = checkWord(msg3, otp)
msg4decode = checkWord(msg4, otp)
msg5decode = checkWord(msg5, otp)


