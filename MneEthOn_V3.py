import random
from rich import print
from rich.panel import Panel
from rich.console import Console
from hdwallet import HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import is_mnemonic
from mnemonic import Mnemonic
from multiprocessing import Process
from requests_html import HTMLSession
import base64

console = Console()

def balance(addr):
    url_n = f"https://eth1.trezor.io/address/{addr}"
    se = HTMLSession()
    nmp = se.get(url_n)
    Master = nmp.html.xpath('/html/body/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')
    return Master[0].text


def transaction(addr):
    url_n = f"https://eth1.trezor.io/address/{addr}"
    se = HTMLSession()
    nmp = se.get(url_n)
    Master = nmp.html.xpath('/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]')
    return Master[0].text


def mmdrza():
    z = 1
    w = 0
    while True:
        z += 1

        langrnd = ['english']
        sellan = random.choice(langrnd)
        mne = Mnemonic(str(sellan))
        listno = ["128", "128"]
        rnd = random.choice(listno)
        words = mne.generate(strength=int(rnd))
        STRENGTH = int(rnd)
        LANGUAGE: str = (sellan)
        MNEMONIC = words
        PASSPHRASE: str = None
        assert is_mnemonic(mnemonic=words, language=sellan)

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=Cryptocurrency, account=0, change=False,
                                                      address=0)
        bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)
        mixword = words[:32]
        addr = bip44_hdwallet.p2pkh_address()
        # addr ='0xfc43f5f9dd45258b3aff31bdbe6561d97e8b71de'
        priv = bip44_hdwallet.private_key()
        # =======================================

        # =======================================
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: ' + '[orange_red1]' + str(
                z) + '[/][gold1 on grey15] ' + ' Win:' + '[white]' + str(
                w) + '[/]' + '[grey74]  ReqSpeed: ' + '[/][gold1]             Balance: ' + '[/][aquamarine1]' + str(
                balance(addr)) + '[/][gold1]             Transaction : ' + '[/][aquamarine1]' + str(
                transaction(addr)) + '\n[/][gold1 on grey15]Addr: ' + '[white] ' + str(
                addr) + '[/]\nPRIVATEKEY: [grey54]' + str(priv) + '[/]\nMNEMONIC: [grey54]'+str(words)+'[/]')
        style = "gold1 on grey11"
        console.print(Panel(str(MmdrzaPanel), title="[white]Ethereum Mnemonic Checker V3[/]",
                            subtitle="[green_yellow blink] Mmdrza.Com [/]", style="green"), style=style, justify="full")

        z += 1
        iffer = '0 ETH'
        if balance(addr) != iffer:
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt', 'a')
            f1.write(f'\nAddress     === {addr}')
            f1.write(f'\nPrivateKey  === {priv}')
            f1.write(f'\nMnemonic    === {words}')
            f1.write(f'\nBalance === {balance(addr)}')
            f1.write(f'\nTransaction === {transaction(addr)}')
            f1.write(f'\n            -------[ M M D R Z A . C o M ]------                   \n')
            f1.close()

    # ============================


mmdrza()

if __name__ == '__main__':
    for i in range(len(add)):
        p = multiprocessing.Process(target=mmdrza)
        p.start()
        p.join()
