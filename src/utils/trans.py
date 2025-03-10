doc_string ="""
레코드갯수, RecCnt, RecCnt, long, 5
		주문번호, OrdNo, OrdNo, long, 10;
		계좌명, AcntNm, AcntNm, char, 40;
		종목명, IsuNm, IsuNm, char, 40;
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
