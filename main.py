from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_block({
    "patient_id": "P-001",
    "name": "haidar",
    "keluhan": "siku robek",
    "tindakan": "jahit dan perban",
    "obat": "preda nyeri",
})

blockchain.add_block({
    "patient_id": "P-002",
    "name": "pinjol",
    "keluhan": "sakit kepala",
    "tindakan": "mcu",
    "obat": "bodrex",
})

blockchain.add_block({
    "patient_id": "P-003",
    "name": "robby pantjoro",
    "keluhan": "diabetes",
    "tindakan": "cek gula darah",
    "obat": "insulin",
})

for block in blockchain.chain:
    print("=" * 50)
    print("INDEX    :", block.index)
    print("TIMESTAMP:", block.timestamp)
    print("DATA     :", block.data)
    print("PREV     :", block.previous_hash)
    print("HASH     :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())
