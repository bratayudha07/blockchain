from block import Block 
from blockchain import Blockchain
from pow import proof_of_work
from pos import proof_of_stake

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

print("\n=== PROOF OF WORK ===")
difficulty = 4

# Block baru khusus buat demo mining, biar chain yang lama gak ikut berubah/invalid
new_block = Block(
    index=len(blockchain.chain),
    data={
        "patient_id": "P-004",
        "name": "siti aminah",
        "keluhan": "demam tinggi",
        "tindakan": "rawat inap",
        "obat": "paracetamol infus",
    },
    previous_hash=blockchain.chain[-1].hash,
)

print("Data Block :", new_block.data)
print("Difficulty :", difficulty)

proof_of_work(new_block, difficulty)

print("Nonce :", new_block.nonce)
print("Hash  :", new_block.hash)

print("\n=== PROOF OF STAKE ===")
validators = {
    "Dokter": 40,
    "Perawat": 30,
    "Admin RS": 20,
    "Apoteker": 10,
}

print("\nValidator:")
for v, s in validators.items():
    print(f"- {v}: {s} stake")

selected = proof_of_stake(validators)
print("\nValidator terpilih:", selected)