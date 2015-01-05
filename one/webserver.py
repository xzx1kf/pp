"""
Implement a HTTP web server in Python that knows how to run server-side
CGI scripts coded in Python; servers files and scrupts from current working
dir; Python scripts must be stored in webdir\cgi-bin or webdir\htbin;
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'    # where your html files and cgi-bin script diretory live
port = 8080       # default http://localhost/, else usr http://localhost:xxxx/

os.chdir(webdir)
srvaddr = ("", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()
