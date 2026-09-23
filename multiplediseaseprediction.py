import pickle

import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Pulse | Health screening",
    page_icon="+",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def load_models():
    with open("diabetes_model.sav", "rb") as file:
        diabetes = pickle.load(file)
    with open("heart_disease_model.sav", "rb") as file:
        heart = pickle.load(file)
    with open("parkinsons_model.sav", "rb") as file:
        parkinsons = pickle.load(file)
    return diabetes, heart, parkinsons


diabetes_model, heart_disease_model, parkinsons_model = load_models()

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap');
        :root { --ink:#183236; --muted:#718387; --line:#dce8e7; --teal:#1c8b83; --teal-dark:#12655f; --mint:#e8f5f1; --paper:#f7fbfa; }
        * { font-family:'DM Sans', sans-serif; }
        .stApp { background:var(--paper); color:var(--ink); }
        [data-testid='stSidebar'] { background:#113e43; border-right:0; }
        [data-testid='stSidebar'] > div:first-child { padding:2rem 1.2rem; }
        [data-testid='stSidebar'] * { color:#eaf7f3; }
        .brand { margin:0 0 2.8rem .35rem; }
        .brand-mark { display:inline-flex; align-items:center; justify-content:center; width:38px; height:38px; margin-bottom:1rem; border-radius:12px; background:#8ed8c2; color:#113e43; font-family:'Manrope', sans-serif; font-size:1.45rem; }
        .brand-name { font-family:'Manrope', sans-serif; font-size:1.55rem; font-weight:800; letter-spacing:-.04em; }
        .brand-caption { margin-top:.35rem; color:#9abbb7; font-size:.78rem; }
        .side-note { margin:3rem .35rem 0; padding-top:1rem; border-top:1px solid #316266; color:#9abbb7; font-size:.76rem; line-height:1.55; }
        .main .block-container { max-width:1240px; padding:3.5rem 4rem 4rem; }
        .eyebrow { color:var(--teal); font-size:.72rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; }
        h1,h2,h3 { font-family:'Manrope', sans-serif !important; color:var(--ink) !important; letter-spacing:-.045em; }
        h1 { font-size:clamp(2.3rem,4vw,4.1rem) !important; line-height:1.02 !important; margin:.4rem 0 .8rem !important; }
        .lede { max-width:600px; color:var(--muted); font-size:1.02rem; line-height:1.6; }
        .status-pill { display:inline-flex; align-items:center; gap:.45rem; padding:.5rem .75rem; border:1px solid var(--line); border-radius:999px; background:white; color:var(--muted); font-size:.78rem; }
        .status-dot { width:7px; height:7px; border-radius:50%; background:#43b987; }
        .intro-row { display:flex; justify-content:space-between; align-items:end; gap:2rem; margin-bottom:2.5rem; }
        .panel { padding:1.5rem; border:1px solid var(--line); border-radius:18px; background:white; }
        .panel-title { margin-bottom:1rem; color:var(--ink); font-family:'Manrope', sans-serif; font-size:1.05rem; font-weight:700; }
        .panel-copy { margin:-.55rem 0 1.2rem; color:var(--muted); font-size:.84rem; }
        label p { color:#52686b !important; font-size:.78rem !important; font-weight:600 !important; }
        input { border-color:var(--line) !important; border-radius:10px !important; background:#fbfdfd !important; }
        input:focus { border-color:var(--teal) !important; box-shadow:0 0 0 1px var(--teal) !important; }
        .stButton > button { width:100%; min-height:3.1rem; border:0; border-radius:11px; background:var(--teal); color:white; font-weight:700; }
        .stButton > button:hover { background:var(--teal-dark); color:white; }
        .result { display:flex; align-items:center; justify-content:space-between; gap:1rem; margin-top:1.5rem; padding:1.2rem 1.35rem; border-radius:14px; background:var(--mint); color:var(--teal-dark); }
        .result strong { display:block; margin-bottom:.25rem; font-family:'Manrope', sans-serif; font-size:1.02rem; }
        .result span { color:#52736e; font-size:.82rem; }
        .result-icon { display:grid; place-items:center; width:40px; height:40px; border-radius:50%; background:#c8eadf; font-weight:700; }
        .disclaimer { margin-top:2.2rem; color:#829295; font-size:.74rem; line-height:1.5; }
        @media (max-width:800px) { .main .block-container { padding:2rem 1.25rem 3rem; } .intro-row { display:block; } .status-pill { margin-top:1.2rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("<div class='brand'><div class='brand-mark'>+</div><div class='brand-name'>pulse</div><div class='brand-caption'>Personal health screening</div></div>", unsafe_allow_html=True)
    selected = option_menu(
        None,
        ["Diabetes", "Heart health", "Parkinson's"],
        icons=["activity", "heart", "person"],
        default_index=0,
        styles={
            "container": {"padding": "0", "background-color": "transparent"},
            "icon": {"color": "#8ed8c2", "font-size": "1rem"},
            "nav-link": {"font-size": "0.88rem", "margin": "0.25rem 0", "border-radius": "10px", "padding": "0.75rem 0.85rem"},
            "nav-link-selected": {"background-color": "#236b6b", "color": "#ffffff"},
        },
    )
    st.markdown("<div class='side-note'>Your entries stay in this session. Results are for screening only and are not a medical diagnosis.</div>", unsafe_allow_html=True)

page_details = {
    "Diabetes": ("Metabolic screening", "Diabetes risk", "Review common metabolic markers in a single, focused check."),
    "Heart health": ("Cardiovascular screening", "Heart health", "Explore the relationship between your heart metrics and risk indicators."),
    "Parkinson's": ("Voice feature screening", "Parkinson's screening", "Assess voice measurements used by the Parkinson's prediction model."),
}
eyebrow, title, description = page_details[selected]
st.markdown(f"<div class='intro-row'><div><div class='eyebrow'>{eyebrow}</div><h1>{title}</h1><div class='lede'>{description}</div></div><div class='status-pill'><span class='status-dot'></span> Models ready</div></div>", unsafe_allow_html=True)


def show_result(key):
    if st.session_state.get(key):
        st.markdown(f"<div class='result'><div><strong>{st.session_state[key]}</strong><span>Use this as a screening signal, then discuss your health with a qualified professional.</span></div><div class='result-icon'>OK</div></div>", unsafe_allow_html=True)


def number_field(label, key, minimum=None, maximum=None, step=0.1):
    uses_float = any(isinstance(value, float) for value in (minimum, maximum, step) if value is not None)
    if uses_float:
        minimum = float(minimum) if minimum is not None else None
        maximum = float(maximum) if maximum is not None else None
        step = float(step)
    else:
        minimum = int(minimum) if minimum is not None else None
        maximum = int(maximum) if maximum is not None else None
        step = int(step)
    return st.number_input(label, min_value=minimum, max_value=maximum, value=None, step=step, key=key, placeholder="Enter value")


if selected == "Diabetes":
    st.markdown("<div class='panel'><div class='panel-title'>Patient measurements</div><div class='panel-copy'>Enter the values from your latest health check.</div>", unsafe_allow_html=True)
    with st.form("diabetes_form"):
        columns = st.columns(3)
        with columns[0]:
            pregnancies = number_field("Pregnancies", "diab_pregnancies", 0, 20, 1)
            skin_thickness = number_field("Skin thickness (mm)", "diab_skin", 0, 100, 1)
            pedigree = number_field("Diabetes pedigree function", "diab_pedigree", 0.0, 3.0)
        with columns[1]:
            glucose = number_field("Glucose level (mg/dL)", "diab_glucose", 0, 300, 1)
            insulin = number_field("Insulin level (mu U/mL)", "diab_insulin", 0, 900, 1)
            age = number_field("Age", "diab_age", 1, 120, 1)
        with columns[2]:
            blood_pressure = number_field("Blood pressure (mmHg)", "diab_pressure", 0, 250, 1)
            bmi = number_field("BMI", "diab_bmi", 0.0, 80.0)
        submitted = st.form_submit_button("Run diabetes screening")
    st.markdown("</div>", unsafe_allow_html=True)
    if submitted:
        values = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]
        if any(value is None for value in values):
            st.warning("Complete every measurement before running the screening.")
        else:
            prediction = diabetes_model.predict([values])[0]
            st.session_state["diabetes_result"] = "The screening indicates elevated diabetes risk." if prediction == 1 else "The screening indicates lower diabetes risk."
    show_result("diabetes_result")

elif selected == "Heart health":
    st.markdown("<div class='panel'><div class='panel-title'>Cardiovascular measurements</div><div class='panel-copy'>Use values from a recent examination where possible.</div>", unsafe_allow_html=True)
    with st.form("heart_form"):
        columns = st.columns(3)
        with columns[0]:
            age = number_field("Age", "heart_age", 1, 120, 1)
            resting_bp = number_field("Resting blood pressure", "heart_bp", 0, 300, 1)
            resting_ecg = number_field("Resting ECG result", "heart_ecg", 0, 2, 1)
            oldpeak = number_field("ST depression", "heart_oldpeak", 0.0, 10.0)
            thal = number_field("Thalassemia result", "heart_thal", 0, 3, 1)
        with columns[1]:
            sex = number_field("Sex (0 or 1)", "heart_sex", 0, 1, 1)
            cholesterol = number_field("Serum cholesterol (mg/dL)", "heart_chol", 0, 700, 1)
            max_rate = number_field("Maximum heart rate", "heart_rate", 0, 300, 1)
            slope = number_field("Exercise ST slope", "heart_slope", 0, 2, 1)
        with columns[2]:
            chest_pain = number_field("Chest pain type", "heart_cp", 0, 3, 1)
            fasting_sugar = number_field("Fasting blood sugar (0 or 1)", "heart_fbs", 0, 1, 1)
            exercise_angina = number_field("Exercise-induced angina (0 or 1)", "heart_exang", 0, 1, 1)
            vessels = number_field("Major vessels (0 to 3)", "heart_ca", 0, 3, 1)
        submitted = st.form_submit_button("Run heart screening")
    st.markdown("</div>", unsafe_allow_html=True)
    if submitted:
        values = [age, sex, chest_pain, resting_bp, cholesterol, fasting_sugar, resting_ecg, max_rate, exercise_angina, oldpeak, slope, vessels, thal]
        if any(value is None for value in values):
            st.warning("Complete every measurement before running the screening.")
        else:
            prediction = heart_disease_model.predict([values])[0]
            st.session_state["heart_result"] = "The screening indicates elevated heart disease risk." if prediction == 1 else "The screening indicates lower heart disease risk."
    show_result("heart_result")

else:
    st.markdown("<div class='panel'><div class='panel-title'>Voice measurements</div><div class='panel-copy'>Enter the acoustic measurements produced by your voice analysis tool.</div>", unsafe_allow_html=True)
    labels = [
        ("MDVP:Fo (Hz)", "fo"), ("MDVP:Fhi (Hz)", "fhi"), ("MDVP:Flo (Hz)", "flo"), ("MDVP:Jitter (%)", "jitter_percent"), ("MDVP:Jitter (Abs)", "jitter_abs"),
        ("MDVP:RAP", "rap"), ("MDVP:PPQ", "ppq"), ("Jitter:DDP", "ddp"), ("MDVP:Shimmer", "shimmer"), ("MDVP:Shimmer (dB)", "shimmer_db"),
        ("Shimmer:APQ3", "apq3"), ("Shimmer:APQ5", "apq5"), ("MDVP:APQ", "apq"), ("Shimmer:DDA", "dda"), ("NHR", "nhr"),
        ("HNR", "hnr"), ("RPDE", "rpde"), ("DFA", "dfa"), ("spread1", "spread1"), ("spread2", "spread2"), ("D2", "d2"), ("PPE", "ppe"),
    ]
    with st.form("parkinsons_form"):
        columns = st.columns(4)
        voice_values = []
        for index, (label, key) in enumerate(labels):
            with columns[index % 4]:
                voice_values.append(number_field(label, f"voice_{key}", step=0.0001))
        submitted = st.form_submit_button("Run Parkinson's screening")
    st.markdown("</div>", unsafe_allow_html=True)
    if submitted:
        if any(value is None for value in voice_values):
            st.warning("Complete every measurement before running the screening.")
        else:
            prediction = parkinsons_model.predict([voice_values])[0]
            st.session_state["parkinsons_result"] = "The screening indicates Parkinson's disease risk." if prediction == 1 else "The screening indicates lower Parkinson's disease risk."
    show_result("parkinsons_result")

st.markdown("<div class='disclaimer'>Pulse is an educational screening interface. It does not replace professional medical advice, diagnosis, or treatment.</div>", unsafe_allow_html=True)
