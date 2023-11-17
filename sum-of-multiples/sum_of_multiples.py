def sum_of_multiples(limit, multiples):
    results = set([])
    for val in multiples:
        values = []
        for x in range(limit):
            if (val * x) < limit:
                values.append(val * x)
        results = results.union(set(values))
    total = 0
    for item in results:
        total += item
    return total
