from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    #define a generic exception
    error = Exception("Ops, algo errado.")
    #parse url into 6 components. we will use only netloc (indicium.tech)
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    # Starts a for loop using HTTP (80) and HTTPs (443) ports
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception:
            print(error)
        finally:
            connection.close()