from src.config.crypto_wallet import CRYPTO_WALLET
from src.core.xa_session import XASession
from src.core.xa_query import XAQuery
from src.core.xa_real import XAReal
import pythoncom
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
        deposit = xa_query.request_deposit(account_num=account_num[0], password=crypto_wallet["acc_pwd"])
        out_standing = xa_query.request_out_standing(account_num=account_num[0], password=crypto_wallet["acc_pwd"])

        print(out_standing)

        # print(deposit)
        
        xa_real = XAReal(account_dict = account_dict, out_standing = out_standing, deposit = deposit)
        symbol_list = ["TSLA", "AAPL", "AMZN"]
        # for symbol in symbol_list:
            # xa_real.GSC(exchange_code = "82", symbol = symbol)
            # xa_real.GSH(exchange_code = "82", symbol = symbol)
        xa_real.ASN()

        test_num = 0
        origin_num = None
        
        while True:
           if not xa_query.queue.empty():
                data = xa_query.queue.get()

                if "주문번호" in data[1].keys() and origin_num is None:
                    origin_num = data[1]["주문번호"]

            
           if test_num == 1 and origin_num is not None:
              test_num += 1
              xa_query.send_order(account_num=account_num[0], password=crypto_wallet["acc_pwd"], order_type="취소", origin_num=origin_num, symbol="TRVI")

           if test_num == 0:
                test_num += 1
                xa_query.send_order(account_num=account_num[0], password=crypto_wallet["acc_pwd"], symbol="TRVI", qty ="1", order_price="5.80")
#self, account_num, password, order_type = "매수", origin_num = "", exchange_code ="82", symbol = "TSLA", qty ="0", order_price="", hoga_type = "00"
           pythoncom.PumpWaitingMessages()


       



if __name__ == "__main__":
    Main()