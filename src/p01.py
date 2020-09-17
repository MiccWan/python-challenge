from string import ascii_lowercase

def caesar(plaintext, shift):
    alphabet = ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    d = {}
    for i in range(len(alphabet)):
        d[alphabet[i]] = shifted_alphabet[i]
    return ''.join(map(lambda x: d.get(x, x), plaintext))


msg = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
print(caesar(msg, 2))

print(caesar('map', 2))

# ocr