# TODAYS CODE =========================================

#Slicing of string with Jump/skip values
name = "czechoslovakia is in Europe"
len_1 = len(name)
print(name)
print(name[0:len_1:3])

# ---------------------------------------------------------


# Study various string Methods

himesh1 = '''
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Aye meri tamanna
Bin tere kahin na
Aye meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Hai meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Main teri yaadon mein
Gumshuda humnashin
Jaan-e-jaan tum
Jahan zindagi hai wahi
Tere khayalon se
Jude mere raat din
Jeena mera hai bin
Tere ab na mumkin


Aye meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon


Junoon mujhpe chhaaya
Tere ishq ka junoon


Kyon tere ishq mein
Dil kahin na lage
Tanha yeh dil jale
Ek pal na dhale
In dhadkano se aati
Hai ab to yeh sada
Teri hi khwaahish ab
To hai tera hi nasha


Aye meri tamanna
Bin tere kahin na
Aaye mujhe sukoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon
Junoon junoon junoon junoon.
'''

print(himesh1)
print(len(himesh1))
print(himesh1.find("Junoon")) #str.find("parameter") location of first instance
print(himesh1.count("Junoon"))
himesh2 = himesh1.title()       
print(himesh2.count("Junoon"))
himesh3 = himesh2.replace("Junoon" , "Afternoon")
print(himesh3)



# string Methods-----> len() , find() , count() , title() , replace() 



himesh5= '''
O.. huzoor
Tera tera tera suroor
Meri baatein, meri yaadein, tanha raatein
Tera tera tera suroor
Mere kisse, meri saanein, meri aahein
Tera tera tera suroor
O. huzoor
Tera tera tera suroor
Tujh mein basi hai meri duniya
Tujh mein rawaan hai meri khushiya
Tujh se ummeedein mujhko badi
Todd na dena dil ki kadi
Iss dard ka ehsaas poocho na
Poocho na poocho na, poocho na
Poocho na sanam
Mere armaan, mere lamhe, mere nagme
Tera tera tera suroor
Tanhaiyon mein tu hi shaamil,
Tere bina jeena bada mushkil
Tere siva kuch na aaye nazar
Nazron pe chaaya tera manzar
Rab hi jaane ye pyaas kaisi hai
Dekho na dekho na dekho na
Dekho na sanam
Meri dhadkan, meri tadpan, mera jeevan
Tera tera tera suroor
Meri baatein, meri yaadein, tanha raatein
Tera tera tera suroor
'''
# FIND NUMBER OF STRING "tera"
# REPLACE "tera" WITH  "mera"
# FIND THE FIRST OCCURENCE OF "poocho"
# CHECK IF ANY DIGIT IS IN THE STRING USING isalpha()
