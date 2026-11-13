
import streamlit as st
from google import genai
from google.genai import types

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="AI Meeting Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- GEMINI CLIENT ----------------

# ---------------- GEMINI CLIENT ----------------

@st.cache_resource
def get_gemini_client():
    api_key = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(
        api_key=api_key
    )

    return client


try:
    client = get_gemini_client()

except Exception as e:
    client = None
    st.error(f"Gemini configuration error: {e}")

# ---------------- APPLICATION TITLE ----------------
st.title("🤖 AI-Powered Meeting-to-Action Assistant")

st.write(
    "Convert meeting transcripts into summaries, "
    "decisions, tasks and follow-up actions using AI."
)

st.divider()

# ---------------- TRANSCRIPT INPUT ----------------
st.subheader("📝 Enter Meeting Transcript")

transcript = st.text_area(
    "Paste your meeting conversation here:",
    height=250,
    placeholder="Example: Today we discussed the project..."
)

# ---------------- GENERATE SUMMARY ----------------
if st.button(
    "✨ Generate Meeting Summary",
    type="primary"
):

    if not transcript.strip():

        st.warning("Please enter a meeting transcript.")

    elif client is None:

        st.error(
            f"Gemini configuration error: {client_error}"
        )

    else:

        prompt = f"""
You are an intelligent AI meeting assistant.

Analyze the meeting transcript and create a professional report.

Include the following sections:

1. MEETING SUMMARY
Write a clear and concise summary.

2. KEY DISCUSSION POINTS
List all important topics discussed.

3. DECISIONS MADE
List the decisions taken during the meeting.

4. ACTION ITEMS
Create a table with:
- Task
- Responsible Person
- Deadline

Do not invent missing names or deadlines.

5. FOLLOW-UP ACTIONS
Mention the next steps.

If information is missing, write:
"Not specified in transcript".

MEETING TRANSCRIPT:
{transcript}
"""

        try:

            with st.spinner(
                "🤖 AI is analyzing your meeting..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                report = response.text

            if report:

                st.success(
                    "Meeting analysis completed successfully!"
                )

                st.divider()

                st.subheader(
                    "📊 AI Generated Meeting Report"
                )

                st.markdown(report)

                st.download_button(
                    label="📥 Download Meeting Report",
                    data=report,
                    file_name="meeting_report.md",
                    mime="text/markdown"
                )

            else:

                st.error(
                    "Gemini returned an empty response."
                )

        except Exception as e:

            st.error(
                f"Error generating summary: {str(e)}"
            )

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "M1-P2 | College AI Project | Powered by Google Gemini"
)
