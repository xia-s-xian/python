import time
import pysvn

work_path = 'http://10.0.2.88/svn/VimcBT/VA9638B/Doc/QA/V0.4'

print(dir(pysvn.wc_notify_action)

client = pysvn.Client()



entry = client.log(work_path,limit=10)




