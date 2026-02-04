import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Be My Valentine ❤️", layout="centered")

# --- CUSTOM CSS & HTML ---
# We wrap your HTML/CSS/JS into a single string to render it properly.
valentine_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        height: 100vh;
        background: linear-gradient(rgba(0,0,0,0.4), rgba(40,0,0,0.4)),
                    url("https://images.unsplash.com/photo-1445233566136-a2a4e2c38bc2?q=80&w=687&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        font-family: sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }

    .card {
        background: rgba(255, 255, 255, 0.9);
        width: 320px;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        animation: heartbeat 2.5s infinite;
        position: relative;
    }

    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        14% { transform: scale(1.05); }
        28% { transform: scale(1); }
        42% { transform: scale(1.05); }
    }

    h1 { color: #e63946; font-size: 1.5rem; }
    p { color: #555; }

    .buttons {
        margin-top: 20px;
        display: flex;
        justify-content: center;
        gap: 20px;
    }

    button {
        padding: 10px 20px;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        font-weight: bold;
        transition: 0.3s;
    }

    .yes { background: #e63946; color: white; }

    .no { 
        background: #ddd; 
        position: relative;
        transition: transform 0.2s ease-out;
    }

    .message {
        display: none;
        color: #e63946;
        font-weight: bold;
        margin-top: 20px;
        line-height: 1.5;
    }

    img {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 15px;
    }
</style>
</head>
<body>

<div class="card">
    <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmpib2V2cmxlb2wyZ2lucGJlOTRmaXNmcjd0cTA5M2QxZmsyanUwOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F6LkzS5hhek3fDKgwb/giphy.gif">
    <h1>Will you be my Valentine? 💖</h1>
    <p>Choose wisely... 😉</p>

    <div class="buttons" id="btnContainer">
        <button class="yes" onclick="showLove()">YES ❤️</button>
        <button class="no" id="noBtn" onmouseover="moveNo()" onclick="moveNo()">NO 🙈</button>
    </div>

    <div class="message" id="loveMessage">
        💕 Yayyyy! 💕<br>
        You've made me the happiest!<br>
        Happy Valentine's Day! ❤️
    </div>
</div>

<script>
    function moveNo() {
        const btn = document.getElementById('noBtn');
        // Calculate random movement within a reasonable range
        const x = Math.random() * 150 - 75;
        const y = Math.random() * 150 - 75;
        btn.style.transform = `translate(${x}px, ${y}px)`;
    }

    function showLove() {
        document.getElementById('btnContainer').style.display = 'none';
        document.getElementById('loveMessage').style.display = 'block';

        // Optional: Simple Confetti effect or logic
    }
</script>

</body>
</html>
"""

# --- STREAMLIT DISPLAY ---

# Injecting the HTML component
# We set the height to 600 or higher to ensure the "No" button has room to move
components.html(valentine_html, height=700)

# Sidebar for extra personalization (Optional Streamlit feature)
with st.sidebar:
    st.write("### Settings")
    name = st.text_input("Enter her/his name:", "Dear")
    st.info("The card above is fully interactive!")
