import re

def decodeBits(bits):
    bits = bits.strip('0')
    transmission_rate = min(len(m) for m in re.findall(r'1+|0+', bits))
    morse_code = []
    index = 0
    while index < len(bits):
        bit = bits[index]
        if bit == '1':
            next_index = bits.find('0', index)
            if next_index < 0:
                next_index = len(bits)
            if next_index - index == transmission_rate:
                morse_code.append('.')
            else:
                morse_code.append('-')
        else:
            next_index = bits.find('1', index)
            if next_index < 0:
                next_index = len(bits)
            if next_index - index == transmission_rate * 3:
                morse_code.append(' ')
            elif next_index - index == transmission_rate * 7:
                morse_code.append('   ')
        index = next_index

    return ''.join(morse_code)


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))


MORSE_CODE = {'.-...': '&',
              '--..--': ',',
              '....-': '4',
              '.....': '5',
              '...---...': 'SOS',
              '-...': 'B',
              '-..-': 'X',
              '.-.': 'R',
              '.--': 'W',
              '..---': '2',
              '.-': 'A',
              '..': 'I',
              '..-.': 'F',
              '.': 'E',
              '.-..': 'L',
              '...': 'S',
              '..-': 'U',
              '..--..': '?',
              '.----': '1',
              '-.-': 'K',
              '-..': 'D',
              '-....': '6',
              '-...-': '=',
              '---': 'O',
              '.--.': 'P',
              '.-.-.-': '.',
              '--': 'M',
              '-.': 'N',
              '....': 'H',
              '.----.': "'",
              '...-': 'V',
              '--...': '7',
              '-.-.-.': ';',
              '-....-': '-',
              '..--.-': '_',
              '-.--.-': ')',
              '-.-.--': '!',
              '--.': 'G',
              '--.-': 'Q',
              '--..': 'Z',
              '-..-.': '/',
              '.-.-.': '+',
              '-.-.': 'C',
              '---...': ':',
              '-.--': 'Y',
              '-': 'T',
              '.--.-.': '@',
              '...-..-': '$',
              '.---': 'J',
              '-----': '0',
              '----.': '9',
              '.-..-.': '"',
              '-.--.': '(',
              '---..': '8',
              '...--': '3'}
