import pandas as pd

data = {'name': ['John', 'Paul', 'George', 'Ringo'],
        'year': [1940, 1942, 1943, 1940],
        'instrument': ['guitar', 'bass', 'guitar', 'drums']}

data2 = {'nombre': ['Pablo', 'Jose', 'Carlos', 'Pedro'],
        'ano': [1991, 1992, 1983, 1990],
        'instrumento': ['piano', 'flute', 'violin', 'trombon']}

df= pd.DataFrame(data)
df2= pd.DataFrame(data2)
print(df)
print(df2)
print ('++++++++++++++++')
print(df.query('year != 1940')) #| instrument == "guitar"'))
print(df2.query('ano == 1940 | instrumento == "flute"'))

