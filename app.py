import streamlit as st
import os
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from google import genai
from google.genai.errors import APIError

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Python AI Showcase",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PREMIUM LOOK & FEEL ---
st.markdown("""
<style>
    /* Custom Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Elegant Title Gradient */
    .title-text {
        font-weight: 800;
        font-size: 3rem;
        background: linear-gradient(135deg, #FF4B4B, #FF8F00, #9E00FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    
    /* Custom Card Style */
    .custom-card {
        background-color: #1e1e2f;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #2e2e4f;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Light/Dark mode adaptability for card headers */
    .card-title {
        color: #FF8F00;
        font-weight: 600;
        font-size: 1.4rem;
        margin-bottom: 10px;
    }
    
    /* Highlight badge style */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        background-color: #2e2e4f;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #00e5ff;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://www.python.org/static/community_logos/python-logo-only.png", width=60)
    st.markdown("### **AI Showcase Navigation**")
    page = st.radio("Go to:", ["🏠 Welcome Home", "🌸 Classical Machine Learning", "🤖 Generative AI Playground"])
    
    st.markdown("---")
    st.markdown("### **Technologies Used**")
    st.markdown("- **Streamlit**: Web Framework")
    st.markdown("- **google-genai**: Gemini API SDK")
    st.markdown("- **scikit-learn**: Classical ML")
    st.markdown("- **pandas / numpy**: Data Science")

# --- DATASETS / CACHING FOR SPEED ---
@st.cache_resource
def get_trained_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, iris

# --- PAGE 1: WELCOME HOME ---
if page == "🏠 Welcome Home":
    st.markdown('<div class="title-text">Python AI Showcase</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Explore the power of Python for Artificial Intelligence and Machine Learning in one interactive dashboard.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class="custom-card">
                <div class="card-title">🌸 Classical Machine Learning</div>
                <p>Train models, visualize datasets, and predict labels interactively using Scikit-Learn.</p>
                <span class="badge">Supervised Learning</span>
                <span class="badge">Random Forest</span>
                <span class="badge">Scikit-Learn</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.info("👈 Select **Classical Machine Learning** in the sidebar to try custom classifications.")
        
    with col2:
        st.markdown(
            """
            <div class="custom-card">
                <div class="card-title">🤖 Generative AI (LLMs)</div>
                <p>Connect with Google's Gemini models using the new <code>google-genai</code> SDK to generate text, brainstorm, or write code.</p>
                <span class="badge">Gemini-2.5-Flash</span>
                <span class="badge">Generative AI</span>
                <span class="badge">SDK Integration</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.info("👈 Select **Generative AI Playground** in the sidebar to talk with Gemini.")

# --- PAGE 2: CLASSICAL MACHINE LEARNING ---
elif page == "🌸 Classical Machine Learning":
    st.markdown('<div class="title-text">Iris Flower Classifier</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Tune flower measurements to predict the species using a Random Forest Classifier trained on the classic Iris dataset.</div>', unsafe_allow_html=True)
    
    # Load model and dataset
    model, iris = get_trained_model()
    
    # Layout splits
    col_input, col_pred = st.columns([1, 1.2])
    
    with col_input:
        st.subheader("🛠️ Flower Feature Inputs")
        
        # User interactive sliders
        sepal_length = st.slider("Sepal Length (cm)", 
                                 float(iris.data[:, 0].min()), float(iris.data[:, 0].max()), float(iris.data[:, 0].mean()))
        sepal_width  = st.slider("Sepal Width (cm)", 
                                 float(iris.data[:, 1].min()), float(iris.data[:, 1].max()), float(iris.data[:, 1].mean()))
        petal_length = st.slider("Petal Length (cm)", 
                                 float(iris.data[:, 2].min()), float(iris.data[:, 2].max()), float(iris.data[:, 2].mean()))
        petal_width  = st.slider("Petal Width (cm)", 
                                 float(iris.data[:, 3].min()), float(iris.data[:, 3].max()), float(iris.data[:, 3].mean()))
        
        user_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    with col_pred:
        st.subheader("🎯 Model Prediction")
        
        # Prediction
        prediction_idx = model.predict(user_features)[0]
        prediction_prob = model.predict_proba(user_features)[0]
        predicted_species = iris.target_names[prediction_idx].capitalize()
        
        # Determine emoji representation
        species_emoji = {
            "Setosa": "🌸",
            "Versicolor": "🌺",
            "Virginica": "🌷"
        }.get(predicted_species, "🌼")
        
        # Display Prediction Card
        st.markdown(
            f"""
            <div class="custom-card">
                <div class="card-title">Predicted Species</div>
                <h1 style='color: #00e5ff; font-size: 3rem; margin: 0;'>{species_emoji} {predicted_species}</h1>
                <p style='color: #7f8c8d; font-size: 0.95rem; margin-top: 10px;'>
                    Confidence Score: <b>{prediction_prob[prediction_idx]:.2%}</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Confidence breakdown
        st.markdown("### Confidence Distribution")
        prob_df = pd.DataFrame({
            'Species': [name.capitalize() for name in iris.target_names],
            'Probability': prediction_prob
        })
        st.bar_chart(prob_df.set_index('Species'), height=180)

# --- PAGE 3: GENERATIVE AI PLAYGROUND ---
elif page == "🤖 Generative AI Playground":
    st.markdown('<div class="title-text">Gemini Playground</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Experience state-of-the-art multi-modal capabilities powered by the Google GenAI SDK.</div>', unsafe_allow_html=True)
    
    # Retrieve API key from environment variable
    env_api_key = os.environ.get("GEMINI_API_KEY", "")
    
    st.markdown("### 🔑 API Authentication")
    
    if env_api_key:
        st.success("Detected `GEMINI_API_KEY` environment variable! App is ready to roll.")
        api_key = env_api_key
    else:
        api_key = st.text_input("Enter your Gemini API Key:", type="password", 
                               help="Get an API key from Google AI Studio. Your key is not saved anywhere outside this session.")
        
    st.markdown("---")
    
    st.markdown("### 💬 Chat/Prompt Gemini")
    prompt = st.text_area("What would you like to ask or generate?", 
                          value="Write a Python function to check if a number is prime.", 
                          height=100)
    
    generate_btn = st.button("✨ Generate Content", type="primary")
    
    if generate_btn:
        if not api_key:
            st.error("Please enter a Gemini API Key or set the `GEMINI_API_KEY` environment variable first!")
        else:
            with st.spinner("Talking to Gemini..."):
                try:
                    # Initialize the new SDK client with the provided API key
                    client = genai.Client(api_key=api_key)
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    
                    st.markdown("### 📄 Response")
                    st.markdown(response.text)
                    
                except APIError as e:
                    st.error(f"Gemini API Error: {e.message}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")
