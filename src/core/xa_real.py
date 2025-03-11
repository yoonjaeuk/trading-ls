from src.config.menulist import *
import win32com.client
import pythoncom
import queue

class XARealReceiver:
    def __init__(self):
        self.parent = None
    
    def OnReceiveRealData(self, event):
        if event == "GSC":
            item = list()
            for idx in range(len(GSC_OUT_BLOCK_CODE)):
                out_block_code = GSC_OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["실시간체결"].GetFieldData("OutBlock", out_block_code)
                item.append(data)
            
            self.parent.queue.put(["실시간체결", dict(zip(GSC_OUT_BLOCK_NAME, item))])
        
        elif event == "GSH":
            item = list()
            for idx in range(len(GSH_OUT_BLOCK_CODE)):
                out_block_code = GSH_OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["실시간호가"].GetFieldData("OutBlock", out_block_code)
                item.append(data)
            
            self.parent.queue.put(["실시간호가", dict(zip(GSH_OUT_BLOCK_NAME, item))])
        
        elif event == "AS0":
            item = list()
            for idx in range(len(AS0_OUT_BLOCK_CODE)):
                out_block_code = AS0_OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["주문접수"].GetFieldData("OutBlock", out_block_code)
                item.append(data)
            
            self.parent.queue.put(["주문접수", dict(zip(AS0_OUT_BLOCK_NAME, item))])

        
        elif event in ["AS1", "AS2", "AS3", "AS4"]:
            if event == "AS1":
                event_type = "주문체결"
            elif event == "AS2":
                event_type = "주문정정"
            elif event == "AS3":
                event_type = "주문취소"
            elif event == "AS4":
                event_type = "주문거부"
            
            item = list()
            for idx in range(len(ASN_OUT_BLOCK_CODE)):
                out_block_code = ASN_OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict[event_type].GetFieldData("OutBlock", out_block_code)
                item.append(data)
            
            self.parent.queue.put([event_type, dict(zip(ASN_OUT_BLOCK_NAME, item))])

            


class XAReal:
    def __init__(self):
        self.response = False
        self.queue = queue.Queue()
        self.real_dict = self.real_objects()  # 실시간 부분에서는 한가지 객체만으로 호가데이터, 체결데이터, 주문데이터 등 모든 것을 다 받을 수 없음(각 요청마다 객체를 생성해야됨 -> 각 객체를 하나의 dictionary안으로)


    def real_objects(self):
        item = dict()
        headers = ["실시간체결", "실시간호가", "주문접수", "주문체결", "주문정정", "주문취소", "주문거부"]
        for header in headers:
            real = win32com.client.DispatchWithEvents("XA_DataSet.XAReal", XARealReceiver) # 각 객체별 저장을 위해
            real.parent = self
            item[header] = real
        return item

    def GSC(self, exchange_code, symbol):
        real = self.real_dict["실시간체결"]
        real.ResFileName = "C:/LS_SEC/xingAPI/Res/GSC.res"
        real.SetFieldData("InBlock", "keysymbol", exchange_code + symbol)
        real.AdviseRealData()
        
    def GSH(self, exchange_code, symbol):
        real = self.real_dict["실시간호가"]
        real.ResFileName = "C:/LS_SEC/xingAPI/Res/GSH.res"
        real.SetFieldData("InBlock", "keysymbol", exchange_code + symbol)
        real.AdviseRealData()    
    
    def ASN(self):
        #해외주식부문 부분일괄등록
        #ASO - 해외주식주문접수
        #AS1 - 해외주식주문체결
        #AS2 - 해외주식주문정정
        #AS3 - 해외주식주문취소
        #AS4 - 해외주식주문거부

        headers = ["주문접수", "주문체결", "주문정정", "주문취소", "주문거부"]
        for idx in range(len(headers)):
            real = self.real_dict[headers[idx]]
            real.ResFileName = f"C:/LS_SEC/xingAPI/Res/AS{idx}.res"
            real.AdviseRealData()