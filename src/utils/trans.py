doc_string ="""
	지연구분,delaygb,delaygb,char,1;
		KEY종목코드,keysymbol,keysymbol,char,18;
		거래소코드,exchcd,exchcd,char,2;
		거래소ID,exchange,exchange,char,4;
		거래상태,suspend,suspend,char,1;
		매매구분,sellonly,sellonly,int,1;
		종목코드,symbol,symbol,char,16;
		한글종목명,korname,korname,char,64;
		업종한글명,induname,induname,char,40;
		소숫점자릿수,floatpoint,floatpoint,char,1;
		외환코드,currency,currency,char,4;
		현재가,price,price,double,15.6;
		전일대비구분,sign,sign,char,1;
		전일대비,diff,diff,double,15.6;
		등락률,rate,rate,float,6.2;
		거래량,volume,volume,long,16;
		거래대금,amount,amount,long,15;
		52주최고가,high52p,high52p,double,15.6;
		52주최저가,low52p,low52p,double,15.6;
		상한가,uplimit,uplimit,double,15.6;
		하한가,dnlimit,dnlimit,double,15.6;
		시가,open,open,double,15.6;
		고가,high,high,double,15.6;
		저가,low,low,double,15.6;
		PER,perv,perv,double,9.2;
		EPS,epsv,epsv,double,9.2;
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
