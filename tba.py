import urllib.request
import warnings

def status(key):
    base_url = "https://www.thebluealliance.com/api/v3"

    full_url = base_url + "/status"

    hdrs = {"X-TBA-Auth-Key": key}


    data = {}
    req = urllib.request.Request(full_url, headers=hdrs)
    try:
        with urllib.request.urlopen(req) as resp:
            data["code"] = resp.getcode()
            # Using json.dumps(json.loads()) to remove carriage returns from
            #   json text provided by Blue Allianc.
            data["text"] = json.dumps(json.loads(resp.read().decode("utf-8")))
            data["url"] = resp.geturl()
            for key, value in resp.info().items():
                data[key] = value
    except urllib.error.HTTPError as err:
        data["code"] = err.code
        data["url"] = err.url
        for key, value in err.headers.items():
            data[key] = value
        if err.code != 304:
            data["error_message"] = "HTTPError, Code {}: {}".format(err.code,
                                                                    err.reason)
            warnings.warn(data["error_message"])
    except urllib.error.URLError as err:
        data["error_message"] = "URLError: {}".format(err.reason)
        warnings.warn(data["error_message"])
    return data