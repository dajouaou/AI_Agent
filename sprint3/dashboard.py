import urllib.parse
import streamlit as st

from app.agent import run_agent
from app.logger import log_event
from app.feedback_manager import save_feedback, count_feedback


st.set_page_config(
    page_title="DEAI AI-Agent",
    page_icon="🎓",
    layout="wide"
)


def create_mailto_link(question, confidence):
    receiver = "24054992@student.hhs.nl"
    subject = "Vraag vanuit Semester 4 AI-Agent"
    body = f"""Beste docent,

De AI-Agent kon deze vraag niet met voldoende zekerheid beantwoorden.

Vraag:
{question}

Confidence:
{confidence}%

Kunt u hierbij helpen?

Met vriendelijke groet,
Semester 4 AI-Agent
"""

    return (
        f"mailto:{receiver}"
        f"?subject={urllib.parse.quote(subject)}"
        f"&body={urllib.parse.quote(body)}"
    )


st.markdown("""
<style>
.stApp {
    background: #f4f6f8;
    color: #10213f;
}

.block-container {
    max-width: 1250px;
    padding-top: 0.5rem !important;
}

.header {
    background: #ffffff;
    border-left: 10px solid #a6b400;
    padding: 22px 30px;
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(16, 31, 61, 0.08);
    margin-bottom: 20px;
}

.header-title {
    font-size: 30px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #10213f;
}

.header-subtitle {
    margin-top: 6px;
    color: #475569;
    font-size: 16px;
}

.intro {
    background: linear-gradient(120deg, #a6b400 0%, #a6b400 30%, #10213f 30%, #10213f 100%);
    padding: 28px;
    border-radius: 18px;
    margin-bottom: 20px;
}

.intro-card {
    background: white;
    width: 450px;
    padding: 26px;
    border-radius: 10px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.16);
}

.intro-title {
    font-size: 34px;
    font-weight: 900;
    color: #10213f;
    line-height: 1.1;
}

.intro-text {
    margin-top: 12px;
    font-size: 16px;
    color: #334155;
}

.panel-top {
    background: #10213f;
    color: white;
    padding: 18px 20px;
    border-radius: 16px;
    margin-bottom: 18px;
}

.panel-top h3 {
    color: white;
    margin: 0;
    font-size: 22px;
}

.panel-top p {
    color: #dbeafe;
    margin: 6px 0 0 0;
    font-size: 14px;
}

.badge {
    background: #a6b400;
    color: #10213f;
    padding: 8px 14px;
    border-radius: 8px;
    font-weight: 800;
    display: inline-block;
    margin-bottom: 12px;
}

.section-title {
    font-size: 25px;
    font-weight: 900;
    color: #10213f;
    margin-bottom: 8px;
}

.feature {
    background: #f8fafc;
    border-left: 5px solid #a6b400;
    padding: 10px 12px;
    margin-bottom: 10px;
    border-radius: 8px;
    color: #10213f;
    font-weight: 600;
}

.escalation-box {
    background: #fff7ed;
    border-left: 6px solid #f97316;
    padding: 14px;
    border-radius: 10px;
    color: #10213f;
    margin-bottom: 12px;
    font-weight: 600;
}

.mail-button {
    display: inline-block;
    background: #10213f;
    color: white !important;
    padding: 12px 18px;
    border-radius: 10px;
    text-decoration: none !important;
    font-weight: 800;
    margin-bottom: 15px;
}

.mail-button:hover {
    background: #a6b400;
    color: #10213f !important;
}

.stButton>button {
    background: #10213f !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    min-height: 44px;
    font-weight: 700 !important;
}

.stButton>button:hover {
    background: #a6b400 !important;
    color: #10213f !important;
}

[data-testid="stChatMessage"] {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 10px;
    margin-bottom: 10px;
}

[data-testid="stChatMessage"] p {
    color: #10213f !important;
    font-size: 16px;
}

.stMarkdown, .stMarkdown p, .stMarkdown li {
    color: #10213f;
}

label,
label p,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p {
    color: #10213f !important;
    opacity: 1 !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Welkom! Ik ben jouw Semester 4 DEAI AI-Agent. "
                "Stel een vraag over DEAI, PD3, niveautests, beoordeling of het AI-Agent project."
            )
        }
    ]

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "last_question" not in st.session_state:
    st.session_state.last_question = None


st.markdown("""
<div class="header">
    <div class="header-title">DE HAAGSE HOGESCHOOL</div>
    <div class="header-subtitle">Semester 4 | Data Engineering & AI | AI-Agent Study Assistant</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="intro">
    <div class="intro-card">
        <div class="intro-title">Semester 4<br>DEAI AI-Agent</div>
        <div class="intro-text">
            Een slimme chatbot die zoekt in jullie Semester 4 knowledge base
            en antwoorden geeft met confidence score, logging, feedback en docent-escalatie.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


left, right = st.columns([2.2, 1], gap="large")


with left:
    st.markdown("""
    <div class="panel-top">
        <h3>💬 Chat met de AI-Agent</h3>
        <p>Stel vragen over Semester 4. De agent gebruikt RAG en zoekt in de kennisbank.</p>
    </div>
    """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    st.markdown("### Snelle vragen")

    c1, c2, c3 = st.columns(3)
    prompt = None

    with c1:
        if st.button("Wat is DEAI?", use_container_width=True):
            prompt = "Wat is DEAI?"
        if st.button("Wat leer je in semester 4?", use_container_width=True):
            prompt = "Wat leer je in semester 4?"

    with c2:
        if st.button("Wat houdt PD3 in?", use_container_width=True):
            prompt = "Wat houdt PD3 in?"
        if st.button("Wanneer is de ML niveautest?", use_container_width=True):
            prompt = "Wanneer is de Machine Learning niveautest?"

    with c3:
        if st.button("Hoe wordt semester 4 beoordeeld?", use_container_width=True):
            prompt = "Hoe wordt semester 4 beoordeeld?"
        if st.button("Wat is het AI-Agent project?", use_container_width=True):
            prompt = "Wat is het AI-Agent project?"

    typed_question = st.chat_input("Typ hier je vraag...")

    if typed_question:
        prompt = typed_question

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("De agent zoekt in de Semester 4 kennisbank..."):
            result = run_agent(prompt)

        st.session_state.last_result = result
        st.session_state.last_question = prompt
        st.session_state.messages.append({"role": "assistant", "content": result["answer"]})

        log_event(
            f"Vraag: {prompt} | Confidence: {result['confidence']} | Status: {result['status']}"
        )

        st.rerun()


with right:
    st.markdown("""
    <div class="panel-top">
        <h3>📊 Dashboard</h3>
        <p>Live status van de AI-agent workflow.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="badge">POC Sprint 3</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📈 Analytics</div>', unsafe_allow_html=True)

    vragen = max(0, len(st.session_state.messages) // 2)
    feedbacks = count_feedback()
    confidence = "Nog geen data"

    if st.session_state.last_result:
        confidence = f'{st.session_state.last_result["confidence"]}%'

    st.markdown(f"""
    <div class="feature">📨 Aantal vragen: <b>{vragen}</b></div>
    <div class="feature">👍 Ontvangen feedback: <b>{feedbacks}</b></div>
    <div class="feature">🎯 Laatste confidence: <b>{confidence}</b></div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown('<div class="section-title">🤖 Status</div>', unsafe_allow_html=True)

    if st.session_state.last_result:
        st.write("**Confidence**")
        st.progress(st.session_state.last_result["confidence"] / 100)
        st.write(f'{st.session_state.last_result["confidence"]}% zekerheid')

        st.write("**Status**")
        st.write(st.session_state.last_result["status"])

        if (
            st.session_state.last_result["confidence"] < 70
            or st.session_state.last_result["status"] == "escalated"
            or st.session_state.last_result["status"] == "needs_clarification"
        ):
            mail_link = create_mailto_link(
                st.session_state.last_question,
                st.session_state.last_result["confidence"]
            )

            st.markdown("""
            <div class="escalation-box">
                ⚠️ De AI-Agent weet dit niet zeker. Stuur de vraag door naar een docent.
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                f'<a class="mail-button" href="{mail_link}" target="_blank">📧 Mail docent</a>',
                unsafe_allow_html=True
            )

            log_event(
                f"Escalatie beschikbaar | Vraag: {st.session_state.last_question} | "
                f"Confidence: {st.session_state.last_result['confidence']}"
            )

    else:
        st.info("Nog geen vraag gesteld.")

    st.divider()

    st.markdown('<div class="section-title">📚 Knowledge Base</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">Semester 4 algemeen</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">DEAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">PD3</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">Niveautests</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">AI-Agent project</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">Beoordeling</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown('<div class="section-title">✅ Techniek</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">RAG + semantic search</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">HuggingFace embeddings</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">ChromaDB vector database</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">Validation + confidence score</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">Logging + feedbackloop</div>', unsafe_allow_html=True)
    st.markdown('<div class="feature">Docent-escalatie via mailto</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown('<div class="section-title">💬 Feedback</div>', unsafe_allow_html=True)

    feedback = st.selectbox(
        "Was het laatste antwoord nuttig?",
        ["Ja", "Nee", "Gedeeltelijk"]
    )

    if st.button("Feedback opslaan", use_container_width=True):
        if st.session_state.last_result:
            save_feedback(
                question=st.session_state.last_question,
                feedback=feedback,
                confidence=st.session_state.last_result["confidence"],
                status=st.session_state.last_result["status"]
            )

            log_event(
                f"Feedback opgeslagen | Vraag: {st.session_state.last_question} | Feedback: {feedback}"
            )
            st.success("Feedback opgeslagen in feedback.csv.")
        else:
            st.warning("Stel eerst een vraag voordat je feedback opslaat.")

    if st.button("Chat wissen", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat gewist. Stel gerust een nieuwe vraag."
            }
        ]
        st.session_state.last_result = None
        st.session_state.last_question = None
        st.rerun()