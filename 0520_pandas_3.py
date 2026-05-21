import pandas as pd

file_path = 'SuperMarket Analysis.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:

    print(f"找不到檔案 '{file_path}'，請確保該 CSV 檔案與此程式碼放在同一個資料夾中。")
    exit()

print("=== 1. 資料基本檢視 ===")
print(f"資料總筆數（列數）：{df.shape[0]} 筆")
print(f"欄位數量：{df.shape[1]} 個")
print("\n前 5 筆資料內容：")
print(df.head())
print("-" * 50)

filtered_df = df[(df['Branch'] == 'A') & (df['Customer type'] == 'Member')]
print("\n=== 2. 條件篩選結果 ===")
print(f"篩選條件 (Branch='A' 且 Customer type='Member') 的交易筆數：{len(filtered_df)} 筆")
print("-" * 50)

sales_col = 'Total' if 'Total' in df.columns else 'Sales'

product_summary = df.groupby('Product line').agg(
    Total_Sales=(sales_col, 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2)

print("\n=== 3. 各產品線銷售額與平均評分彙總 ===")
print(product_summary)
print("-" * 50)

city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=(sales_col, 'mean'),
    Transaction_Count=(sales_col, 'count')
).round(2)

print("\n=== 4. 依 City 與 Gender 分組彙總 ===")
print(city_gender_summary)
print("-" * 50)

top_product_line = product_summary['Total_Sales'].idxmax()
max_sales_value = product_summary.loc[top_product_line, 'Total_Sales']

print("\n=== 5. 銷售冠軍產品線 ===")
print(f"總銷售額最高的產品線為：【{top_product_line}】")
print(f"該產品線總銷售額為：${max_sales_value:,.2f}")
print("-" * 50)

output_df = product_summary.reset_index()
output_df.columns = ['產品線 (Product line)', '總銷售額 (Total Sales)', '平均評分 (Average Rating)']

output_file_name = '0520_pandas_3OK.CSV'
output_df.to_csv(output_file_name, index=False, encoding='utf-8-sig')

print(f"\n[成功] 已將產品線彙總結果成功導出至檔案：{output_file_name}")