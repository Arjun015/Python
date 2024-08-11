#slicing of string with jump/skip values

name = "czechoslovakia is in Europe"

qwe = len(name)
print(qwe)

print(name[0:qwe:3])
print(name[0:qwe:2])
print(name[0:qwe:5])
print(name[5:qwe:4])
print(name[0:qwe:10])
print(name[:qwe:])
print(name[0:qwe:])
print(name[::6])



# string = 1-string is the store the sequence of character or collection of character 
#          2- it written by double quote (""), single(''),triple(''' ''')


#string methods -length --this is the property 
# methods- len() , find() , count() , title() , replace()

# program 1

song ='''Junoon junoon junoon junoon
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
Junoon junoon junoon junoon'''

print(song)
print(len(song))
aa= song.find("Junoon") #str.find("parameter")location of first instance
print(aa)

print(song.count("Junoon"))

ABC = song.title()
print(ABC.count("Junoon"))

gg = ABC.replace("Junoon","Afternoon")
print(gg)

print("-----------------------------------------------")
# Program 2 
music = '''O.. huzoor
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
Tera tera tera suroor'''

# FIND NUMBER OF STRING "tera"

print(len(music))
print(music.find("tera"))  # 16

print(music.find("Tera"))  #11

print(music.find("Tera tera tera suroor")) #


# REPLACE "tera" WITH  "mera"

print(music.replace("tera","mera"))


# FIND THE FIRST OCCURENCE OF "poocho"

print(music.find("poocho")) # 326


# CHECK IF ANY DIGIT IS IN THE STRING USING isalpha()

print(music.isalpha())