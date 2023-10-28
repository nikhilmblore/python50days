# Escape characters
# \n
# \t
# \r
# \'
# \"
# \b	Backspace	
# \f	Form Feed	
# \000	Octal value	
# \xhh	Hex value
# ---------------------------
strList = [
    "Bengaluru\tis \nKarnataka's \"capital\""
    ,"use of\bbackspace"
    ,"use of\fformfeed"
    ,"use of \116\151\153\150\151\154 \'\\000\' octal"
    ,"use of \x4e\x69\x6b\x68\x69\x6c \'\\x48\'"
    ]


for string in strList:
    print(strList.index(string))
    print(string)

