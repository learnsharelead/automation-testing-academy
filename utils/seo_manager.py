import streamlit as st
import json

# =============================================================================
# SEO CONFIGURATION
# =============================================================================
SEO_METADATA = {
    "Home": {
        "title": "Automation Testing Academy | Playwright, WebdriverIO, Karate",
        "description": "Master modern test automation with Playwright, WebdriverIO, and Karate. Code examples, best practices, and architecture guides.",
        "keywords": "automation testing, playwright tutorial, webdriverio guide, karate dsl, api testing, ui automation"
    },
    "Playwright": {
        "title": "Playwright Mastery | Fast, Reliable E2E Testing",
        "description": "Deep dive into Microsoft Playwright. Learn locators, auto-waiting, network interception, and browser contexts in Python and Node.js.",
        "keywords": "playwright python tutorial, playwright vs selenium, playwright locators, end to end testing"
    },
    "WebdriverIO": {
        "title": "WebdriverIO Guide | Next-Gen WebDriver Automation",
        "description": "Learn WebdriverIO for scalable test automation. Synchronous vs Asynchronous modes, Page Object Model, and custom services.",
        "keywords": "webdriverio tutorial, webdriverio vs cypress, wdio page object model, javascript automation"
    },
    "Karate": {
        "title": "Karate DSL Tutorial | API & Performance Testing",
        "description": "Unified API and UI testing with Karate. Write tests in simple Gherkin syntax without Java/Python code.",
        "keywords": "karate framework tutorial, api testing tool, karate dsl, bdd testing, karate vs rest assured"
    },
    "Comparisons": {
        "title": "Automation Tool Comparison | Choose the Right Framework",
        "description": "Detailed comparison of Playwright vs WebdriverIO vs Cypress vs Selenium. Benchmarks, feature matrices, and selection guides.",
        "keywords": "automation tool comparison, playwright vs webdriverio, best automation framework 2025"
    }
}

def setup_seo_routing(nav_options, default_selection):
    try:
        query_params = st.query_params
        url_nav = query_params.get("nav", None)
    except:
        url_nav = None
    
    if url_nav in nav_options:
        if "nav_selection" not in st.session_state:
            st.session_state.nav_selection = url_nav
        return url_nav
    else:
        if "nav_selection" not in st.session_state:
            st.session_state.nav_selection = default_selection
        return st.session_state.nav_selection

def inject_seo_meta(selection):
    meta = SEO_METADATA.get(selection, SEO_METADATA["Home"])
    try:
        st.query_params["nav"] = selection
    except:
        pass
        
    st.markdown(f"""
    <div style="display:none;">
        <h1>{meta['title']}</h1>
        <p>{meta['description']}</p>
    </div>
    """, unsafe_allow_html=True)
