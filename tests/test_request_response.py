from app.pipeline.request import Request
from app.pipeline.response import Response

req = Request("Open Notepad")
print(req)

res = Response(True, "Opening Notepad")
print(res)
