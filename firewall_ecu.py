BLOCKED_IDS = ["666", "999"]

with open("malicious_can.txt") as f:
    for line in f:
        can_id = line.split(",")[0]

        if can_id in BLOCKED_IDS:
            print(f"🚨 BLOCKED malicious CAN ID: {can_id}")
        else:
            print(f"✔ Allowed CAN ID: {can_id}")
