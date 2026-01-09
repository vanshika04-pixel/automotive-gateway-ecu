from sec_module import secure
from ethernet_tx import send
from logger import log

with open("can_input.txt") as f:
    for line in f:
        can_id, b1,b2,b3,b4,b5 = line.strip().split(",")
        payload = f"{can_id}:{b1}{b2}{b3}{b4}{b5}"

        checksum = secure(payload)
        frame = f"{payload}|{checksum}"

        send(frame)
        log(frame)
