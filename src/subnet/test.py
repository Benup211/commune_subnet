from communex.module.client import ModuleClient
from substrateinterface import Keypair
import asyncio

key:Keypair=Keypair.create_from_mnemonic("sample license wide sound rabbit pudding robot merit text stamp throw film")
print(key)
miner_key="5Fq8N2rNxFAoq5jPxNFhBkEWnzYXc32xPeWKPt1upEXTDYAK"
client = ModuleClient("localhost", 8000,key)

miner_answer = asyncio.run(client.call("generate", miner_key, {"prompt": "45", "model": "hi"}, timeout=1000))
miner_answer = miner_answer["answer"]
print(miner_answer)
