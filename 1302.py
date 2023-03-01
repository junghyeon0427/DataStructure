from collections import Counter

N = int(input())

book_list = list()

for _ in range(N):
    book_list.append(input())

book_cnt = Counter(book_list)

ret = sorted(book_cnt.most_common())
sorted_ret = sorted(ret, key=lambda x: x[1], reverse=True)

print(sorted_ret[0][0])
