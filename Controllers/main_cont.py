from API.trading_broker import *
from Bot.fetcher_bot import *
from Bot.transaction_bot import *
from Model.transaction import *


class MainController(object):

    def __init__(self, app, model):
        self.model = model
        self.exchange = Exchange(model)
        self.fetcher_bot = None
        self.transaction_bot = None
        self.app = app

    def change_login_api_key(self, value):
        self.model.login_api_key = value
        self.model.update_func("login_api_key")
        print("Updated login_api_key " + str(value))

    def change_login_api_sign(self, value):
        self.model.login_api_sign = value
        self.model.update_func("login_api_sign")
        print("Updated login_login_api_sign " + str(value))

    def change_strategy_target(self, value):
        self.model.strategy_target = value
        self.model.update_func("strategy_target")
        print("Updated strategy_target " + str(value))

    def change_strategy_stop_limit(self, value):
        self.model.strategy_stop_limit = value
        self.model.update_func("strategy_stop_limit")
        print("Updated strategy_stop_limit " + str(value))

    def change_transaction_amount(self, value):
        self.model.transaction_amount = value
        self.model.update_func("transaction_amount")
        print("transaction_amount " + str(value))

    def change_transaction_buy_in(self, value):
        self.model.transaction_buy_in = value
        self.model.update_func("transaction_buy_in")
        print("Updated transaction buy in " + str(value))

    def change_transaction_target(self, value):
        self.model.transaction_target = value
        self.model.update_func("transaction_target")
        print("Updated transaction target " + str(value))

    def change_transaction_stop_limit(self, value):
        self.model.transaction_stop_limit = value
        self.model.update_func("transaction_stop_limit")
        print("Updated transaction_stop_limit " + str(value))

    def change_base_currency(self, value):
        self.model.base_currency = value
        print("Updated base currency: " + str(value))

    def change_target_currency(self, value):
        self.model.target_currency = value
        print("Updated target currency: " + str(value))

    def change_account_balance(self, value):
        self.model.account_balance = value
        self.model.update_func("account_balance")
        print("account_balance " + str(value))

    def login(self):
        key = self.model.login_api_key
        sign = self.model.login_api_sign

        self.exchange.connect(key, sign)

        if self.exchange.connection_active:
            self.model.login_msg = "Login Success"
            self.login_procedure()
        else:
            self.model.login_msg = "Login Fail"

    def login_procedure(self):
        self.model.logged_in = True
        self.load_currencies()
        self.init_bots()

    def load_currencies(self):
        self.model.base_currency = "BTC"
        self.model.target_currency = "ETH"
        self.exchange.load_data_to_model()
        self.model.target_currency_data = self.exchange.get_all_asset_names()
        self.model.update_func("base_currency_options")
        self.model.update_func("target_currency_options")

    def init_bots(self):
        self.fetcher_bot = FetcherBot(self.model, self.exchange)
        self.transaction_bot = TransactionBot(self.model, self.exchange)
        self.fetcher_bot.start()
        self.transaction_bot.start()

        self.app.aboutToQuit.connect(self.stop_bots)

    def stop_bots(self):
        self.fetcher_bot.stop()
        self.transaction_bot.stop()

    def apply_strategy(self):
        print("Strategy applied")

    def execute_order(self): #change name to transaction
        #add check if all fields are entered

        item = TransactionItem(self.model.transaction_amount, self.model.transaction_buy_in, self.model.transaction_target, self.model.transaction_stop_limit, self.model.base_currency, self.model.target_currency)
        self.model.transactions.append(item)
        print("Item added")
