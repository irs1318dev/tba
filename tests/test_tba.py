import tba
import auth

def test_status():
    print()
    print("*****TESTING*****")
    data = tba.status(auth.key)
    print(data["text"])