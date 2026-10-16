import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# Page setup optimized for mobile Chrome
st.set_page_config(
    page_title="Taly & Brooks Studio Engine",
    page_icon="🎬",
    layout="centered"
)

# Initialize Gemini Client via Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("API Key missing! Add GEMINI_API_KEY in Streamlit Cloud Settings > Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# Permanent Semantic Biometric Specifications
TALY_TOKENS = """
[TALULAH (TALY) BIOMETRIC PROFILE]
- Stature & Anatomy: Statuesque 6-foot tall athletic female frame commanding vertical scale with elongated limb proportions. Pronounced athletic hourglass silhouette featuring a full, naturally contoured bustline with soft natural drape and projection filling out the garment line. Aggressively tapered, narrow slanting waistline with sharp lateral indentation and sculpted oblique definition transitioning over a toned, flat abdomen. High pelvic flare opening into rounded, prominent gluteal curves establishing a high waist-to-hip ratio. Long sculptural legs displaying a distinct daylight thigh gap and defined sweeping oval frontal quadricep development tapering cleanly to lean calves and ankles. Natural unretouched skin texture balancing defined athletic tone with smooth feminine softness.
- Facial Identity: Sculpted high cheekbones, clean mandibular jawline, hooded almond hazel-green eyes with calm, magnetic direct gaze, straight nasal bridge, full naturally contoured lips. Glossy, sun-bleached golden-blonde beach waves.
- Stylistic Tone: High-fashion editorials, combat conditioning, heritage royal drapery, brutalist architecture, bold 35mm captures.
"""

BROOKS_TOKENS = """
[BROOKS BIOMETRIC PROFILE]
- Stature & Anatomy: Statuesque 6-foot tall athletic female frame with long, elegant limb proportions. Naturally contoured, lithe athletic hourglass silhouette featuring a firm, naturally full bustline with soft natural drape and projection. Slender, tapered narrow waistline transitioning smoothly over a completely flat, toned abdomen with a subtle natural vertical midline. Smooth, high feminine pelvic flare creating a distinct waist-to-hip curve and naturally rounded, firm athletic glutes. Elongated sculptural legs displaying a clean daylight thigh gap and smooth, streamlined quadricep tone tapering gracefully to lean calves and slender ankles. Sun-kissed golden-tan skin texture balancing lean athletic definition with soft, youthful feminine touch.
- Facial Identity: Fresh feminine softness, softly tapered jawline with a delicate rounded chin, supple plump cheeks with healthy youthful volume and zero gauntness or hollows. Striking hooded almond hazel-green eyes, soft naturally arched brows, straight refined nasal bridge, full naturally plump lips. Glossy dark brunette hair with honey sun-highlights in loose beach waves or textured braid.
- Stylistic Tone: Coastal minimalism, unbuttoned washed linen, headland walks, rocky trails, organic earth tones, candid documentary 35mm film.
"""

SYSTEM_PROMPT = f"""
You are the Technical Cinematographer and Visual Prompt Engineer for the virtual creator duo "Talulah & Brooks".
Your job is to generate production-ready prompts that maintain strict anatomical and facial fidelity while strictly adhering to safety filters.

{TALY_TOKENS}

{BROOKS_TOKENS}

DELIVERABLE FORMAT RULES:
For every generation request, output the following structured blocks:

1. MASTER KEYFRAME STILL PROMPT (For Google AI Studio / Imagen 3):
- Clean, photographic, high-fidelity prompt.
- Explicit lighting setup, camera focal length (85mm/35mm), authentic film stock grain, and environmental physics.
- Include the exact character biometric description at the front.

2. THREE SEQUENTIAL VIDEO GENERATION PROMPTS (For Google Flow / Veo 3):
- Clip 1 (0:00 - 0:03.5): Establishing kinetic hook with continuous camera dolly or tracking.
- Clip 2 (0:03.5 - 0:07.0): Micro-action, fabric/wind interaction, or environmental motion.
- Clip 3 (0:07.0 - 0:10.5): Direct lens engagement, facial focus, subtle half-smile, and seamless loop reset.

SAFETY DIRECTIVE:
Never use explicit lingerie or suggestive words. Use filter-safe terms like "athletic performance activewear", "washed linen overshirt", or "heritage silk drape". Video prompts must focus strictly on camera trajectory, wind physics, lighting, and natural expression.
"""

st.title("🎬 Taly & Brooks Studio")
st.caption("Automated Dual-Persona Production Suite")

# Persona Selector
persona = st.radio(
    "Select Persona:",
    ["Talulah (Taly)", "Brooks", "Talulah & Brooks (Duo)"],
    horizontal=True
)

# Reference Anchors Display
st.markdown("### 📌 Active Master Anchors")
col1, col2, col3 = st.columns(3)

def load_anchor(filename):
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        return Image.open(path)
    return None

if persona == "Talulah (Taly)":
    img_face = load_anchor("taly_face_anchor.jpg")
    img_body = load_anchor("taly_body_anchor.jpg")
    img_rear = load_anchor("taly_rear_anchor.jpg")
    with col1:
        if img_face: st.image(img_face, caption="Taly Face Anchor", use_container_width=True)
    with col2:
        if img_body: st.image(img_body, caption="Taly Frontal Body", use_container_width=True)
    with col3:
        if img_rear: st.image(img_rear, caption="Taly Rear / Profile", use_container_width=True)

elif persona == "Brooks":
    img_face = load_anchor("brooks_face_anchor.jpg")
    img_body = load_anchor("brooks_body_anchor.jpg")
    img_rear = load_anchor("brooks_rear_anchor.jpg")
    with col1:
        if img_face: st.image(img_face, caption="Brooks Face Anchor", use_container_width=True)
    with col2:
        if img_body: st.image(img_body, caption="Brooks Frontal Body", use_container_width=True)
    with col3:
        if img_rear: st.image(img_rear, caption="Brooks Rear / Profile", use_container_width=True)

else:
    t_face = load_anchor("taly_face_anchor.jpg")
    b_face = load_anchor("brooks_face_anchor.jpg")
    with col1:
        if t_face: st.image(t_face, caption="Talulah (Blonde)", use_container_width=True)
    with col2:
        if b_face: st.image(b_face, caption="Brooks (Brunette)", use_container_width=True)

# Prompt Controls
st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    lighting = st.selectbox(
        "Lighting Setup:",
        ["Warm Golden Hour Sunset", "Diffused Studio Softbox", "Moody Chiaroscuro / Candlelight", "Crisp Overcast Coastal Mist"]
    )
with c2:
    vibe = st.selectbox(
        "Expression & Presence:",
        ["Quiet & Contemplative", "Teasing & Playful Smirk", "Direct Magnetic Gaze", "Athletic Intensity"]
    )

scene_action = st.text_area(
    "Scene Action / Concept:",
    placeholder="e.g. Walking along a rugged sandstone cliff path in a breeze, looking toward the horizon..."
)

if st.button("🚀 Generate Production Suite", type="primary", use_container_width=True):
    if not scene_action.strip():
        st.warning("Please type a scene concept first.")
    else:
        with st.spinner("Compiling production prompts..."):
            try:
                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash",
                    system_instruction=SYSTEM_PROMPT
                )
                user_query = f"""
                Selected Persona: {persona}
                Lighting Environment: {lighting}
                Vibe / Mood: {vibe}
                Action / Staging: {scene_action}
                """
                response = model.generate_content(user_query)
                st.markdown("### 📋 Production Deliverables")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Generation error: {str(e)}")
