import numpy as np
import pandas as pd

dates = pd.date_range("2013-01-01", periods=6)

print (dates)

df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list("ABCDE"))

print (df)

df2 = pd.DataFrame({
"A": 1.0,
"B": pd.Timestamp("20130102"),
"C": pd.Series(1, index=list(range(4)), dtype="float32"),
"D": np.array([3] * 4, dtype="int32"),
"E": pd.Categorical(["test", "train", "test", "train"]),
"F": "foo",})

print (df2)
print (df2.describe())
print (df2.T)

x=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print (x)
