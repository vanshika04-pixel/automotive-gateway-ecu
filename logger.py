def log(msg):
    with open("diag.log", "a") as f:
        f.write(msg + "\n")
