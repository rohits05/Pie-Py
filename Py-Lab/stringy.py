# Getting started with String
str = 'Hey, Learner!!'
print(str)

# How you can use '/""/''' into string
leap = "Let's start the Adventure..."
print(leap)

namify = '''I'm "Rohit"'''
print(namify)
# ____________________________________________________________________

# Define multiple string by using '''/""""
champak = '''Jeene ke hai
Chaar Din,

Ohooo hooo ho ho hooo..
Ehiiii hii hiiii hiiiiiiiiii _
'''
print(champak)
# _______________________________________________________________________-


# Access Idx of String
# 0 -> 1st Idx & -1 -> Last Idx
# Slicing [start:end] -- excluding end
# [:] returns the entire cloned one
lassi = 'Creamy Wali mastt Chilled'
print(lassi[0], lassi[-1], lassi[7:11], lassi[:11], lassi[-13:])

Rabdi = 'Amul Doodh ki gaadhi bani'
print(Rabdi[:])
print(Rabdi[1:-1], "\n")
# ____________________________________________________________________________


# Formatted Strings
odinSson = 'Thor'
his_soulMate = "Jane"
mjolnir = odinSson + ' & [' + his_soulMate + '] are best Marvel Couple.'
storm_breaker = f'{odinSson}_{his_soulMate} See-You on 7J!'
print(mjolnir)
print(storm_breaker)


# String methods
bhramastra = 'Kesariya tera Ishq hai piya....'
# len() , upper() , lower() , title () , find() , replace() , '.....' in stringy_name
print(len(bhramastra))
print(bhramastra.upper(), bhramastra.lower())
print(bhramastra.find('h'))  # returns -1 for NF
print(bhramastra.replace('piya', 'cutuyii'), bhramastra.replace('t', 'T'))
print('piya' in bhramastra)  # performs bool checking operation
