
import streamlit as st
from google import genai

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="AI Advertisement Generator",
    page_icon="📢",
    layout="wide"
)

# ---------------------------------
# CUSTOM DESIGN
# ---------------------------------

st.title("📢 AI-Based Product Advertisement Generator")

st.markdown(
    "### Turn your product details into a complete advertising package!"
)

st.write(
    "Enter your product information, select your target audience, "
    "and let AI create professional marketing content for you."
)

st.divider()

# ---------------------------------
# PRODUCT INFORMATION
# ---------------------------------

st.subheader("🛍️ Product Information")

col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input(
        "Product Name",
        placeholder="Example: Smart Watch"
    )

    product_category = st.selectbox(
        "Product Category",
        [
            "Electronics",
            "Fashion",
            "Food and Beverages",
            "Beauty and Personal Care",
            "Home Appliances",
            "Education",
            "Sports",
            "Other"
        ]
    )

    price = st.text_input(
        "Product Price",
        placeholder="Example: ₹2,999"
    )

with col2:
    target_audience = st.selectbox(
        "Select Target Audience",
        [
            "Students",
            "Working Professionals",
            "Teenagers",
            "Families",
            "Business Owners",
            "Fitness Enthusiasts",
            "General Audience"
        ]
    )

    tone = st.selectbox(
        "Advertisement Tone",
        [
            "Professional",
            "Creative",
            "Funny",
            "Emotional",
            "Luxury",
            "Friendly"
        ]
    )

    platform = st.selectbox(
        "Social Media Platform",
        [
            "Instagram",
            "Facebook",
            "YouTube",
            "LinkedIn",
            "All Platforms"
        ]
    )

product_features = st.text_area(
    "Product Features and Description",
    placeholder="Enter the important features, benefits and details of your product...",
    height=120
)

st.divider()

# ---------------------------------
# GENERATE ADVERTISEMENT
# ---------------------------------

if st.button("✨ Generate Advertisement Package", type="primary"):

    if not product_name.strip() or not product_features.strip():
        st.warning("Please enter the product name and product features.")

    else:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]

            client = genai.Client(api_key=api_key)

            prompt = f"""
You are an expert digital marketing and advertising specialist.

Create a complete advertising package using the following information.

PRODUCT DETAILS:
Product Name: {product_name}
Category: {product_category}
Price: {price if price else "Not provided"}
Features: {product_features}

TARGET AUDIENCE: {target_audience}
ADVERTISEMENT TONE: {tone}
SOCIAL MEDIA PLATFORM: {platform}

Generate the following sections:

1. PRODUCT DESCRIPTION
Write an attractive and informative product description.

2. PROMOTIONAL TEXT
Create a persuasive promotional advertisement.

3. SOCIAL MEDIA CONTENT
Write an engaging social media post with relevant hashtags.

4. VISUAL CONCEPT
Suggest an image advertisement concept.
Include background, colours, product placement and text ideas.

5. VIDEO ADVERTISEMENT NARRATION
Write a short video advertisement script with a strong opening,
product benefits and a call to action.

6. MARKETING SLOGAN
Create three memorable advertising slogans.

IMPORTANT:
- Adapt all content to the selected target audience.
- Maintain the selected advertisement tone.
- Use clear and engaging language.
- Do not invent product specifications or benefits.
- Clearly label each section.
"""

            with st.spinner("AI is creating your advertisement package..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            result = response.text

            if result:
                st.success("Advertisement package generated successfully!")

                st.subheader("🎯 Your AI-Generated Advertisement Package")

                st.markdown(result)

                st.download_button(
                    label="⬇️ Download Advertisement Package",
                    data=result,
                    file_name="advertisement_package.md",
                    mime="text/markdown"
                )

            else:
                st.error("The AI returned an empty response. Please try again.")

        except Exception as e:
            st.error("Something went wrong while generating the advertisement.")
            st.code(str(e))

# ---------------------------------
# FOOTER
# ---------------------------------

st.divider()

st.caption(
    "AI-Based Product Advertisement Generator | College Project"
)
