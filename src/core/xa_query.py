import win32com.client
import pythoncom
import sys


class XAQueryReceiver: #XASession에서 서버에 요청한 데이터의 결과값을 수신함
    def __init__(self):
        self.parent = None
    
    def OnReceiveMessage(self, _, code, msg): #데이터를 요청했을 때 결과 메시지를 수신하는 함수
        print(f"OnReceiveMessage : {code} | {msg}")
        self.parent.response = True

    def OnReceiveDate(self, event): #요청한 데이터를 수신받는 함수
        pass
        

class XAQuery:
    def __init__(self, login_server):
        self.response = False
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryReceiver)
        self.query.parent = self
    
    def request(self):
         while not self.response:
            pythoncom.PumpWaitingMessages()