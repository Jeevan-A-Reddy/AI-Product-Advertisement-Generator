
import tomllib
from google import genai
from google.genai import types

print("1. Reading API key...", flush=True)

with open(".streamlit/secrets.toml", "rb") as f:
    secrets = tomllib.load(f)

print("2. Connecting to Gemini...", flush=True)

client = genai.Client(
api_key=secrets["GEMINI_API_KEY"],
http_options=types.HttpOptions(timeout=30000)
)

print("3. Sending request to Gemini...", flush=True)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Say hello in one sentence."
    )

    print("4. SUCCESS!", flush=True)
    print(response.text, flush=True)

except Exception as e:
    print("4. REQUEST FAILED!", flush=True)
    print(type(e).__name__, flush=True)
    print(str(e), flush=True)

print("Test finished.", flush=True)
