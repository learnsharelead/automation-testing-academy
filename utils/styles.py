import streamlit as st

def apply_apple_style_css():
    """
    Applies the Apple-inspired CSS system to the Streamlit app.
    MATCHING: Performance Testing Academy Theme
    """
    st.markdown("""
<style>
    /* ==========================================================================
       RESET & BASICS
       ========================================================================== */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
    }

    /* Remove Streamlit Bloat */
    #MainMenu, footer, header {visibility: hidden; height: 0;}
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none;}
    .stDeployButton {display: none;}

    /* App Background - Apple System Gray */
    .stApp {
        background-color: #f5f5f7 !important;
    }

    /* ==========================================================================
       LAYOUT & WHITESPACE
       ========================================================================== */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }

    /* ==========================================================================
       TYPOGRAPHY - Apple Style
       ========================================================================== */
    h1 {
        font-family: -apple-system, sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        letter-spacing: -0.01em !important;
        color: #1d1d1f !important;
        margin-bottom: 0.5rem !important;
    }

    h2, h3 {
        color: #1d1d1f !important;
        margin-top: 1rem !important;
        margin-bottom: 0.5rem !important;
    }

    h2 { font-size: 1.4rem !important; }
    h3 { font-size: 1.1rem !important; }

    p, li, label, .stMarkdown {
        font-size: 15px !important;
        line-height: 1.6 !important;
        color: #3b3b3b !important;
    }

    /* ==========================================================================
       VIBRANT PILL TABS
       ========================================================================== */
    .stTabs {
        margin-top: 20px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        padding: 6px;
        border-radius: 12px;
        border-bottom: none !important;
        margin-bottom: 1rem;
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .stTabs [data-baseweb="tab"] {
        height: 40px;
        padding: 0 20px;
        border-radius: 8px;
        border: none !important;
        background-color: transparent !important;
        color: #6e6e73;
        font-weight: 500;
        font-size: 14px;
        flex-grow: 1;
        max-width: 200px;
    }

    /* LEVEL 1: MAIN TABS (Blue) */
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%) !important;
        color: #0d47a1 !important;
        box-shadow: 0 2px 6px rgba(13, 71, 161, 0.15);
    }

    /* ==========================================================================
       CARDS & SURFACES
       ========================================================================== */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid rgba(0,0,0,0.05);
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        padding: 20px;
    }
    
    .stCodeBlock {
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    button { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)
