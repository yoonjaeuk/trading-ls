doc_string ="""
	관리지점번호, MgmtBrnNo, MgmtBrnNo, char, 3;
		계좌번호, AcntNo, AcntNo, char, 20;
		계좌명, AcntNm, AcntNm, char, 40;
		체결시각, ExecTime, ExecTime, char, 9;
		주문시각, OrdTime, OrdTime, char, 9;
		주문번호, OrdNo, OrdNo, long, 10;
		원주문번호, OrgOrdNo, OrgOrdNo, long, 10;
		단축종목번호, ShtnIsuNo, ShtnIsuNo, char, 9;
		주문처리유형명, OrdTrxPtnNm, OrdTrxPtnNm, char, 50;
		주문처리유형코드, OrdTrxPtnCode, OrdTrxPtnCode, long, 9;
		정정취소가능수량, MrcAbleQty, MrcAbleQty, long, 16;
		주문수량, OrdQty, OrdQty, long, 16;
		해외주문가, OvrsOrdPrc, OvrsOrdPrc, double, 22.7;
		체결수량, ExecQty, ExecQty, long, 16;
		해외체결가, OvrsExecPrc, OvrsExecPrc, double, 28.7;
		호가유형코드, OrdprcPtnCode, OrdprcPtnCode, char, 2;
		호가유형명, OrdprcPtnNm, OrdprcPtnNm, char, 40;
		주문유형명, OrdPtnNm, OrdPtnNm, char, 40;
		주문유형코드, OrdPtnCode, OrdPtnCode, char, 2;
		정정취소구분코드, MrcTpCode, MrcTpCode, char, 1;
		정정취소구분명, MrcTpNm, MrcTpNm, char, 10;
		전체체결수량, AllExecQty, AllExecQty, long, 16;
		통신매체코드, CommdaCode, CommdaCode, char, 2;
		주문시장코드, OrdMktCode, OrdMktCode, char, 2;
		시장명, MktNm, MktNm, char, 40;
		통신매체명, CommdaNm, CommdaNm, char, 40;
		일본시장한글종목명, JpnMktHanglIsuNm, JpnMktHanglIsuNm, char, 100;
		미체결수량, UnercQty, UnercQty, long, 16;
		확인수량, CnfQty, CnfQty, long, 16;
		통화코드, CrcyCode, CrcyCode, char, 3;
		등록시장코드, RegMktCode, RegMktCode, char, 2;
		종목번호, IsuNo, IsuNo, char, 12;
		중개인구분코드, BrkTpCode, BrkTpCode, char, 2;
		상대중개인명, OppBrkNm, OppBrkNm, char, 40;
		매매구분코드, BnsTpCode, BnsTpCode, char, 1;
		대출일자, LoanDt, LoanDt, char, 8;
		대출금액, LoanAmt, LoanAmt, long, 16;
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
