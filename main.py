from src.config.crypto_wallet import CRYPTO_WALLET
from src.core.xa_session import XASession
from src.core.xa_query import XAQuery

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

        xa_query = XAQuery()
        account_dict = xa_query.request_balance(account_num=account_num[1], password=crypto_wallet["acc_pwd"])
        deposit = xa_query.request_deposit(account_num=account_num[1], password=crypto_wallet["acc_pwd"])
        out_standing = xa_query.request_out_standing(account_num=account_num[1], password=crypto_wallet["acc_pwd"])

        print(out_standing)

        # print(deposit)
        
        xa_query.g3101(exchange_code="82", symbol="TSLA")




if __name__ == "__main__":
    Main()