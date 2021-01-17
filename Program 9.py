import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in range(1, 10):
                ip=f'192.168.0.{n}'
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, "inactive")
                else:
                        print (ip, "active")
