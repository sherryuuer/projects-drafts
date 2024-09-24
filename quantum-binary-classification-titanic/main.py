import pandas as pd
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print('train has {} rows and {} columns'.format(*train.shape))
print('test has {} rows and {} columns'.format(*test.shape))
print(train.info())

# Missing value processing
print(f"{len(train)} rows")  # 891 rows
# 1- Missing Values
# option 1
# You only have two passengers without it. This is bearable
train = train.dropna(subset=["Embarked"])  # 889 rows
print(f"{len(train)} rows after dropna of Embarked colum")
# option 2
# You only have very few information about the cabin, let's drop it
train = train.drop("Cabin", axis=1)
print(f"{len(train)} rows after drop Cabin colum")  # 889 rows
# option 3
# The age misses quite a few times. But intuition
# says it might be important for someone's chance to survive.
mean = train["Age"].mean()
train["Age"] = train["Age"].fillna(mean)
