# Write a Pandas program to convert all the string values to upper, lower cases in a given
# pandas series. Also find the length of the string values.
# s = pd.Series ([‘X’, ‘Y’, ‘T’, ‘Aaba’, ‘Baca’, ‘CABA’, None, ‘bird’, ‘horse’, ‘dog’])

import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

uppercase = s.str.upper()
lowercase = s.str.lower()
length = s.str.len()
result = pd.DataFrame({
    'Original': s,
    'Upper': uppercase,
    'Lower': lowercase,
    'Length': length
})

print(result)
