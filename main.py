from src.config.crypto_wallet import CRYPTO_WALLET
from src.core.xa_session import XASession
from src.core.xa_query import XAQuery
from src.core.xa_real import XAReal
import pythoncom
import time
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
        account_dict = xa_query.request_balance(account_num=account_num[0], password=crypto_wallet["acc_pwd"])
        # print(account_dict)
        deposit = xa_query.request_deposit(account_num=account_num[0], password=crypto_wallet["acc_pwd"])
        # print(deposit)
        out_standing = xa_query.request_out_standing(account_num=account_num[0], password=crypto_wallet["acc_pwd"])

        # print(out_standing, {2})

        # print(deposit)
        
        xa_real = XAReal()
        symbol_list = ["TSLA", "AAPL", "AMZN"]
        # for symbol in symbol_list:
            # xa_real.GSC(exchange_code = "82", symbol = symbol)
            # xa_real.GSH(exchange_code = "82", symbol = symbol)
        xa_real.ASN()

        test_num = 0
        origin_num = None
        
        # time.sleep(1)
        # account_dict = xa_query.request_balance(account_num=account_num[0], password=crypto_wallet["acc_pwd"])
        # print(account_dict)

        while True:  #원하는 매매 방식 여기서 지정
    
           
           if not xa_real.queue.empty():
                data = xa_real.queue.get()
                if data[0][:2] == "주문":
                    print(data)
                
                if data[0] == "주문체결":
                    time.sleep(0.1)
                    account_dict = xa_query.request_balance(account_num=account_num[0], password=crypto_wallet["acc_pwd"])
                    print(account_dict)

           if not xa_query.queue.empty():
                data = xa_query.queue.get()


           if test_num == 0:
                test_num += 1
                # xa_query.send_order(account_num=account_num[0], password=crypto_wallet["acc_pwd"], symbol="TRVI", qty ="1", order_price="5.00")
           pythoncom.PumpWaitingMessages()


       



if __name__ == "__main__":
    Main()