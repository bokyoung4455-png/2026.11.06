import streamlit as st

st.set_page_config(
    page_title="나를 소개합니다",
    page_icon="🌃",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #f4f3ff;
        --muted: #a4a8c4;
        --line: rgba(195, 199, 255, 0.14);
        --violet: #a78bfa;
        --cyan: #67e8f9;
    }

    .stApp {
        color: var(--ink);
        background:
            radial-gradient(ellipse at 82% 8%, rgba(109, 72, 196, 0.25), transparent 34%),
            radial-gradient(ellipse at 8% 30%, rgba(29, 96, 142, 0.17), transparent 32%),
            linear-gradient(160deg, #090d1a 0%, #11152a 54%, #090d19 100%);
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }

    .block-container {
        max-width: 1120px;
        padding: 2rem 2rem 4rem;
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"] { right: 1rem; }

    .cityscape {
        position: relative;
        overflow: hidden;
        min-height: 390px;
        display: flex;
        align-items: center;
        padding: 3.5rem 3.2rem;
        border: 1px solid var(--line);
        border-radius: 28px;
        background:
            linear-gradient(90deg, rgba(10, 14, 29, .98) 0%, rgba(13, 17, 36, .86) 55%, rgba(15, 20, 42, .38) 100%),
            radial-gradient(ellipse at 78% 18%, rgba(127, 93, 231, .38), transparent 34%),
            linear-gradient(145deg, #19213e, #11172c 62%, #101427);
        box-shadow: 0 24px 80px rgba(0, 0, 0, .28);
    }

    .cityscape::before {
        content: "";
        position: absolute;
        inset: auto 0 0;
        height: 46%;
        opacity: .7;
        background:
            linear-gradient(90deg, transparent 0 4%, #202747 4% 9%, transparent 9% 12%, #18213f 12% 18%, transparent 18% 21%, #252b50 21% 28%, transparent 28% 32%, #1c2546 32% 38%, transparent 38% 42%, #252a4c 42% 49%, transparent 49% 53%, #1c2341 53% 59%, transparent 59% 63%, #25294c 63% 70%, transparent 70% 74%, #1c2342 74% 82%, transparent 82% 86%, #25294a 86% 93%, transparent 93%),
            linear-gradient(to top, #11162a 0%, rgba(17, 22, 42, .7) 70%, transparent 100%);
        clip-path: polygon(0 34%, 4% 34%, 4% 11%, 9% 11%, 9% 43%, 12% 43%, 12% 24%, 18% 24%, 18% 50%, 21% 50%, 21% 0, 28% 0, 28% 37%, 32% 37%, 32% 17%, 38% 17%, 38% 46%, 42% 46%, 42% 26%, 49% 26%, 49% 53%, 53% 53%, 53% 9%, 59% 9%, 59% 39%, 63% 39%, 63% 20%, 70% 20%, 70% 47%, 74% 47%, 74% 13%, 82% 13%, 82% 42%, 86% 42%, 86% 26%, 93% 26%, 93% 0, 100% 0, 100% 100%, 0 100%);
        pointer-events: none;
    }

    .cityscape::after {
        content: "";
        position: absolute;
        inset: 0;
        opacity: .28;
        background-image: radial-gradient(rgba(230, 230, 255, .8) .7px, transparent .7px);
        background-size: 41px 41px;
        mask-image: linear-gradient(to bottom, black, transparent 76%);
        pointer-events: none;
    }

    .hero-content { position: relative; z-index: 1; max-width: 650px; }
    .eyebrow {
        color: var(--cyan);
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .2em;
        text-transform: uppercase;
    }
    .hero-content h1 {
        margin: .8rem 0 .45rem;
        color: var(--ink);
        font-size: clamp(2.6rem, 7vw, 5.2rem);
        font-weight: 800;
        letter-spacing: -.06em;
        line-height: 1.08;
    }
    .hero-content h1 span {
        color: var(--violet);
        text-shadow: 0 0 32px rgba(167, 139, 250, .4);
    }
    .hero-content p {
        margin: 0;
        color: #c2c6df;
        font-size: 1.05rem;
        line-height: 1.8;
    }
    .hero-meta {
        display: flex;
        flex-wrap: wrap;
        gap: .65rem;
        margin-top: 1.6rem;
    }
    .pill {
        padding: .48rem .8rem;
        border: 1px solid rgba(195, 199, 255, .2);
        border-radius: 999px;
        background: rgba(255, 255, 255, .055);
        color: #e6e5f7;
        font-size: .84rem;
    }
    .section-label {
        margin: 2.5rem 0 1rem;
        color: var(--cyan);
        font-size: .75rem;
        font-weight: 700;
        letter-spacing: .19em;
    }
    .section-title {
        margin: 0 0 1.25rem;
        color: var(--ink);
        font-size: 1.75rem;
        font-weight: 700;
        letter-spacing: -.04em;
    }
    .info-card {
        height: 100%;
        min-height: 150px;
        padding: 1.35rem 1.45rem;
        border: 1px solid var(--line);
        border-radius: 18px;
        background: linear-gradient(145deg, rgba(31, 37, 67, .78), rgba(17, 22, 42, .78));
    }
    .info-card .icon { font-size: 1.35rem; }
    .info-card h3 {
        margin: .75rem 0 .35rem;
        color: #e9e9fa;
        font-size: 1rem;
    }
    .info-card p {
        margin: 0;
        color: var(--muted);
        font-size: .92rem;
        line-height: 1.65;
    }
    .about-card {
        padding: 1.7rem 1.8rem;
        border: 1px solid var(--line);
        border-left: 3px solid var(--violet);
        border-radius: 16px;
        background: rgba(25, 30, 55, .72);
        color: #c4c7dc;
        line-height: 1.9;
    }
    .contact-card {
        padding: 1.5rem;
        border: 1px solid rgba(103, 232, 249, .2);
        border-radius: 18px;
        background: linear-gradient(110deg, rgba(27, 47, 69, .65), rgba(31, 31, 63, .65));
        color: #d7d9ec;
        line-height: 1.8;
        text-align: center;
    }
    .footer {
        margin-top: 3rem;
        color: #858aa8;
        font-size: .8rem;
        text-align: center;
    }

    @media (max-width: 640px) {
        .block-container { padding: 1rem 1rem 3rem; }
        .cityscape { min-height: 350px; padding: 2rem 1.5rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="cityscape">
      <div class="hero-content">
        <div class="eyebrow">A LITTLE INTRODUCTION</div>
        <h1>안녕하세요,<br><span>문보경</span>입니다.</h1>
        <p>나만의 이야기를 이곳에 적어보세요.<br>관심 있는 일과 앞으로의 목표를 소개할 수 있어요.</p>
        <div class="hero-meta">
          <span class="pill">🏙️ 소속을 입력하세요</span>
          <span class="pill">✦ MBTI 입력</span>
          <span class="pill">📍 활동 지역 입력</span>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">01 / ABOUT ME</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">저를 소개합니다</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="about-card">
      자기소개를 여기에 작성해 보세요. 현재 하고 있는 일이나 공부, 중요하게 생각하는 가치,
      앞으로 이루고 싶은 목표 등을 두세 문장으로 적으면 좋아요.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">02 / MY INTERESTS</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">요즘 관심 있는 것</h2>', unsafe_allow_html=True)

interest_columns = st.columns(3)
interests = [
    ("✦", "관심사 하나", "좋아하는 활동이나 주제를 소개해 보세요."),
    ("⌘", "관심사 둘", "최근 배우고 있거나 도전 중인 것을 적어보세요."),
    ("☕", "관심사 셋", "나를 잘 설명해 주는 취미를 추가해 보세요."),
]

for column, (icon, title, description) in zip(interest_columns, interests):
    with column:
        st.markdown(
            f"""
            <div class="info-card">
              <div class="icon">{icon}</div>
              <h3>{title}</h3>
              <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-label">03 / SAY HELLO</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">함께 이야기 나눠요</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="contact-card">
      새로운 인연과 아이디어를 환영합니다.<br>
      연락처나 소셜 미디어 링크를 이곳에 추가해 보세요.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="footer">나만의 색으로 채워가는 자기소개 페이지</div>', unsafe_allow_html=True)
