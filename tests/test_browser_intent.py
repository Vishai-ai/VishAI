from app.intents.browser_intent import BrowserIntent
from app.pipeline.request import Request

intent = BrowserIntent()

request = Request(
    text="search python tutorial"
)

response = intent.handle(request)

print(response.message)