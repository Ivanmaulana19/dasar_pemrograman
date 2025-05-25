import uuid 
from datetime import datetime
import random

def generate_order_id():
    tanggal = datetime.now().strftime("%y%m%d")
    random_number = random.randint(100000, 99999999)
    return f"Order-{tanggal}-{random_number}"