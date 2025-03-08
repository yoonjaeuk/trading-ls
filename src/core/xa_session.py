import win32com.client
import pythoncom
import sys


class XASessionReceiver: #XASession에서 서버에 요청한 데이터의 결과값을 수신함
    def __init__(self):
        self.parent = None
    
    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            self.parent.response = True
        
        else:
            print(f"로그인 실패 : {code} | {msg}")
            sys.exit()
    
    def OnDisconnect(self):
        print("서버와의 연결이 끊겼습니다")
        sys.exit()
        

class XASession:
    def __init__(self, login_server):
        self.response = False
        self.login_server = self.set_server(login_server=login_server)
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionReceiver)
        self.session.parent = self

    @staticmethod
    def set_server(login_server):
        if login_server == "실투자":
            return "api.ls-sec.co.kr"
        else:
            return "demo.ls-sec.co.kr"
    
    def connect_server(self):
         res = self.session.ConnectServer(self.login_server, 20001)
         if not res:
             error_code = self.GetLastError()
             error_msg = self.GetErrorMessage(error_code)
             print(error_msg)
             sys.exit()

    def disconnect_server(self):
        self.session.DisconnectServer()
        sys.exit()

    def login(self, crypto_wallet):
        _id = crypto_wallet["id"]
        _pw = crypto_wallet["pwd"]
        _cert = crypto_wallet["cert_pwd"]
      
        self.session.Login(_id, _pw, _cert, 0, False)
        
        while not self.response:
            pythoncom.PumpWaitingMessages()
        
        # print("대기 종료")
    
    def get_account_list(self):
        cnt = self.session.GetAccountListCount()
        account_list = list()
        for idx in range(cnt):
            account_num = self.session.GetAccountList(idx)
            account_list.append(account_num)
        return account_list

# if __name__ == "__main__":
   