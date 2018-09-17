import json
import urllib.request

import auth

def status(key):
    base_url = "https://www.thebluealliance.com/api/v3"

    full_url = base_url + "/status"

    hdrs = {"X-TBA-Auth-Key": key,
            "User-Agent": "FRC 1318 Python Code"}

    data = {}
    req = urllib.request.Request(full_url, headers=hdrs)

    with urllib.request.urlopen(req) as resp:
        data["code"] = resp.getcode()
        data["text"] = json.loads(resp.read())

    return data


result = status(auth.key)
print(result["text"])
