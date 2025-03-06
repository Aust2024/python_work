#產生六都菜價分析折線圖

import pymysql
import pandas as pd
import matplotlib.pyplot as plt

# MySQL 連線資訊
db_host = 'localhost'
db_user = 'root'
db_password = '12345678'
db_name = 'world'
db_table = 'produce'

# 連接 MySQL 資料庫
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# 第一條查詢數據
query1 = f"""SELECT '台北市' as city, transaction_date, round(AVG(average_price)
,2) AS average_price  FROM {db_table} WHERE crop_code = '812' AND (market_code
 = 104 OR market_code = 105 OR market_code = 109) AND transaction_date < 
'2024-09-01' GROUP BY transaction_date ORDER BY transaction_date"""
df1 = pd.read_sql(query1, connection)

# 第二條查詢數據
query2 = f"""SELECT '新北市' as city, transaction_date, round(AVG(average_price)
,2) AS average_price  FROM {db_table} WHERE crop_code = '812' AND (market_code
 = 220 OR market_code = 241) AND transaction_date < '2024-09-01' GROUP BY 
 transaction_date ORDER BY transaction_date"""
df2 = pd.read_sql(query2, connection)

# 第三條查詢數據
query3 = f"""SELECT '桃園市' as city, transaction_date, round(AVG(average_price)
,2) AS average_price  FROM {db_table} WHERE crop_code = '812' AND market_code
 = 338 AND transaction_date < '2024-09-01' GROUP BY transaction_date ORDER BY
 transaction_date"""
df3 = pd.read_sql(query3, connection)

# 第四條查詢數據
query4 = f"""SELECT '臺中市' as city, transaction_date, round(AVG(average_price)
,2) AS average_price  FROM {db_table} WHERE crop_code = '812' AND (market_code
 = 400 OR market_code = 420 OR market_code = 423) AND transaction_date <
'2024-09-01' GROUP BY transaction_date ORDER BY transaction_date"""
df4 = pd.read_sql(query4, connection)

# 第五條查詢數據
query5 = f"""SELECT '臺南市' as city, transaction_date, round(AVG(average_price)
,2) AS average_price  FROM {db_table} WHERE crop_code = '812' AND market_code
 = 700 AND transaction_date < '2024-09-01' GROUP BY transaction_date ORDER BY
 transaction_date"""
df5 = pd.read_sql(query5, connection)

# 第六條查詢數據
query6 = f"""SELECT '高雄市' as city, transaction_date, round(AVG(average_price)
,2) AS average_price  FROM {db_table} WHERE crop_code = '812' AND (market_code
 = 800 OR market_code = 830) AND transaction_date < '2024-09-01' GROUP BY
 transaction_date ORDER BY transaction_date"""
df6 = pd.read_sql(query6, connection)

# 關閉資料庫連接
connection.close()

# 檢查數據
print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)

# 將 'transaction_date' 轉換為 datetime 類型
df1['transaction_date'] = pd.to_datetime(df1['transaction_date'])
df2['transaction_date'] = pd.to_datetime(df2['transaction_date'])
df3['transaction_date'] = pd.to_datetime(df3['transaction_date'])
df4['transaction_date'] = pd.to_datetime(df4['transaction_date'])
df5['transaction_date'] = pd.to_datetime(df5['transaction_date'])
df6['transaction_date'] = pd.to_datetime(df6['transaction_date'])

# 繪圖 - 折線圖顯示兩組數據的平均價格隨時間的變化
plt.figure(figsize=(16, 10))

# 繪製第1~6條折線
plt.plot(df1['transaction_date'], df1['average_price'], marker='o', 
         color='tab:blue', label='台北市')
plt.plot(df2['transaction_date'], df2['average_price'], marker='x', 
         color='tab:orange', label='新北市')
plt.plot(df3['transaction_date'], df3['average_price'], marker='D', 
         color='tab:green', label='桃園市')
plt.plot(df4['transaction_date'], df4['average_price'], marker='s', 
         color='tab:red', label='臺中市')
plt.plot(df5['transaction_date'], df5['average_price'], marker='p', 
         color='tab:purple', label='臺南市')
plt.plot(df6['transaction_date'], df6['average_price'], marker='H', 
         color='tab:brown', label='高雄市')

# 設置標籤和標題
plt.xlabel('交易日期')
plt.ylabel('平均價(元_公斤)')
plt.title('六都菜價波動')

# 圖表美化
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# 顯示圖表
plt.show()



