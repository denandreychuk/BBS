def calculateSeed(x, n):
    return pow(x, 2) % n

def generateSequence(x, n, amount):
    seed = calculateSeed(x, n)
    s0 = seed % 2
    sequence = [s0]

    prevX = seed
    for i in range(1, amount):
        xi = pow(prevX, 2) % n
        si = xi % 2
        sequence.append(si)
        prevX = xi
    return  sequence

def encrypt(text, x, n):
    result = []
    sequence = generateSequence(x, n, len(text))

    for i in range(len(text)):
        char = text[i]
        result.append((ord(char) + sequence[i] - 1040) % n)

    return result

def decrypt(text, x, n):
    result = ""
    sequence = generateSequence(x, n, len(text))

    for i in range(len(text)):
        char = text[i]
        result += chr((char  + (n - sequence[i])) % n + 1040)

    return result

if __name__ == '__main__':
    p = 19
    q = 23
    x = 233
    n = p * q

    encrypted = encrypt("ПРИВЕТ", x, n)
    print(encrypted)

    decrypted = decrypt(encrypted, x, n)
    print(decrypted)
