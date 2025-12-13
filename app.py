import streamlit as st
from utils.layout import render_header, render_navigation, render_footer
from utils.styles import apply_apple_style_css
from utils.seo_manager import setup_seo_routing, inject_seo_meta

# Page Config
st.set_page_config(
    page_title="Automation Testing Academy",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style & Routing
apply_apple_style_css()
nav_options = ["Home", "Playwright", "WebdriverIO", "Karate", "Comparisons"]
setup_seo_routing(nav_options, "Home")

# Layout
render_header()
selected_nav = render_navigation()
inject_seo_meta(selected_nav)

# Routing Logic
if selected_nav == "Home":
    st.markdown("""
    ## Welcome to the Future of Automation 🚀
    
    Traditional automation is evolving. From flaky Selenium scripts to self-healing, fast, and reliable frameworks.
    This academy is dedicated to the **Modern Big Three**:
    
    ### 🎭 Playwright
    The speed demon from Microsoft. Native auto-waiting, browser context isolation, and powerful tracing.
    
    ### 🤖 WebdriverIO
    The versatile nodejs powerhouse. Deep integration with mobile (Appium), frontend frameworks, and cloud providers.
    
    ### 🥋 Karate DSL
    The unified platform. API, UI, and Performance testing combined in a simple Gherkin-like syntax.
    
    ---
    
    ### 📚 Curriculum
    Select a module from the navigation bar above to start mastering these tools.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Playwright**\n\nLatest v1.40+\nPython & Node.js Support")
    with col2:
        st.success("**WebdriverIO**\n\nAsync/Sync Mode\nAppium Mobile Support")
    with col3:
        st.warning("**Karate**\n\nAPI + UI + Perf\nZero Coding Required")

elif selected_nav == "Playwright":
    # Dynamic import to keep app.py clean, assumes we will create this file
    exec(open("pages/1_Playwright.py", encoding="utf-8").read())

elif selected_nav == "WebdriverIO":
    exec(open("pages/2_WebdriverIO.py", encoding="utf-8").read())

elif selected_nav == "Karate":
    exec(open("pages/3_Karate.py", encoding="utf-8").read())

elif selected_nav == "Comparisons":
    exec(open("pages/4_Comparisons.py", encoding="utf-8").read())

render_footer()
