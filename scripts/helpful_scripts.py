from brownie import network, accounts, config
import dotenv

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "mainnet-fork"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None
