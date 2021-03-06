import os

from .wallets import OpenNodeWallet  # OR LndWallet OR OpennodeWallet

WALLET = OpenNodeWallet(endpoint=os.getenv("OPENNODE_API_ENDPOINT"),admin_key=os.getenv("OPENNODE_ADMIN_KEY"),invoice_key=os.getenv("OPENNODE_INVOICE_KEY"))
#WALLET = LntxbotWallet(endpoint=os.getenv("LNTXBOT_API_ENDPOINT"),admin_key=os.getenv("LNTXBOT_ADMIN_KEY"),invoice_key=os.getenv("LNTXBOT_INVOICE_KEY"))
#WALLET = LndWallet(endpoint=os.getenv("LND_API_ENDPOINT"),admin_macaroon=os.getenv("LND_ADMIN_MACAROON"),invoice_macaroon=os.getenv("LND_INVOICE_MACAROON"),read_macaroon=os.getenv("LND_READ_MACAROON"))
#WALLET = LNPayWallet(endpoint=os.getenv("LNPAY_API_ENDPOINT"),admin_key=os.getenv("LNPAY_ADMIN_KEY"),invoice_key=os.getenv("LNPAY_INVOICE_KEY"),api_key=os.getenv("LNPAY_API_KEY"),read_key=os.getenv("LNPAY_READ_KEY"))


LNBITS_PATH = os.path.dirname(os.path.realpath(__file__))
LNBITS_DATA_FOLDER = os.getenv("LNBITS_DATA_FOLDER", os.path.join(LNBITS_PATH, "data"))

DEFAULT_USER_WALLET_NAME = os.getenv("DEFAULT_USER_WALLET_NAME", "Bitcoin LN Wallet")
FEE_RESERVE = float(os.getenv("FEE_RESERVE", 0))
