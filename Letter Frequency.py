from operator import itemgetter

def engFreq():
    eng = {
        'E': 12.70, 'O': 7.5, 'S': 6.3, 'L': 4.00, 'U':2.80, 'F': 2.2,
        'p': 1.93,'K': .80, 'Q': .10, 'T': 9.10, 'I': 7.00, 'H': 6.10, 
        'D': 4.3, 'M': 2.4, 'G':2.0, 'B': 1.50, 'J': 0.25, 'Z': 0.10,
        'A': 8.20, 'N': 6.70, 'R': 6.00, 'C': 2.80, 'W': 2.40, 'Y': 2.00,
        'V': 1.00, 'X': 0.20
    }
    en  = sorted(eng.items(), key = itemgetter(1), reverse=True)
    return en

#Gets and returns letter frequencies of cipher text
def letFreq(text):

    """
    Create a dictionary of letters A-Z and count the frequency
    of each in the supplied text.
    Lower case letters are converted to upper case.
    All other characters are ignored.
    The returned data structure is a list as we need to sort it by frequency.
    """

    frequencies = {}

    for asciicode in range(65,91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    for i in frequencies.keys():
        frequencies[i] = round((frequencies[i]/len(text) * 100),2)
        #print(i)

    sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

    
    return sorted_by_frequency

cipher ="UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"
ciph = "BTJNQMFNFTTBHF"
freq_eng = engFreq()
freq_let = letFreq(cipher)


eng_let = tuple(zip(freq_let, freq_eng))
print(eng_let)
plain = ''

#Swaps letters based on
for j in cipher:
    for i in eng_let:
            if ord(i[0][0])== ord(j):
                #print("swapped {bruh} for {burh}".format(bruh=i[0][0], burh=i[1][0]))
                plain += i[1][0]
print(plain)

