from app.pipeline.request import Request

request = Request("open notepad")

request.parsed_command = {
    "action": "open_app",
    "target": "notepad"
}

print(request)