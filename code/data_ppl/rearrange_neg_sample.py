import pandas as pd

def read_csv_to_list(filename):
    # 读取csv文件
    df = pd.read_csv(filename)

    # 将DataFrame转换为列表
    data_list = df.values.tolist()
    new_data_list = []
    for i in range(9999):
        new_data_list.append(data_list[i])
        for j in range(100):
            new_data_list.append(data_list[j + 9999])
    # 将数据转换为字符串
    data_str = '\n'.join([','.join(map(str, sublist)) for sublist in new_data_list])

    # 打开文件并写入数据
    with open('target_train_rearange.csv', 'w') as f:
        f.write(data_str)

# 调用函数
data_list = read_csv_to_list('../../data/ml-1m/feateng_data/target_train.csv')

# 打印结果
print(data_list)