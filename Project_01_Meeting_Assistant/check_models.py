
from google import genai
import tomllib

with open(".streamlit/secrets.toml", "rb") as f:
    secrets = tomllib.load(f)

client = genai.Client(
    api_key=secrets["GEMINI_API_KEY"]
)

print("Checking models available to your API key...\n")

try:
    for model in client.models.list():
        supported = getattr(model, "supported_actions", []) or []

        if "generateContent" in supported:
            print(model.name)

except Exception as e:
    print("ERROR:", type(e).__name__, str(e))
