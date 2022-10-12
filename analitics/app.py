import time

def run(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())

while True:
    run("update_sql.py")
    time.sleep(5)