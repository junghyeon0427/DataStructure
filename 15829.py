L = int(input())
string = input()

hash_val = 0

for i, j in enumerate(string):
    hash_val += (ord(j) - 96) * (31 ** i)
    if hash_val >= 1234567891:
        hash_val %= 1234567891

print(hash_val)
