#!/usr/bin/env python3
"""Simple HTTP server for Assortment Optimizer on port 5002"""
import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Assortment Optimizer → http://127.0.0.1:5002")
http.server.HTTPServer(("127.0.0.1", 5002), http.server.SimpleHTTPRequestHandler).serve_forever()
