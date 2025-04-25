# Whenever your friends John and Judy visit you together, y’all have a party. Given a
# DataFrame with 10 rows representing the next 10 days of your schedule and whether John
# and Judy are scheduled to make an appearance, insert a new column
# called days_til_party that indicates how many days until the next party.
# days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn’t
# occur but will occur the next day, etc.

import pandas as pd

data = {
    'John': [True, False, True, False, True, True, False, False, True, True],
    'Judy': [False, True, True, True, False, True, False, True, False, True]
}

df = pd.DataFrame(data)

df['days_till_party'] = df['John'] & df['Judy']

print(df['days_till_party'])

k=[]
m=0
for i in range(len(df['days_till_party'])):
     if(df['days_till_party'][i]==True):
         k.append(m)
         m=0
     else:
         m-=1
i=0
p=0
while(i<len(k)):
    if(k[i]==0):
        df['days_till_party'][p] = 0
        p+=1
        i+=1
    else:
        df['days_till_party'][p] = (k[i]*-1)
        k[i]+=1
        p+=1
        
print(df)