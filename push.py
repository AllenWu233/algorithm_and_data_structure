#! /usr/bin/python
import os
import time


local_time = time.strftime('%Y/%m/%d-%H:%M', time.localtime(time.time()))
cmd = f'git add . && git commit -m "{local_time}" && git push origin main'

os.system(cmd)
