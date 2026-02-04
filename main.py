import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Set page config
st.set_page_config(page_title="Be My Valentine ❤️", layout="centered")

# Sidebar for extra personalization
with st.sidebar:
    st.write("### Settings")
    name = st.text_input("Enter her/his name:", "Dear")
    st.info("The card above is fully interactive!")

# Locate test.html next to this script and read it (safe fallback if missing)
html_path = Path(__file__).resolve().parent / "test.html"
if html_path.exists():
    try:
        html_content = html_path.read_text(encoding="utf-8")
    except Exception as e:
        html_content = f"<div style='padding:20px; color:darkred;'>Error reading test.html: {e}</div>"
else:
    html_content = (
        "<div style='padding:20px; font-family:system-ui, sans-serif;'>"
        "<h1>Be My Valentine ❤️</h1>"
        f"<p>Could not find <code>{html_path.name}</code>. Using fallback content.</p>"
        "</div>"
    )

# Replace optional placeholder {{name}} in the HTML with the sidebar input
valentine_html = html_content.replace("{{name}}", name)

# Render the HTML component
components.html(valentine_html, height=700, scrolling=True)
