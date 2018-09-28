import urllib.request

import auth

def GetStatus():
    hdrs = {"X-TBA-Auth-Key": auth.key, "User-Agent": "jared-at-the-lush-store"}
    req = urllib.request.Request("http://www.thebluealliance.com/api/v3/status", headers=hdrs)

    response = urllib.request.urlopen(req)

    print(response.read())

GetStatus()
