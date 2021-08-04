import pandas as pd
import re



data = pd.read_excel('d:/Jupyter/天工矿业公司2020年预算目标完成情况统计报表.xlsx',
                     sheet_name=1, header=1, usecols='A,C:AS', nrows=114)
data.columns = map(lambda x: x.replace('\n', ''), data.columns)
# rint(data.columns)

mask = data['2020年预算'] != 0 # 条件表达式 也俗称掩码
data[mask]

data_one = data.loc[:, list(filter(lambda x:x.endswith('实际'), data.columns))]
data_one.loc[1:16, '2019年5月实际':'2020年10月实际']  # loc切片用法之一


data_2019 = data.loc[:, [
    x for x in data.columns if re.search('2019年.*月实际', x)]]  # 2019年实际
data_2019.loc[[1, 113], '2019年3月实际':'2019年6月实际']  # loc切片用法之二

data_2020 = data.loc[:, list(
    filter(lambda x:re.match('2020年.*实际', x), data.columns))]  # 2020年实际

# loc是基于labers标签索引来切片的，注意与iloc切片的区别！！！
data.loc