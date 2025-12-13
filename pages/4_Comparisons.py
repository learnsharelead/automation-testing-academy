import streamlit as st

st.header("⚡ Playwright vs WebdriverIO vs Karate vs Selenium")

st.markdown("""
The "Best" tool depends entirely on your team's skillset and your project requirements.
""")

# ----------------------------------------------------------------------------
# MATRIX
# ----------------------------------------------------------------------------
st.subheader("Feature Comparison Matrix")

cols = st.columns(5)
cols[0].markdown("**Feature**")
cols[1].markdown("**Playwright**")
cols[2].markdown("**WebdriverIO**")
cols[3].markdown("**Karate**")
cols[4].markdown("**Selenium**")

# Row 1
cols = st.columns(5)
cols[0].markdown("Primary Language")
cols[1].markdown("TS/JS, Python")
cols[2].markdown("JS/Node.js")
cols[3].markdown("Gherkin (DSL)")
cols[4].markdown("Java, Python, C#")

# Row 2
cols = st.columns(5)
cols[0].markdown("Architecture")
cols[1].markdown("WebSocket (DevTools)")
cols[2].markdown("WebDriver + DevTools")
cols[3].markdown("HTTP + DevTools")
cols[4].markdown("WebDriver (HTTP)")

# Row 3
cols = st.columns(5)
cols[0].markdown("Speed/Stability")
cols[1].markdown("⭐⭐⭐⭐⭐ (Highest)")
cols[2].markdown("⭐⭐⭐⭐")
cols[3].markdown("⭐⭐⭐")
cols[4].markdown("⭐⭐ (Flaky)")

# Row 4
cols = st.columns(5)
cols[0].markdown("Mobile Support")
cols[1].markdown("Exper. (Emulation)")
cols[2].markdown("⭐⭐⭐⭐⭐ (Appium)")
cols[3].markdown("No")
cols[4].markdown("Via Appium")

# Row 5
cols = st.columns(5)
cols[0].markdown("API Testing")
cols[1].markdown("Native (Good)")
cols[2].markdown("Possible (Axios)")
cols[3].markdown("⭐⭐⭐⭐⭐ (Best)")
cols[4].markdown("No (Need RestAssured)")


# ----------------------------------------------------------------------------
# SCENARIOS
# ----------------------------------------------------------------------------
st.markdown("---")
st.subheader("Which one should you choose?")

s1, s2 = st.columns(2)

with s1:
    st.success("✅ **Choose Playwright if:**")
    st.markdown("""
    - You want the **fastest execution** and most stable tests.
    - Your team knows Python or Typescript.
    - You primarily test **Web Applications**.
    - You need to debug network traffic or mock API responses easily.
    """)

with s2:
    st.info("✅ **Choose WebdriverIO if:**")
    st.markdown("""
    - You need **Mobile (iOS/Android)** and Web testing in one framework.
    - Your project uses **JavaScript/Node.js**.
    - You need integration with many cloud providers (Sauce, BrowserStack).
    """)

s3, s4 = st.columns(2)

with s3:
    st.warning("✅ **Choose Karate if:**")
    st.markdown("""
    - You focus heavily on **API Testing**.
    - Your team includes **non-coders** (Manual QAs, BAs).
    - You want a unified tool for API + UI + Performance.
    """)
    
with s4:
    st.error("✅ **Choose Selenium if:**")
    st.markdown("""
    - You are maintaining a legacy Java project.
    - You have strict enterprise requirements for W3C standard compliance.
    - You need to test on very old browsers (IE11).
    """)
