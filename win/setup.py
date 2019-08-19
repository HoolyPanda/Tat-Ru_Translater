import os
import client

try:
    os.mkdir("C:\\Personal")
except Exception as e:
    print(str(e))
os.mkdir("C:\\Personal\\ElinorTranslater")
c = client.Client()
c.PullDict()