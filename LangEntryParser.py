#python 3
'''
This is intended to be used to parse data from the starling.rinet.ru (I do NOT own that site) 
etymology database and post it to Wiktionary (which is also NOT mine)
'''

#Use this with Berber language entries
berDict = { "Ghadames"       : "gha" ,
"Qabyle (Ayt Mangellat)"     : "kab" ,
			"Nefusa"         : "jbn" ,
			"Shawiya"        : "shy" ,
			"Shenwa"         : "cnu" ,
			"Siwa"           : "siz" ,
  "Ahaggar (Tahaggart)"      : "thv" , 
			"Ayr"            : "ay"  ,
			"Tawllemmet"     : "ttq" ,
			"Sened"          : "sds" ,
			"Wargla"         : "oua" ,
			"Zenaga"         : "zen"};

head = "{{reconstructed}}\n==Proto-Berber==\n\n===Etymology===\nFrom {{inh|ber-pro|afa-pro|*   }}.<ref>https://starling.rinet.ru/cgi-bin/query.cgi?basename=\\data\\semham\\afaset</ref>\n\n===Noun===\n{{ber-noun}}\n\n"
head += "# [[   ]]\n\n====Descendants====\n"
tail = "\n====References====\n<references/>"
lang = ""
lemma = ""
key = ""			
fileIn = open("entry.txt")
fileOut = open("wiktEntry.txt","w")

fileOut.write(head)
line = fileIn.readline()
while(line != ""):
	key = line.split(":")[0]
	if(key in berDict):
		lang = berDict[key]
		lemma = line.split(":")[1]
		fileOut.write("* {{desc|%s|tr=%s}}\n" % (lang,lemma.lstrip().rstrip()))
	line = fileIn.readline()
	
fileOut.write(tail)
	
fileIn.close();
fileOut.close();

'''
EXAMPLE INPUT FILE

Ghadames: a-sīn
Nefusa: sīn
Siwa: a-sayn
Ghat: i-sin
Ayr: e-šen
Ahaggar (Tahaggart): esîn
Tawllemmet: e-šen
Taneslemt: e-sen
Sened: i-sîn

Source: https://starling.rinet.ru/cgi-bin/query.cgi?basename=\data\semham\afaset ; Proto-Afro-Asiatic word: sin- ; Meaning: tooth
Copyright 1998 - 2003 by Georgiy Sergeevich Starostin
Retrieved on May 23, 2020

OUTPUT FILE (note: I couldn't find the ISO codes for some of the languages given above)

{{reconstructed}}
==Proto-Berber==

===Etymology===
From {{inh|ber-pro|afa-pro|*   }}.<ref>https://starling.rinet.ru/cgi-bin/query.cgi?basename=\data\semham\afaset</ref>

===Noun===
{{ber-noun}}

# [[   ]]

====Descendants====
* {{desc|gha|tr=a-sīn}}
* {{desc|jbn|tr=sīn}}
* {{desc|siz|tr=a-sayn}}
* {{desc|ay|tr=e-šen}}
* {{desc|thv|tr=esîn}}
* {{desc|ttq|tr=e-šen}}
* {{desc|sds|tr=i-sîn}}

====References====
<references/>
'''