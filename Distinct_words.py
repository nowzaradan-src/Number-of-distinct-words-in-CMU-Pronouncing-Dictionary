import re
dictionary=[]
syllablesSounds = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}

with open('cmudict-0.7b','r',encoding="ISO-8859-1") as file:
    for line in file:
        if line.startswith(";;;"):
            continue
        # When we see a double space we are gonna split the string to separate words and pronunciations
        parts = line.split("  ", 1)
        if len(parts) == 2:
            word, pronunciation = parts
            # When we split the words at the first "(" then we can take the first element so by doing that we extracted (1),(2)... numbers from the words
            word = word.split('(')[0]
            pronunciation = pronunciation
            dictionary.append((word, pronunciation))
            # we will add words and pronunciations to the list by append function

#We will evaulate the number of syllbal in a given pronunciation by this function
def numSyllablesPronunciation(pronunciation):
    phonemes = pronunciation.split()
    return sum(1 for phoneme in phonemes
               if phoneme[:2] in syllablesSounds)

def estimateSyllables(text, dictionary):
    #We are gonna use dictionary set to find the corresponding pronunciation with lower complexity
    # to do that we will convert dictionary list to a dictionary set
    dict_lookup = {word: pronunciation for word, pronunciation in dictionary}
    #Here we will take each word as an element by using regular expression modul
    words = re.findall(r"\b\w+\b", text)
    numSyllables = 0
    for word in words:
        #We have to make sure that words are uppercase otherwise there can't be a match
        wordUpper = word.upper()
        if wordUpper in dict_lookup:
            pronunciation = dict_lookup[wordUpper]
            syllables = numSyllablesPronunciation(pronunciation)
            #Summing up syllables
            numSyllables += syllables

    return numSyllables

text = """This is a test text car"""

totalSyllables = estimateSyllables(text, dictionary)
print("Total syllables in the text:",totalSyllables)