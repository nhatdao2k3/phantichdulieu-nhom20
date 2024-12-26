import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = 'supermarket_sales_cleaned.csv'
df = pd.read_csv(filename)

#Biểu đồ tương quan heatmap giữa các cột
dfnum = df.select_dtypes(include=[np.number])
corr_matrix = dfnum.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title('Biểu đồ tương quan giữa các cột số', fontsize=16)
plt.show()


#Biểu đồ top sản phẩm bán ra theo tháng
df_top_product = df.groupby(['Product line', 'Month'])['Quantity'].sum().reset_index()
result = df_top_product.loc[df_top_product.groupby('Month')['Quantity'].idxmax()].reset_index(drop=True)
color_mapping = {
    'Health and beauty': 'skyblue',
    'Electronic accessories': 'orange',
    'Home and lifestyle': 'green',
    'Sports and travel': 'red',
    'Food and beverages': 'purple',
    'Fashion accessories': 'cyan'
}
result['Color'] = result['Product line'].map(color_mapping) # Gán màu sắc tương ứng với từng sản phẩm
plt.figure(figsize=(10, 6))
bars = plt.bar(result['Month'].astype(str), result['Quantity'], color=result['Color'], alpha=0.8)
# Thêm chú thích (legend) cho từng màu
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in color_mapping.values()]
plt.legend(legend_handles, color_mapping.keys(), title="Products line", loc="upper left", bbox_to_anchor=(0.8, 1), fontsize=10)
plt.title('Top sản phẩm bán nhiều nhất theo tháng', fontsize=14)
plt.xlabel('Tháng', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
plt.show()

#Biểu đồ tổng doanh thu theo từng thành phố
df_city = df.groupby('City')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_city['City'], df_city['Total'], color='skyblue', width=0.3)
plt.xlabel('Thành phố', fontsize=12)
plt.ylabel('Tổng doanh thu', fontsize=12)
plt.title('Tổng doanh thu theo từng thành phố', fontsize=14)
# Hiển thị số liệu trên mỗi cột
for i, revenue in enumerate(df_city['Total']):
    plt.text(i, revenue + 5000, f'{revenue}', ha='center', va='bottom', fontsize=10)
plt.show()

# #Biểu đồ doanh thu theo từng loại hình thanh toán
df_payment = df.groupby('Payment')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_payment['Payment'], df_payment['Total'], color='skyblue', width=0.3)
plt.xlabel('Loại hình thanh toán', fontsize=12)
plt.ylabel('Doanh thu', fontsize=12)
plt.title('Tổng doanh thu theo từng loại hình thanh toán', fontsize=14)
# Hiển thị số liệu trên mỗi cột
for i, total in enumerate(df_payment['Total']):
    plt.text(i, total + 5000, f'{total}', ha='center', va='bottom', fontsize=10)
plt.show()


# #Biểu đồ doanh thu theo kiểu khách hàng
df_cus = df.groupby('Customer type')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_cus['Customer type'], df_cus['Total'], color='skyblue', width=0.4)
plt.xlabel('Kiểu khách hàng', fontsize=12)
plt.ylabel('Doanh thu', fontsize=12)
plt.title('Tổng doanh thu theo kiểu khách hàng', fontsize=14)
# Hiển thị số liệu trên mỗi cột
for i, total in enumerate(df_cus['Total']):
    plt.text(i, total + 5000, f'{total}', ha='center', va='bottom', fontsize=10)
plt.show()

#Biểu đồ doanh thu theo giới tính khách hàng
df_gender = df.groupby('Gender')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_gender['Gender'], df_gender['Total'], color='skyblue', width=0.4)
plt.xlabel('Giới tính', fontsize=12)
plt.ylabel('Doanh thu', fontsize=12)
plt.title('Tổng doanh thu theo giới tính khách hàng', fontsize=14)
# Hiển thị số liệu trên mỗi cột
for i, total in enumerate(df_gender['Total']):
    plt.text(i, total + 5000, f'{total}', ha='center', va='bottom', fontsize=10)
plt.show()

#Biểu đồ boxplot xếp hạng đánh giá theo từng chi nhánh
plt.figure(figsize=(10, 6))
sns.boxplot(x='Branch', y='Rating', data=df, palette="Set2", linewidth=1.5, width=0.4)
plt.title('Boxplot đánh giá theo từng chi nhánh', fontsize=16)
plt.xlabel('Chi nhánh', fontsize=12)
plt.ylabel('Đánh giá', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

#Biểu đồ doanh thu theo chi nhánh
df_branch = df.groupby('Branch')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_branch['Branch'], df_branch['Total'], color='skyblue', width=0.4)
plt.xlabel('Chi nhánh', fontsize=12)
plt.ylabel('Doanh thu', fontsize=12)
plt.title('Tổng doanh thu theo từng hãng chi nhánh', fontsize=14)
# Hiển thị số liệu trên mỗi cột
for i, total in enumerate(df_branch['Total']):
    plt.text(i, total + 5000, f'{total}', ha='center', va='bottom', fontsize=10)
plt.show()

#Biểu đồ top sản phẩm của các chi nhánh
top_product_branch = df.groupby(['Product line', 'Branch'])['Quantity'].sum().reset_index()
result = top_product_branch.loc[top_product_branch.groupby('Branch')['Quantity'].idxmax()].reset_index(drop=True)
print(result)
color_mapping = {
    'Health and beauty': 'skyblue',
    'Electronic accessories': 'orange',
    'Home and lifestyle': 'green',
    'Sports and travel': 'red',
    'Food and beverages': 'purple',
    'Fashion accessories': 'cyan'
}
result['Color'] = result['Product line'].map(color_mapping) # Gán màu sắc tương ứng với từng sản phẩm
plt.figure(figsize=(10, 6))
bars = plt.bar(result['Branch'].astype(str), result['Quantity'], color=result['Color'], alpha=0.8, width=0.3)
# Thêm chú thích (legend) cho từng màu
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in color_mapping.values()]
plt.legend(legend_handles, color_mapping.keys(), title="Products line", loc="upper left", bbox_to_anchor=(0.8, 1), fontsize=10)
plt.title('Top sản phẩm bán nhiều nhất theo chi nhánh', fontsize=14)
plt.xlabel('Chi nhánh', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
plt.show()

#Tổng sản phẩm bán được theo thời gian
df_month_quantity = df.groupby('Month')['Quantity'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(df_month_quantity['Month'], df_month_quantity['Quantity'], marker='o', color='royalblue', linestyle='-', linewidth=2, markersize=8, label='Tổng sản phẩm')
plt.xlabel('Tháng', fontsize=12, labelpad=10)
plt.ylabel('Tổng số sản phẩm', fontsize=12, labelpad=10)
plt.title('Tổng số sản phẩm bán được theo từng tháng', fontsize=14, pad=20)
plt.grid(True, linestyle='--', alpha=0.6)
for i, total in enumerate(df_month_quantity['Quantity']):
    plt.text(df_month_quantity['Month'][i], total + 5000, f'{total}', ha='center', va='bottom', fontsize=10, color='darkblue', fontweight='bold')
plt.xticks(df_month_quantity['Month'], rotation=45, ha='right', fontsize=10)
plt.legend()
plt.show()
