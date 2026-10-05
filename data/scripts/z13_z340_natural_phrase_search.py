import hashlib

PATH = 'data/external-sources/azdecrypt-doranchak-2026-09-27/z340-solved-transposed.txt'

with open(PATH, 'rb') as f:
    raw_bytes = f.read()
print("file sha256:", hashlib.sha256(raw_bytes).hexdigest())

with open(PATH, encoding='utf-8') as f:
    raw = f.read()
letters_only = ''.join(ch for ch in raw.upper() if ch.isalpha())
print("total letters:", len(letters_only))

def satisfies_partition(window):
    return (
        window[0] == window[11] and
        window[2] == window[10] and
        window[4] == window[6] == window[8] and
        window[7] == window[12]
    )

matches = [(i, letters_only[i:i+13]) for i in range(len(letters_only) - 12) if satisfies_partition(letters_only[i:i+13])]

print("windows scanned:", len(letters_only) - 12)
print("matches:", len(matches))
for i, w in matches:
    print(i, w)
