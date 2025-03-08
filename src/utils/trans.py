doc_string ="""
레코드갯수, RecCnt, RecCnt, long, 5
		계좌번호, AcntNo, AcntNo, char, 20;
		비밀번호, Pwd, Pwd, char, 8;
		기준일자, BaseDt, BaseDt, char, 8;
		통화코드, CrcyCode, CrcyCode, char, 3;
		해외증권잔고구분코드, AstkBalTpCode, AstkBalTpCode, char, 2;
"""


item = list()
item2 = list()

data = doc_string.split('\n')[1:-1]
for idx in range(len(data)):
    res = data[idx].split(',')
    item.append(res[1].replace('\t', '').replace(' ', '').replace(';', ''))
    item2.append(res[0].replace('\t', '').replace(' ', '').replace(';', ''))


print(item)
print(item2)
