cv = {"name":"Ahmet",
"surname":"Tepegil",
"birth_day":"07/06/1986",
"school":"x uni",
"meslek":"muzisyen",
"foregin_languages":"English, Italien, Japanese"
}   
cv1 = {"name":"Mira",
"surname":"Yigit",
"birth_day":"11/03/1990",
"school":"y uni",
"occupation":"data scientist",
"foregin_languages":"English, French"
} 
cv2 = {"name":"Della",
"surname":"Klein",
"birth_day":"04/10/1990",
"school":"z uni",
"occupation":"developer",
"foregin_languages":"English, Turkish, Spanish"
}
cv3 = {"name":"Selim",
"surname":"Demirbas",
"birth_day":"05/07/1994",
"school":"x uni",
"occupation":"IoT developer",
"foregin_languages":"English, Russian, German"
}
cv4 = {"name":"Idil",
"surname":"Oduncu",
"birth_day":"23/08/1985",
"school":"t uni",
"occupation":"teacher",
"foregin_languages":"English, French, Dutch"}

CV = [cv,cv1, cv2, cv3, cv4]

for i in range(len(CV)):
    print(CV[i].items())
