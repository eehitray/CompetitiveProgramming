def c(y):
    news = []
    strs = y.split()
    for i in range(len(strs)):
        if strs[i] == 'is':
            news.append('is not')
        elif strs[i] == 'not':
            news.pop(-1)
        else:
            news.append(strs[i])
    x = ''.join(news)
    if not x[-1] == '.':
        x = x.join('.')
    return x

print(c('It is fair if you do not go.'))
