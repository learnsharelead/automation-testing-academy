import streamlit as st
import os

st.set_page_config(layout="wide", page_title="WebdriverIO Expert Guide")

st.header("🤖 WebdriverIO: The Full-Stack Powerhouse")
st.markdown("### The 'Swiss Army Knife' of Automation")

# Introduction with Ecosystem Diagram
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("#### 🌐 The Protocol Agnostic Engine")
    st.info("""
    **The "Universal Remote" Analogy**
    
    If Playwright is a specialized high-speed racecar for modern web, **WebdriverIO (WDIO)** is a transforming Optimus Prime.
    
    It doesn't just speak one language. It can switch modes instantly:
    *   **WebDriver Protocol**: For cross-browser compatibility (IE11, Safari).
    *   **DevTools Protocol**: For speed and Chrome automation (Puppeteer mode).
    *   **Mobile Protocol**: For driving native Android/iOS apps via Appium.
    
    It is the *only* major JS framework that conquers **Web, Mobile, and Desktop** in one codebase.
    """)
with col2:
    c1, c2, c3 = st.columns([0.1, 2, 0.1])
    with c2:
        st.image("assets/wdio_ecosystem_1765635940013.png", caption="The Extensible WDIO Ecosystem")

tabs = st.tabs([
    "🧬 1. Architecture", 
    "🏗️ 2. Enterprise POM", 
    "📱 3. Mobile (Appium)", 
    "🔌 4. Service Layer",
    "🧠 5. Expert Selectors"
])

# ----------------------------------------------------------------------------
# TAB 1: ARCHITECTURE
# ----------------------------------------------------------------------------
with tabs[0]:
    st.subheader("Hybrid Automation Strategy")
    st.markdown("Most tools force you to choose: Speed (Puppeteer) or Compatibility (Selenium). **WDIO gives you both.**")
    

    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/wdio_protocol_architecture_1765635963941.png", caption="Dual-Protocol Architecture")
    
    st.markdown("### 🚦 How to Configure modes")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**1. Standard Mode (WebDriver)**")
        st.caption("Best for: True Cross-Browser Testing & Cloud Grids")
        st.code("""
// wdio.conf.js
capabilities: [{
    browserName: 'firefox', // Uses GeckoDriver
    browserVersion: 'latest'
}, {
    browserName: 'safari', // Uses SafariDriver
}]
        """, language="javascript")
        
    with c2:
        st.markdown("**2. Automation Protocol (DevTools)**")
        st.caption("Best for: Speed, Network Interception, Tracing")
        st.code("""
// wdio.conf.js
capabilities: [{
    browserName: 'chrome',
    'wdio:devtoolsOptions': {
        headless: true
    }
}],
automationProtocol: 'devtools' // 🚀 PUPPETEER MODE
        """, language="javascript")

# ----------------------------------------------------------------------------
# TAB 2: PAGE OBJECTS
# ----------------------------------------------------------------------------
with tabs[1]:
    st.subheader("🏗️ Scalable Page Object Model (POM)")
    
    st.markdown("""
    **The "Restaurant Kitchen" Analogy**
    *   **Test Script**: The Customer ordering food ("I want a Login").
    *   **Page Object**: The Chef who knows *how* to make it.
    *   **DOM**: The raw ingredients.
    
    The Customer (Test) shouldn't care if the Chef (Page Object) changes the recipe (Selector), as long as the Meal (Result) is the same.
    """)
    

    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/page_object_pattern_1765635989376.png", caption="Separation of Concerns Pattern")
    
    st.markdown("### 🧑‍🍳 Expert Pattern: Composable Components")
    st.markdown("Don't just make `Page` classes. Make `Component` classes for reusable widgets (Navbars, Modals).")
    
    st.code("""
// 1. BASE COMPONENT (The Reusable Widget)
class Component {
    constructor(selector) { this.root = selector; }
    
    get main() { return $(this.root); }
    async isVisible() { return await this.main.isDisplayed(); }
}

// 2. SEARCH BAR COMPONENT (Specific Logic)
class SearchBar extends Component {
    get input() { return this.main.$('input.search-term'); }
    get btn()   { return this.main.$('button.search-btn'); }
    
    async search(text) {
        await this.input.setValue(text);
        await this.btn.click();
    }
}

// 3. PAGE CLASS (Composing Components)
class HomePage {
    constructor() {
        // Reuse the component!
        this.navSearch = new SearchBar('header.global-nav');
        this.footerSearch = new SearchBar('footer.site-map');
    }
}
    """, language="javascript")

