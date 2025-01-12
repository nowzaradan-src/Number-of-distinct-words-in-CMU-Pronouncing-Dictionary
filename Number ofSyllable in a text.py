# To store words and pronunciations
dictionary=[]
# Maximum number of words to process(2000 demanded)
maxWord=2000

# We will use the context manager to help us
with open("cmudict-0.7b", 'r',encoding="ISO-8859-1") as file:
    for line in file:
        #we have to skip command lines to reach to the words
        if line.startswith(";;;"):
            continue
      #When we see a double space we are gonna split the string to separate words and pronunciations
        parts = line.split("  ", 1)
        if len(parts) == 2:
            word, pronunciation = parts
            #When we split the words at the first "(" then we can take the first element so by doing that we extracted (1),(2)... numbers from the words
            word = word.split('(')[0]
            pronunciation = pronunciation
            # we will add words and pronunciations to the list by append function
            dictionary.append((word, pronunciation))

        # Read until 2000's word
        if len(dictionary)>= maxWord:
            break

# Extract distinct words using a set
distinctWords = set(word for word, _ in dictionary)
numDistinctWords = len(distinctWords)

# To calculate the words that has more than one pronunciation we will extract distinct words from the total number of the words
unDistinctWords=maxWord-numDistinctWords
fraction=unDistinctWords/maxWord
print(dictionary)
print("Number of distinct words:", numDistinctWords)
print("Fraction of words that have more than one pronunciation:", fraction)
