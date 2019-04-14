import re


def decodeBitsAdvanced(bits):
    bits = bits.strip('0')
    ones = []
    zeros = []
    index = 0

    while index < len(bits):
        bit = bits[index]
        next_index = bits.find(str(int(not int(bit))), index + 1)
        if next_index < 0:
            next_index = len(bits)

        if int(bit):
            ones.append((next_index - index, len(ones) + len(zeros)))
        else:
            zeros.append((next_index - index, len(ones) + len(zeros)))
        index = next_index
    ones_clusters = get_clusters(list(set(o[0] for o in ones)), 1)
    dots, dashes = [], []
    if len(ones_clusters) == 2:
        dots, dashes = ones_clusters
    else:
        if len(zeros) > 0 and min(ones_clusters[0]) > min(z[0] for z in zeros):
            dashes = ones_clusters[0]
        else:
            dots = ones_clusters[0]
    between_char_pause, between_word_pause = [], []
    zeros_clusters = get_clusters(list(set(z[0] for z in zeros)), 2)
    if len(zeros_clusters) == 3:
        in_char_pause, between_char_pause, between_word_pause = zeros_clusters
    elif len(zeros_clusters) == 2:
        pass
    elif len(zeros_clusters[0]) > 0:
        single_cluster = zeros_clusters[0]
        if len(dashes) > 0 and max(dashes) < min(single_cluster) or len(dots) > 0 and max(dots) * 6 < min(single_cluster):
            between_word_pause = single_cluster
        elif len(dashes) > 0 and max(dashes) == max(single_cluster) or len(dots) > 0 and max(dots) * 2 < min(single_cluster):
            between_char_pause = single_cluster
    result = []

    for i in range(len(ones) + len(zeros)):
        if ones[0][1] == i:
            o = ones.pop(0)
            if o[0] in dots:
                result.append('.')
            else:
                result.append('-')
        else:
            z = zeros.pop(0)
            if z[0] in between_word_pause:
                result.append('   ')
            elif z[0] in between_char_pause:
                result.append(' ')

    return ''.join(result)


def get_clusters(numbers, k):
    if len(numbers) < 2:
        return [numbers]
    numbers.sort()
    diffs = []
    for i in range(1, len(numbers)):
        diffs.append((numbers[i] - numbers[i - 1], i))
    cuts = sorted(map(lambda p: p[1], sorted(diffs, key=lambda d: (d[0], -d[1]))[-k:]))
    cuts.insert(0, 0)
    cuts.append(len(numbers) + 1)
    return [numbers[cuts[i - 1]:cuts[i]] for i in range(1, len(cuts))]


def decodeBits(bits):
    bits = bits.strip('0')
    transmission_rate = min(len(m) for m in re.findall(r'1+|0+', bits))

    return bits[::transmission_rate].replace('111', '-').replace('1', '.').replace('0000000', '   ').replace('000',
                                                                                                             ' ').replace(
        '0', '')


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
