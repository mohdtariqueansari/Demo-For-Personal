
import streamlit as st
import streamlit.components.v1 as components
import base64
import mimetypes
import os

st.set_page_config(
    page_title="My Forever Love",
    page_icon="💕",
    layout="centered"
)

# Apni photo ka path yahan set karo
PHOTO_PATH = r"C:\Users\hp\Downloads\For HerStreamLit\MeandHer.jpeg"

photo_html = ""

if os.path.exists(PHOTO_PATH):
    mime_type = mimetypes.guess_type(PHOTO_PATH)[0] or "image/jpeg"

    with open(PHOTO_PATH, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    photo_html = f"""
        <img class="couple-photo"
        src="data:{mime_type};base64,{encoded}"
        alt="Our beautiful memory">
    """
else:
    photo_html = """
        <p style="color:#d63384">
        Photo nahi mili. PHOTO_PATH check karo.
        </p>
    """

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: 'Trebuchet MS', sans-serif;
    background: #fff0f5;
}

.main {
    min-height: 650px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px;
}

.card {
    width: 100%;
    max-width: 650px;
    min-height: 480px;
    background: #ffe0eb;
    border: 3px solid #ffb6cf;
    border-radius: 35px;
    padding: 35px 20px;
    text-align: center;
    box-shadow: 0 12px 35px #f5a6c244;
    position: relative;
    overflow: hidden;
}

.heart {
    font-size: 48px;
    animation: beat 1s infinite;
}

@keyframes beat {
    50% { transform: scale(1.12); }
}

h1 {
    color: #d63384;
    font-size: clamp(27px, 5vw, 38px);
    margin: 18px 0;
}

p {
    color: #c02d76;
    font-size: 18px;
    line-height: 1.6;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 25px;
    margin-top: 30px;
    min-height: 55px;
}

button {
    padding: 13px 32px;
    border: none;
    border-radius: 25px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}

#yes {
    color: white;
    background: #ff69a6;
}

#no {
    color: #d63384;
    background: white;
}

#success {
    display: none;
}

.couple-photo {
    display: block;
    width: 100%;
    max-width: 300px;
    max-height: 350px;
    object-fit: cover;
    border: 5px solid white;
    border-radius: 22px;
    margin: 20px auto;
    box-shadow: 0 5px 18px #d8709355;
}

.love-note {
    font-size: 19px;
    margin: 12px 0;
}

.hearts {
    font-size: 30px;
    margin-top: 25px;
}

#no.running {
    position: fixed;
    z-index: 9999;
}

</style>
</head>

<body>
<div class="main">
<div class="card" id="card">

    <section id="question">
        <div class="heart">💗</div>

        <h1>Will you marry me?</h1>

        <p>
        You're my favourite person in the whole world!
        </p>

        <div class="buttons">
            <button id="yes">Yes 💖</button>
            <button id="no">No 🙈</button>
        </div>
    </section>

    <section id="success">
        <div class="heart">💖</div>

        __PHOTO__

        <h1>Awww! 🥹💕</h1>

        <p class="love-note">
        I knew you'd say yes!
        </p>

        <p class="love-note">
        You've just made me the happiest person ever.
        </p>

        <p class="love-note">
        Here's to our forever! 💍
        </p>

        <div class="hearts">
        💕 💗 💖 💘 💕
        </div>
    </section>

</div>
</div>

<script>
const yesBtn = document.getElementById("yes");
const noBtn = document.getElementById("no");
const question = document.getElementById("question");
const success = document.getElementById("success");

function moveNo() {
    const maxX = Math.max(0, window.innerWidth - noBtn.offsetWidth);
    const maxY = Math.max(0, window.innerHeight - noBtn.offsetHeight);

    noBtn.classList.add("running");
    noBtn.style.left = Math.random() * maxX + "px";
    noBtn.style.top = Math.random() * maxY + "px";
}

noBtn.addEventListener("click", moveNo);

yesBtn.addEventListener("click", function() {
    question.style.display = "none";
    noBtn.style.display = "none";
    success.style.display = "block";
});
</script>

</body>
</html>
"""

html_code = html_code.replace("__PHOTO__", photo_html)

components.html(
    html_code,
    height=850,
    scrolling=True
)