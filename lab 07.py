import hashlib

def mine_email(sender, recipient, subject, message, difficulty):
    nonce = 0
    attempts = 0
    target = "f" * difficulty
    
    while True:
        attempts += 1
        input_str = f"{sender}{recipient}{subject}{message}{nonce}"
        hash_value = hashlib.sha256(input_str.encode()).hexdigest()
        
        if hash_value.startswith(target):
            return hash_value, attempts
        
        nonce += 1


sender = str(input("enter the sender email address : "))
recipient = str(input("enter the recipient email address :"))
subject =  str(input("enter the subjects : "))
message =  str(input("enter the meaasge : "))
nonce =  int(input("enter the nonce number :"))
difficulty =  int(input("enter the defficulty level : "))

hash_value, attempts = mine_email(sender, recipient, subject, message, difficulty)
print(f"Task : Difficulty {difficulty}")
print(f"Hash: {hash_value}")
print(f"Attempts: {attempts}")

