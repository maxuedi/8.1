import csv
with open('E:\\8月1日工作\\test.csv', mode='w',encoding="UTF-8") as f:
    d= csv.writer(f,delimiter=',' )#分隔符','
    d.writerow(['姓名', '年龄', '性别'])
    d.writerow(['张三', ' 19 ', ' 男'])
    d.writerow(['李四', ' 20 ', ' 男'])
    d.writerow(['王二', ' 21 ', ' 女'])
    d.writerow(['麻子', ' 22 ', ' 男'])
    d.writerow(['小五', ' 23 ', ' 女'])

    