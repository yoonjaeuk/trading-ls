import win32com.client
import pythoncom
import sys

#XASessionReceiver는 이벤트 핸들러 느낌
class XASessionReceiver: #XASession에서 서버에 요청한 데이터의 결과값을 수신함(로그인 요청을 보내면 API는 비동기 방식으로 동작하기 때문에)
    def __init__(self):
        self.parent = None 
    
    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            self.parent.response = True #XASessionReceiver에서 XASession을 직접적으로 참조할 방법이 없음 self.parent로 접근
        
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
        self.session.parent = self #XA_Session.XASession 객체에 parent 속성을 추가하고 현재 XASession 인스턴스를 저장(XASessionReceiver에서 접근 가능)

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
        
        while not self.response:  #로그인이 완료되면 로그아웃을 할 때까지 XingAPI가 내부적으로 세션 유지
            pythoncom.PumpWaitingMessages()
        
        # print("대기 종료")
    
    def get_account_list(self):
        cnt = self.session.GetAccountListCount()
        account_list = list()
        for idx in range(cnt):
            account_num = self.session.GetAccountList(idx)
            account_list.append(account_num)
        return account_list

   