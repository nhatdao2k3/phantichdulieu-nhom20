import pandas as pd

df = pd.read_csv("supermarket_sales.csv")

#BẮT ĐẦU QUÁ TRÌNH TIỀN XỬ LÝ DỮ LIỆU CHO PHÂN TÍCH MÔ TẢ
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
print('---------------------------------')
print("Dòng, cột:", df.shape)
print('---------------------------------')
print("\nThông tin dữ liệu: ", df.info())

#Kiểm tra tỷ lệ lỗi thiếu data
missing_df = df.isnull().sum()  # Tổng số giá trị thiếu cho từng cột
total_data = len(df)  # Tổng số hàng trong dataframe
missing_data = (missing_df / total_data) * 100  # Tính tỷ lệ %
print('---------------------------------')
print(f"TỶ LỆ THIẾU DỮ LIỆU:\n{missing_data}")

#Kiểm tra data bị trùng
duplicate_rows = df.duplicated().sum()  # Lọc các hàng bị trùng lặp
print('---------------------------------')
print(f"SỐ LƯỢNG DATA BỊ TRÙNG lẶP: {duplicate_rows}")
df = df.drop_duplicates() # Xoá các dòng data bị trùng lặp

#Đếm số lượng data riêng biệt của từng cột
print('---------------------------------')
print("SỐ LƯỢNG DATA RIÊNG BIỆT:")
for column in df.columns:
    num_distinct_values = len(df[column].unique())
    print(f"{column} : {num_distinct_values} distinct values")

# Chuyển đổi cột Date sang datetime object với định dạng phù hợp
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
#Tạo thêm cột Month
df['Month'] = ''
df['Month'] = df['Date'].dt.strftime('%m')

# Loại bỏ các cột không cần thiết
columns_to_drop = ['Invoice ID', 'Tax 5%', 'gross margin percentage']
dfcleaned = df.drop(columns=columns_to_drop, errors='ignore')

#Tóm lược dữu liệu
dfnum = df.select_dtypes(include=['number']).drop(columns=['gross margin percentage'])
counts = dfnum.count()
means = dfnum.mean()
medians = dfnum.median()
modes = dfnum.mode()
maxes = dfnum.max()
mines = dfnum.min()
q1 = dfnum.quantile(0.25)
q2 = dfnum.quantile(0.5)
q3 = dfnum.quantile(0.75)
iqr = q3 - q1
variances = dfnum.var()
std_devs = dfnum.std()
data = {'Count': [i for i in counts],
        'Min': [i for i in mines],
        'Max': [i for i in maxes],
        'Mean': [i for i in means],
        'Median': [i for i in medians],
        'Mode': [i for i in modes.values[0]],
        'Q1': [i for i in q1],
        'Q2': [i for i in q2],
        'Q3': [i for i in q3],
        'IQR': [i for i in iqr],
        'Variance': [i for i in variances],
        'Stdev': [i for i in std_devs],
        }
df1 = pd.DataFrame(data)
df1.index = dfnum.keys()
dfsummary = df1.transpose()
print('---------------------------------')
print("BẢNG TÓM LƯỢC DỮ LIỆU:")
print(dfsummary)

#Lưu bảng tóm lược và data đã làm sạch vào file mới
dfcleaned.to_csv('supermarket_sales_cleaned.csv', index=False)
dfsummary.to_csv('supermarket_sales_summary.csv', index=True)

