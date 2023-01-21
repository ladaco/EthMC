import random
from rich import print
from rich.panel import Panel
from rich.console import Console
from hdwallet import HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import is_mnemonic
from lxml import html
from mnemonic import Mnemonic
from multiprocessing import Process

filename = 'EthRich.txt'
with open(filename) as f :
    add = f.read().split()
add = set(add)
console = Console()


def mmdrza() :
    z = 0
    w = 0
    while True :
       # z += 1

        langrnd = ['english' , 'english']
        sellan = random.choice(langrnd)
        mne = Mnemonic(str(sellan))
        listno = ["128" , "128"]
        rnd = random.choice(listno)
        words = mne.generate(strength = int(rnd))
        STRENGTH = int(rnd)
        LANGUAGE: str = (sellan)
        MNEMONIC = words
        PASSPHRASE: str = None
        assert is_mnemonic(mnemonic = words , language = sellan)

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 0)
        bip44_hdwallet.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
        mixword = words[:32]
        addr = bip44_hdwallet.p2pkh_address()
        #addr = str.lower(addr)
        addr ='0x07Ee55aA48Bb72DcC6E9D78256648910De513eca'
        #addr ='0x07Ee55aA48Bb72DcC6E9D78256648910De513eca'
        #addr ='0x07ee55aa48bb72dcc6e9d78256648910de513eca'
        priv = bip44_hdwallet.private_key()
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: '+'[orange_red1]'+str(z)+'[/][gold1 on grey15] '+' Win:'+'[white]'+str(w)+'[/]'+'\n[gold1 on grey15]Addr: '+'[white] '+str(addr)+'[/]\nPRIVATEKEY: [grey54]'+str(priv)+'[/]\nMNEMONIC: [grey54]'+str(words)+'[/]')
        style = "bold on grey11"
        console.print(Panel(str(MmdrzaPanel) , title = "[white]Ethereum Mnemonic Checker Offline V3[/]" , subtitle = "[green_yellow blink] Mmdrza.Com [/]" , style = "gold1") , style = style , justify = "full")

        if addr !='' :
            f0 = open('Rezult_ETH_Wallets.txt' , 'a')
            f0.write('\nAddr: '+str(addr))
            f0.write('\nPriv: '+str(priv))
            f0.write('\nMnemonic: '+str(words))
            f0.write('\n     ---     \n')
            f0.close()

        z += 1
        if addr in add :
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt' , 'a')
            f1.write('\nAddress     === '+str(addr))
            f1.write('\nPrivateKey  === '+str(priv))
            f1.write('\nMnemonic    === '+str(words))
            f1.write('\n            ---          \n')
            f1.close()


        bip44_hdwallet1: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 1)
        bip44_hdwallet1.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
        mixword = words[:32]
        addr1 = bip44_hdwallet1.p2pkh_address()
        addr1 = str.lower(addr1)
        priv1 = bip44_hdwallet1.private_key()
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: '+'[orange_red1]'+str(z)+'[/][gold1 on grey15] '+' Win:'+'[white]'+str(w)+'[/]'+'\n[gold1 on grey15]Addr: '+'[white] '+str(addr1)+'[/]\nPRIVATEKEY: [grey54]'+str(priv1)+'[/]\nMNEMONIC: [grey54]'+str(words)+'[/]')
        style = "bold on grey11"
        console.print(Panel(str(MmdrzaPanel) , title = "[white]Ethereum Mnemonic Checker Offline V3[/]" , subtitle = "[green_yellow blink] Mmdrza.Com [/]" , style = "gold1") , style = style , justify = "full")

        z += 1
        if addr1 in add :
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt' , 'a')
            f1.write('\nAddress     === '+str(addr1))
            f1.write('\nPrivateKey  === '+str(priv1))
            f1.write('\nMnemonic    === '+str(words))
            f1.write('\n            ---          \n')
            f1.close()


        bip44_hdwallet2: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 2)
        bip44_hdwallet2.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
        mixword = words[:32]
        addr2 = bip44_hdwallet2.p2pkh_address()
        addr2 = str.lower(addr2)
        priv2 = bip44_hdwallet2.private_key()
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: '+'[orange_red1]'+str(z)+'[/][gold1 on grey15] '+' Win:'+'[white]'+str(w)+'[/]'+'\n[gold1 on grey15]Addr: '+'[white] '+str(addr2)+'[/]\nPRIVATEKEY: [grey54]'+str(priv2)+'[/]\nMNEMONIC: [grey54]'+str(words)+'[/]')
        style = "bold on grey11"
        console.print(Panel(str(MmdrzaPanel) , title = "[white]Ethereum Mnemonic Checker Offline V3[/]" , subtitle = "[green_yellow blink] Mmdrza.Com [/]" , style = "gold1") , style = style , justify = "full")

        z += 1
        if addr2 in add :
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt' , 'a')
            f1.write('\nAddress     === '+str(addr2))
            f1.write('\nPrivateKey  === '+str(priv2))
            f1.write('\nMnemonic    === '+str(words))
            f1.write('\n            ---          \n')
            f1.close()

    # ============================


mmdrza()

if __name__ == '__main__' :
    for i in range(len(add)) :
        p = multiprocessing.Process(target = mmdrza)
        p.start()
        p.join()