# ----------------------------------------------------------------------------
# TAB 3: MOBILE
# ----------------------------------------------------------------------------
with tabs[2]:
    st.subheader("📱 Native Mobile Automation (Appium)")
    st.warning("WebdriverIO is widely considered the **best usage** of Appium due to its async handling and tight integration.")
    

    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/appium_architecture_1765636011256.png", caption="One Codebase, Native Execution")
    
    st.markdown("### 🤖 Android vs 🍎 iOS Strategies")
    
    m1, m2 = st.columns(2)
    with m1:
        st.markdown("**Android (UiAutomator2)**")
        st.code("""
const btn = await $('android=new UiSelector().text("Login")');
await btn.click();
        """, language="javascript")
    with m2:
        st.markdown("**iOS (XCUITest)**")
        st.code("""
const btn = await $('~login_button_accessibility_id');
await btn.click();
        """, language="javascript")
        
    st.markdown("### 👆 Advanced Interactions (Gestures)")
    st.code("""
// Perform a vertical swipe (Scroll)
await driver.touchPerform([
    { action: 'press', options: { x: 500, y: 1500 }},
    { action: 'wait', options: { ms: 500 }},
    { action: 'moveTo', options: { x: 500, y: 500 }}, // Drag up
    { action: 'release' }
]);
    """, language="javascript")

# ----------------------------------------------------------------------------
# TAB 4: SERVICES
# ----------------------------------------------------------------------------
with tabs[3]:
    st.subheader("🔌 The Service Layer: Supercharging the Runner")
    st.markdown("WDIO services hook into the test lifecycle (before session, after test, on failure) to add magic capabilities.")
    
    service_exp = st.expander("📂 Popular Services Deep Dive", expanded=True)
    with service_exp:
        st.markdown("""
        | Service | Purpose | Magic Power ✨ |
        | :--- | :--- | :--- |
        | **Visual Service** | Visual Regression | `expect(browser).toMatchImageSnapshot()` |
        | **Google Lighthouse** | Performance Audit | `browser.checkPWA()` checks performance scores |
        | **Shared Store** | Parallel State | Share tokens between parallel workers |
        | **Intercept** | Network Mocking | Simpler wrapper over DevTools mocking |
        """)

    st.code("""
// wdio.conf.js - Using the Visual Regression Service
services: [
    ['visual', {
        autoSaveBaseline: true,
        blockOutStatusBar: true, // Ignore phone status bar
        blockOutToolBar: true
    }]
],
    """, language="javascript")

# ----------------------------------------------------------------------------
# TAB 5: SELECTORS
# ----------------------------------------------------------------------------
with tabs[4]:
    st.subheader("🧠 Expert Selector Strategies")
    
    st.markdown("#### ⚛️ React Selectors (Resq)")
    st.markdown("Stop fighting div soup. Select components by their **React Name**.")
    st.code("""
// Find the <ProductCard /> component where props.id === 55
const card = await browser.react$('ProductCard', {
    props: { id: 55 }
});
await card.click();
    """, language="javascript")
    
    st.markdown("#### ⛓️ Chained Selectors")
    st.code("""
// Find the 'Submit' button specifically inside the 'Login Form'
// Avoids clicking the 'Newsletter Submit' by mistake
const submitBtn = await $('.login-form').$('.btn-primary');
    """, language="javascript")
    
    st.markdown("#### 🌑 Shadow DOM Support")
    st.code("""
// Deep selector automatically pierces Shadow DOM boundaries
// No need for 'shadowRoot.querySelector' nightmare
const el = await $('>>>.deep-element-inside-shadow-root');
    """, language="javascript")
