from src.config.menulist import *
import win32com.client
import pythoncom
import sys


#기본적으로 XingAPi는 비동기 이벤트 기반으로 동작하기 때문에 서버에 데이터 요청과 응답을 분리한 로직이 유리함(이벤트 기반 프로그래밍)
#책임 분리 원칙(각 클래스가 자신의 역할에만 집중하게)

class XAQueryReceiver: #XASession에서 서버에 요청한 데이터의 결과값을 수신함
    def __init__(self):
        self.parent = None
    
    def OnReceiveMessage(self, _, code, msg): #데이터를 요청했을 때 결과 메시지를 수신하는 함수
        print(f"OnReceiveMessage : {code} | {msg}")
        self.parent.response = True

    def OnReceiveData(self, event): #요청한 데이터를 수신받는 함수
        if event == "COSOQ00201":
            account_dict = dict()
            
            item = list()
            for idx in range(len(BALANCE_OUT_BLOCK_2_CODE)):
                out_block_code = BALANCE_OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData("COSOQ00201OutBlock2", out_block_code, 0)
                item.append(data)
            # print(dict(zip(BALANCE_OUT_BLOCK_2_NAME, item)))
            
            item = list()
            for idx in range(len(BALANCE_OUT_BLOCK_3_CODE)):
                out_block_code = BALANCE_OUT_BLOCK_3_CODE[idx]
                data = self.parent.query.GetFieldData("COSOQ00201OutBlock3", out_block_code, 0)
                item.append(data)
            # print(dict(zip(BALANCE_OUT_BLOCK_3_NAME, item)))
            
            count = self.parent.query.GetBlockCount("COSOQ00201OutBlock4")
            for cnt in range(count):  #occurs 속성인 경우
                item = list()
                for idx in range(len(BALANCE_OUT_BLOCK_4_CODE)):
                   out_block_code = BALANCE_OUT_BLOCK_4_CODE[idx]
                   data = self.parent.query.GetFieldData("COSOQ00201OutBlock4", out_block_code, cnt)
                   item.append(data)
                # print(dict(zip(BALANCE_OUT_BLOCK_4_NAME, item)))
                
                code = item[1]
                account_dict[code] = dict(zip(BALANCE_OUT_BLOCK_4_NAME, item))

            self.parent.accout_dict = account_dict

        
        elif event == "COSOQ02701":
            deposit = self.parent.query.GetFieldData("COSOQ02701OutBlock3", "FcurrOrdAbleAmt", 0)
            self.parent.deposit = deposit
        
        elif event == "COSAQ00102":
            out_standing = dict()
            
            item = list()
            for idx in range(len(OUT_STANDING_OUT_BLOCK_1_CODE)):
                out_block_code = OUT_STANDING_OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData("COSAQ00102OutBlock1", out_block_code, 0)
                item.append(data)
            # print(dict(zip(OUT_STANDING_OUT_BLOCK_1_NAME, item)))
            
            item = list()
            for idx in range(len(OUT_STANDING_OUT_BLOCK_2_CODE)):
                out_block_code = OUT_STANDING_OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData("COSAQ00102OutBlock2", out_block_code, 0)
                item.append(data)
            # print(dict(zip(OUT_STANDING_OUT_BLOCK_2_NAME, item)))
            
            count = self.parent.query.GetBlockCount("COSAQ00102OutBlock3")
            for cnt in range(count):  #occurs 속성인 경우
                item = list()
                for idx in range(len(OUT_STANDING_OUT_BLOCK_3_CODE)):
                   out_block_code = OUT_STANDING_OUT_BLOCK_3_CODE[idx]
                   data = self.parent.query.GetFieldData("COSAQ00102OutBlock3", out_block_code, cnt)
                   item.append(data)
                # print(dict(zip(OUT_STANDING_OUT_BLOCK_3_NAME, item)))
                
                code = item[7]
                out_standing[code] = dict(zip(OUT_STANDING_OUT_BLOCK_3_NAME, item))

            self.parent.out_standing = out_standing
       
        elif event == "g3101":
            item = list()
            for idx in range(len(G3101_OUT_BLOCK_CODE)):
                out_block_code = G3101_OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData("g3101OutBlock", out_block_code, 0)
                item.append(data)
            print(dict(zip(G3101_OUT_BLOCK_NAME, item)))



class XAQuery:  #서버에 데이터 요청
    def __init__(self):
        self.deposit = 0
        self.account_dict = dict()
        self.out_standing = dict()
        self.response = False
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryReceiver)
        self.query.parent = self
    
    def request(self, cont=False):
         res = self.query.Request(cont)
         
         if res < 0:
             print("데이터 요청에 실패했습니다")
            
         self.response = False
    
         while not self.response:
            pythoncom.PumpWaitingMessages()

    def request_balance(self, account_num, password):  #RES파일 객체등록
        self.query.ResFileName = "C:/LS_SEC/xingAPI/Res/COSOQ00201.res"
        datas = ["00001", account_num, password, "", "USD", "00"]

        for idx in range(len(datas)):
            self.query.SetFieldData("COSOQ00201InBlock1", BALANCE_IN_BLOCK_CODE[idx], 0, datas[idx])
        
        self.request()

        return self.account_dict #계좌잔고 수신 후 dictionary 반환
    

    def request_deposit(self, account_num, password):
        self.query.ResFileName = "C:/LS_SEC/xingAPI/Res/COSOQ02701.res"
        datas = ["00001", account_num, password, "USD"]

        for idx in range(len(datas)):
            self.query.SetFieldData("COSOQ02701InBlock1", DEPOSIT_IN_BLOCK_CODE[idx], 0, datas[idx])
        
        self.request()

        return self.deposit #계좌잔고 수신 후 dictionary 반환

    
    def request_out_standing(self, account_num, password):
       self.query.ResFileName = "C:/LS_SEC/xingAPI/Res/COSAQ00102.res"
       datas = ["00001", "1", "2", "82", account_num, password, "0", "", "0", "", "2", "USD", "1", "0"]

       for idx in range(len(datas)):
            self.query.SetFieldData("COSAQ00102InBlock1", OUT_STANDING_IN_BLOCK_CODE[idx], 0, datas[idx])
        
       self.request()

       return self.out_standing
    
    def g3101(self, exchange_code, symbol):  #exchange = 거래소 코드, symbol = 종목코드
       
       self.query.ResFileName = "C:/LS_SEC/xingAPI/Res/g3101.res"
       datas = ["R", exchange_code + symbol, exchange_code, symbol]

       for idx in range(len(datas)):
            self.query.SetFieldData("g3101InBlock", G3101_IN_BLOCK_CODE[idx], 0, datas[idx])
        
       self.request()

       