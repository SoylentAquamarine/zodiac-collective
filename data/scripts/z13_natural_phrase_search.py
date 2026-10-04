import re

with open('data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt', encoding='utf-8') as f:
    raw = f.read()
letters_only = re.sub(r'[^A-Za-z]', '', raw).upper()

def satisfies_partition(window):
    return (
        window[0] == window[11] and
        window[2] == window[10] and
        window[4] == window[6] == window[8] and
        window[7] == window[12]
    )

matches = [(i, letters_only[i:i+13]) for i in range(len(letters_only) - 12) if satisfies_partition(letters_only[i:i+13])]

print("total letters:", len(letters_only))
print("windows scanned:", len(letters_only) - 12)
print("matches:", len(matches))
for i, w in matches[:20]:
    print(i, w)
