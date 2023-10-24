def n_gram(text, n):
    return [text[i:i+n] for i in range(len(text)-n+1)]

cleaned = ['mary','park','minseo','.']

print(n_gram(cleaned,3))