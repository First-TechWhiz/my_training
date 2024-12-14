def fake_divide(first, second):
    if second == 0:
        results = 'Ошибка'
    else:
        results = first / second
    return results

#print(fake_divide(12, 0))