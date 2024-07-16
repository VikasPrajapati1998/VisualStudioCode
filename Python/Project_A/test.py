with open('visualization.csv', 'r+') as f:
    data = f.read()
    next(f)
    print(data)