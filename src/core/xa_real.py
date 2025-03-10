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



class XAReal:
    def __init__(self, account_dict, out_standing, deposit):
        self.response = False
        self.queue = queue.Queue()
        self.real_dict = self.real_objects()  # 실시간 부분에서는 한가지 객체만으로 호가데이터, 체결데이터, 주문데이터 등 모든 것을 다 받을 수 없음(각 요청마다 객체를 생성해야됨 -> 각 객체를 하나의 dictionary안으로)

        self.account_dict = account_dict
        self.out_standing = out_standing
        self.deposit = deposit

    def real_objects(self):
        item = dict()
        headers = ["실시간체결", "실시간호가", "주문접수", "주문체결", "주문정정", "주문취소", "주문거부"]
        for header in headers:
            real = win32com.client.DispatchWithEvents("XA_DataSet.XAReal", XARealReceiver) # 각 객체별 저장을 위해
            real.parent = self
            item[header] = real
        return item
    
    def loop(self):
        while True:
            if not self.queue.empty():
                print(self.queue.get())

            pythoncom.PumpWaitingMessages()


    def GSC(self, exchange_code, symbol):
        real = self.real_dict["실시간체결"]
        real.ResFileName = "C:/LS_SEC/xingAPI/Res/GSC.res"
        real.SetFieldData("InBlock", "keysymbol", exchange_code + symbol)
        real.AdviseRealData()
        
