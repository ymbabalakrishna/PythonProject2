import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import re
import base64

# Render the raw HTML file as a full-page component (no sidebar, no audio)
st.set_page_config(page_title="Be My Valentine ❤️", layout="wide")

html_path = Path(__file__).resolve().parent / "test.html"
if not html_path.exists():
    st.error(f"Could not find {html_path.name} next to main.py")
    st.stop()

# Read the HTML
html_content = html_path.read_text(encoding="utf-8")

# If test.html references styles.css, embed it as a data URI so the iframe can load it
link_pattern = re.compile(r'(?i)(<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\'])(styles\.css)(["\'][^>]*>)')
css_path = html_path.parent / "styles.css"
if css_path.exists() and link_pattern.search(html_content):
    try:
        css_text = css_path.read_text(encoding="utf-8")
        b64 = base64.b64encode(css_text.encode('utf-8')).decode('ascii')
        data_uri = f"data:text/css;base64,{b64}"
        # replace only the href target (keep original attributes)
        html_content = link_pattern.sub(rf"\1{data_uri}\3", html_content, count=1)
    except Exception as e:
        st.warning(f"Could not embed styles.css: {e}")

# Remove any <audio>...</audio> blocks to disable audio playback inside Streamlit
html_content = re.sub(r'(?is)<audio\b.*?>.*?</audio>', '', html_content)

# Render the page. Use a large height so it looks like a full page; increase if needed.
components.html(html_content, height=1000, scrolling=True)
