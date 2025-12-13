import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Playwright Masterclass")

st.header("🎭 Playwright: The Modern Automation Standard")
st.markdown("### From Beginner to Industry Expert")

# Introduction Section with Architecture
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("#### 🏛️ The Architecture of Speed")
    st.info("""
    **The WebSocket Revolution**
    
    Imagine trying to have a conversation with someone in another room (Selenium/WebDriver) where you have to send a letter for every sentence and wait for a reply letter. That's HTTP polling.
    
    **Playwright** is like being in the *same room* talking over a direct phone line (WebSocket). 
    
    It communicates directly with the browser's engine (Chromium, WebKit, Firefox) via the **DevTools Protocol**, allowing for:
    - ⚡ **Bi-directional communication** (Events fire instantly)
    - 🚀 **Faster execution** (No HTTP overhead)
    - 🛡️ **Flakiness resistance** (It "knows" when the browser is busy)
    """)
with col2:
    # Centered and smaller image
    c1, c2, c3 = st.columns([0.2, 2, 0.2])
    with c2:
        st.image("assets/playwright_architecture_1765634867859.png", caption="Playwright's Direct-Communication Architecture")


tabs = st.tabs([
    "🧠 1. Smart Locators", 
    "⏳ 2. Auto-Waiting", 
    "🔄 3. End-to-End Workflow", 
    "🔐 4. Auth & State", 
    "🕸️ 5. Network Mocking", 
    "🏭 6. Industry Patterns"
])

# ----------------------------------------------------------------------------
# TAB 1: SMART LOCATORS
# ----------------------------------------------------------------------------
with tabs[0]:
    st.subheader("🔍 Locating Elements: The User Perspective")
    
    comp_col1, comp_col2 = st.columns([1, 1])
    
    with comp_col1:
        st.markdown("#### ❌ The Old Way (Implementation Details)")
        st.markdown("""
        Finding an element by CSS Class or ID is like **giving directions based on landmarks that change**.
        
        > *"Turn left at the blue house with the red fence."*
        
        **Why it fails**: If the house gets painted yellow (developer changes CSS), your test gets lost.
        """)
        
    with comp_col2:
        st.markdown("#### ✅ The Playwright Way (User-Facing)")
        st.markdown("""
        Finding an element by Role or Text is like **giving directions based on the destination's purpose**.
        
        > *"Go to the Library."*
        
        **Why it works**: Even if the library is renovated, it's still the "Library".
        """)
        
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/locator_comparison_1765634890442.png", caption="Fragile vs. Resilient Locators")

    st.markdown("### 🏆 Best Practices Code Comparison")
    c1, c2 = st.columns(2)
    with c1:
        st.error("🚫 BRITTLE (Selenium/Cypress Style)")
        st.code("""
# Breaks if class changes
page.locator("div.btn-primary").click()

# Breaks if DOM structure changes
page.locator("//div[3]/span[2]/input").fill("data")
        """, language="python")
    with c2:
        st.success("✅ ROBUST (Playwright Style)")
        st.code("""
# Resilience: Finds the 'Submit' button regardless of class
page.get_by_role("button", name="Submit").click()

# Resilience: Finds label associated with input
page.get_by_label("User Email").fill("test@example.com")
        """, language="python")


# ----------------------------------------------------------------------------
# TAB 2: AUTO-WAITING
# ----------------------------------------------------------------------------
with tabs[1]:
    st.subheader("⏳ The 'Polite' Automation Engine")
    
    st.markdown("""
    **The "Polite Conversation" Analogy**
    
    *   **Selenium/Old Tools**: Like a person who shouts a question and immediately expects an answer, getting angry (Exception) if you haven't processed it yet.
    *   **Playwright**: Like a polite conversation partner. It asks a question and **waits patiently** (Auto-Wait) for you to finish thinking (Loading) and look at them (Visibility) before expecting a response.
    """)
    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/auto_wait_mechanism_1765634911762.png", caption="Playwright's Actionability Checks")
    
    st.markdown("### 📝 What does it check?")
    st.info("Before performing a `click()`, Playwright ensures ALL these are true:")
    st.markdown("""
    1.  👁️ **Attached**: Element is in the specific DOM.
    2.  🪜 **Visible**: Not `display: none` or `visibility: hidden`.
    3.  🛑 **Stable**: Element is not animating or moving.
    4.  👂 **Receives Events**: Not covered by another element (like a modal backdrop).
    5.  🖱️ **Enabled**: Not `disabled`.
    """)


