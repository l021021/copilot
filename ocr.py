import pytesseract
from PIL import Image
import csv

# 图片路径
image_path = "D:\\BaiduNetdiskWorkspace\\微信图片_20230612111749.png"

# 读取图片中的文本
text = pytesseract.image_to_string(Image.open(image_path))

# 将文本写入CSV文件
with open(f"D:\\BaiduNetdiskWorkspace\\微信图片_", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['text'])
    writer.writerow([text])