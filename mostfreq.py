def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
most_frequent.sort(reverse=True)
print('List Descending Order: ',most_frequent )
