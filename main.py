from src.config.crypto_wallet import CRYPTO_WALLET
from src.core.xa_session import XASession

class Main:
    def __init__(self):
        #Settings
        login_server = "실투자"
        crypto_wallet = CRYPTO_WALLET[login_server]
        #Login
        xa_session = XASession(login_server=login_server)
        xa_session.connect_server()
        xa_session.login(crypto_wallet=crypto_wallet)
        #account_number 
        account_num = xa_session.get_account_list()
        print(account_num)


if __name__ == "__main__":
    Main()