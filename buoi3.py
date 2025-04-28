import pandas as pd 

df = pd.read_excel(r"C:\Users\DELL\Downloads\exercise_data.xlsx")
print(df)

df['Ngày'] = df['Ngày'].fillna(method='ffill')
print(df)

df.loc[20, 'Ngày'] = '2020/12/20'
print(df)
# 2. Xử lý ô trống trong cột "Lượng calo"
# Cách 1: Điền bằng giá trị trung bình của cột
mean_calories = df['Lượng calo'].mean()
df['Lượng calo'] = df['Lượng calo'].fillna(mean_calories)

print(df)
print("-" * 50)

# Sửa ngày của '20201226' thành '2020/12/24'
df.loc[24, 'Ngày'] = '2020/12/24'
print(df)

# Sửa hàng thứ 7 (index 5) thành 45
df.loc[5, 'Thời lượng'] = 45
print(df)
print("-" * 50)

# Loại bỏ các hàng trùng lặp
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame sau khi loại bỏ các hàng trùng lặp:")
print(df_no_duplicates)
