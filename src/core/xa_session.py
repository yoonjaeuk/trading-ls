import win32com.client
import pythoncom
import sys


class XASessionReceiver:
    def __init__(self):
        self.parent = None


class XASession:
    def __init__(self, login_server):
        self.login_server = self.set_server(login_server=login_server)
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionReceiver)
    
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

    def disconnect_server(self):
        self.session.DisconnectServer()
        
# if __name__ == "__main__":
   