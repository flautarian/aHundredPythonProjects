
""" Defininition of a dictionary to map Morse code representation of ASCII basic code """
morse_dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

""" Function to convert ASCII text to uppercase to Morse code """
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_dictionary:
            morse_code.append(morse_dictionary[char])
        else:
            morse_code.append(' ')
    return ' '.join(morse_code)

# Input from the user
input_text = input("Enter text to convert to Morse code: ")
morse_code = text_to_morse(input_text)
print("Morse code: " + morse_code)
