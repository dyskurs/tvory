from http.server import BaseHTTPRequestHandler, HTTPServer
import pandas as pd
import time
import markdown as md
import jinja2 as jj


templateLoader = jj.FileSystemLoader(searchpath="./")
templateEnv = jj.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"
template = templateEnv.get_template(TEMPLATE_FILE)


hostName = "localhost"
serverPort = 8080

df = pd.read_csv("central.csv")
endpoints = set(df["endpoint"])
templates = {}
for temp_name in set(df["template"]):
    with open("_layouts/{}.html".format(temp_name), "r") as fin:
        templates[temp_name] = fin.read()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("index.html"):
            self.path = self.path[:-10]
        if self.path in endpoints:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            info = df[df["endpoint"]==self.path].iloc[0]
            with open(info["folder"] + "/" + info["filename"], "r") as fin:
                content = fin.read()
            self.wfile.write(bytes(md.markdown(templates[info["template"]].format(content = content)), "utf-8"))
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(f"<html><head><title>https://pythonbasics.org</title></head><p>Request: {self.path}, response : 404 not found.</p></body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")