from proxy_checker import ProxyChecker
from flask import *

app=Flask(__name__)
app.secret_key="okVaiProxyCheckV1.0"

def chk(proxy):
    checker = ProxyChecker()
    ok=checker.check_proxy(proxy)
    if ok==False:
        return { "country":None, "country_code": None, "protocols": [], "anonymity": None, "timeout": None }
    else:
        return ok

@app.route("/")
def apiChk():
    if request.args.get("proxy"):
        pro=request.args.get("proxy")
        return chk(pro)
    else:
        return """{ "country":None, "country_code": None, "protocols": [], "anonymity": None, "timeout": None }"""

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")