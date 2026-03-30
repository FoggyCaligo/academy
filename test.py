import numpy as np

array = np.random.rand(2,2,2,2)
# print(array)

array.reshape(1,16)
# print(array)

array = np.std([175,177,179,181,183])
print(array,"test")


import pandas as pd
# 데이터프레임 생성
data = {
 '이름': ['Alice', 'Bob', 'Charlie'], 
 '나이': [25, 30, 22], 
 '성별': ['여', '남', '남']}
df = pd.DataFrame(data, index=['A', 'B', 'C'])  # 행 인덱스를 지정
result = df # 전체
result = df.loc[:,"이름"] #이름만 (loc = 이름)
result = df.iloc[:,0] # 첫번째 열만 전체 (iloc = 숫자)
result = df.iloc[0:2,:] # 0~2까지의 행 전체
result = df.loc[:,'이름':'성별'] # 전체 행에서 '이름'~'성별'
result = df.loc[df['나이']>=25] # 나이가 25 이상인 행만
result = df.loc[df['성별']=='남']#성별 남자만
result = df.loc[df.iloc[:,2]=='남']#성별 남자만
# print(result,'\n')



import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/diabetes.csv')
result = df.head()
result = df.info()
result = df.describe()
# result = df.hist(figsize=(10,8))
sns.heatmap(df.corr(),annot=True)#히트맵
plt.show()

# 결측치 평균값으로 채우기
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)  # inplace = True 는 변경된 설정으로 덮어쓴다는 의미
print(df)

#데이터 생성
x = np.linspace(0,10,100)
y = np.sin(x)
# 선 그래프
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.show()