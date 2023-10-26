import pandas as pd
df = pd.read_csv("seoul.csv", encoding = "euc-kr")

df.columns = ['년월', '평균기온','최저기온','최고기온']
print(df.loc[df["평균기온"].idxmax()])

'''
print(df.sort_values(by = "금액", ascending = False).head(3))
'''
'''
name = input()
print(df[df["과일명"].str.contains(name)])
'''
'''
print(df.columns)
df.columns = ["name", " amount", "price","total"]
print(df.columns)
'''
'''
print(df["수량"].idxmax(),df["수량"].idxmin())
print(df.loc[df["수량"].idxmax()])
'''
'''
print(" 최대값 출력\n",df.max())
print(" 최솟값 출력\n", df.min())
print(" 평균값 출력\n", df.mean(numeric_only = True))
'''
