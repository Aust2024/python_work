#替換CSV檔案內部文字

#os模組：控制和操作電腦內的文件操作電腦功能
import os
#csv模組：讀取和寫入csv文件
import csv

#指定資料夾路徑
folder_path = r'C:\Users\User\Desktop\testtt\01'

#取得資料夾內所有CSV檔案
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

#欄位名稱的替換對應表
replace_dict = {
    "113.": "2024.",
    "交易日期": "transaction_date",
    "種類代碼": "category_code",
    "作物代號": "crop_code",
    "作物名稱": "crop_name",
    "市場代號": "market_code",
    "市場名稱": "market_name",
    "上價(元_公斤)": "highest_price",
    "中價(元_公斤)": "median_price",
    "下價(元_公斤)": "lowest_price",
    "平均價(元_公斤)": "average_price",
    "交易量(公斤)": "transaction_volume"
}

#用for迴圈處理每個CSV檔案
for csv_file in csv_files:
    input_file = os.path.join(folder_path, csv_file)
    
    #暫存行內容
    rows = []
    
    #讀取並修改CSV檔案中的內容
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        
        #for迴圈讀取CSV並進行替換
        for row in reader:
            new_row = []
            for item in row:
                #逐一對表中的key值進行替換
                for old, new in replace_dict.items():
                    item = item.replace(old, new)
                new_row.append(item)
            rows.append(new_row)

    #將修改後的內容寫回原檔案
    with open(input_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        
        #寫入所有修改過的行內容
        writer.writerows(rows)

    print(f'檔案 {csv_file} 已成功修改')

