from src.core.xa_session import XASession

class Main:
    def __init__(self):
        #Settings
        login_server = "실투자"
        
        #Login
        xa_session = XASession(login_server=login_server)
        xa_session.connect_server()


if __name__ == "__main__":
    Main()