# ----------------------------------------------------------------------------
# TAB 3: END-TO-END WORKFLOW
# ----------------------------------------------------------------------------
with tabs[2]:
    st.subheader("🔄 Unified API & UI Testing")
    st.markdown("Stop treating API and UI tests as separate silos. Playwright integrates them for **hybrid testing**.")
    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/api_ui_workflow_1765634942790.png", caption="Hybrid Testing Workflow")
    
    st.markdown("#### ⚡ The 'Shortcut' Pattern Example")
    st.code("""
def test_new_user_dashboard(page):
    # 🚀 FAST: Create data via API (Milliseconds)
    user_data = page.request.post("/api/v1/users/create", data={"name": "Alice"}).json()
    
    # 🐢 UI: Login and Check Visuals (Seconds)
    page.goto(f"/dashboard/{user_data['id']}")
    
    # Assert
    expect(page.get_by_role("heading", name="Alice")).to_be_visible()
    """, language="python")


# ----------------------------------------------------------------------------
# TAB 4: AUTH & STATE
# ----------------------------------------------------------------------------
with tabs[3]:
    st.subheader("🔐 Global Authentication Pattern")
    st.markdown("### Write Once, Log In Everywhere")
    
    st.markdown("""
    **The "Season Pass" Analogy**
    
    Imagine going to a theme park.
    *   **Standard approach**: You buy a ticket at the booth **every single time** you want to ride a coaster. (Logging in before every test).
    *   **Global Auth**: You buy a **Season Pass** (Storage State) once. You just flash your pass to get on any ride instantly.
    """)
    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/global_auth_pattern_1765634968972.png", caption="Global Setup Architecture")
    
    st.code("""
# 1. DEFINE GLOBAL SETUP (The "Season Pass Office")
# global_setup.py
def global_setup():
    page.goto("https://app.com/login")
    page.fill("#user", "admin")
    page.fill("#pass", "1234")
    page.click("#login")
    page.context.storage_state(path="auth.json") # 💾 SAVE THE PASS

# 2. CONFIGURE PROJECT
# pytest.ini
[pytest]
addopts = --storage-state=auth.json

# 3. ENJOY FAST TESTS
# test_admin.py - Already logged in!
def test_admin_panel(page):
    page.goto("/admin") # ⚡ Instant access
    """, language="python")


# ----------------------------------------------------------------------------
# TAB 5: NETWORK MOCKING
# ----------------------------------------------------------------------------
with tabs[4]:
    st.subheader("🕸️ Network Interception: The 'Movie Set' Strategy")
    
    st.markdown("""
    **The "Movie Set" Analogy**
    
    When filming a movie scene inside a house, Hollywood doesn't buy a real house. They build a **facade** (Mock).
    It looks real to the camera (the UI), but behind the door, there's nothing.
    
    *   **Why?** It's cheaper, faster, and you control the weather (Network Errors).
    """)
    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/network_interception_1765634991293.png", caption="Intercepting & Mocking API Calls")
    
    st.markdown("### 🧪 Scenario: Testing a Server Crash")
    st.markdown("How do you test your UI handles a 500 Error without actually breaking the server? **Mock it.**")
    
    st.code("""
def test_handling_server_crash(page):
    # 🎭 ACTING: Pretend the server is on fire
    page.route("**/api/payments", lambda route: route.fulfill(
        status=500,
        body="Internal Server Error"
    ))
    
    page.goto("/checkout")
    page.get_by_role("button", name="Pay Now").click()
    
    # 🕵️ CHECK: Does the UI show a nice error message?
    expect(page.get_by_text("Something went wrong. Please try again.")).to_be_visible()
    """, language="python")


# ----------------------------------------------------------------------------
# TAB 6: INDUSTRY PATTERNS
# ----------------------------------------------------------------------------
with tabs[5]:
    st.subheader("🏭 Real-World Application Architectures")
    
    st.markdown("### 🛍️ Modern E-Commerce Testing Flow")
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/ecommerce_workflow_1765635016791.png", caption="Complex E-Commerce Verification Flow")
    
    st.markdown("#### 🔑 Key Industry Considerations")
    
    ic1, ic2, ic3 = st.columns(3)
    with ic1:
        st.markdown("**1. Visual Regression**")
        st.caption("Pixel-perfect validation")
        st.code('expect(page).to_have_screenshot()')
    with ic2:
        st.markdown("**2. Traceability**")
        st.caption("Debug failures in CI")
        st.code('trace.zip (contains snapshots)')
    with ic3:
        st.markdown("**3. Accessibility**")
        st.caption("Legal compliance")
        st.code('axe.run(page)')

    st.markdown("### 🩺 Healthcare/Fintech: Handling Sensitivity")
    st.warning("**PII/PHI Data Rules**: Never use real patient/customer data in automation. Use **Synthetic Data Factories**.")
    
    st.code("""
from faker import Faker
fake = Faker()

def test_patient_registration(page):
    # 🏭 Generate fake, valid data on the fly
    fake_name = fake.name()
    fake_email = fake.email()
    
    page.get_by_label("Full Name").fill(fake_name)
    page.get_by_label("Email").fill(fake_email)
    page.click("text=Register")
    
    expect(page.get_by_text(f"Welcome, {fake_name}")).to_be_visible()
    """, language="python")
