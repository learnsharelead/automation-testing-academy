import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Karate Expert Guide")

st.header("🥋 Karate: The Unified Test Platform")
st.markdown("### API, UI, Mocks, and Performance - In One Language")

# Introduction section with Architecture
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("#### 🎯 The \"One Tool\" Philosophy")
    st.info("""
    **The "Swiss Army Knife" Analogy**
    
    Most teams have a fragmented stack:
    *   **Postman/RestAssured** for API
    *   **Selenium/Playwright** for UI
    *   **Gatling/JMeter** for Performance
    *   **WireMock** for Mocks
    
    **Karate** is the only framework where you write **ONE script** (Feature file) and can run it as an API test, a Performance test, or a UI test.
    """)
with col2:
    c1, c2, c3 = st.columns([0.2, 2, 0.2])
    with c2:
        st.image("assets/karate_unified_architecture_1765636269592.png", caption="Unified Automaton Platform")

tabs = st.tabs([
    "📜 1. Gherkin++", 
    "⚡ 2. JSON Power", 
    "🚀 3. Performance Reuse", 
    "🎭 4. Total Mocking",
    "🖥️ 5. Hybrid UI"
])

# ----------------------------------------------------------------------------
# TAB 1: SYNTAX
# ----------------------------------------------------------------------------
with tabs[0]:
    st.subheader("Gherkin on Steroids")
    st.markdown("Karate doesn't require Java/Python 'Step Definitions'. The Gherkin **IS** the code.")
    
    st.code("""
Feature: User Management API

    Background:
        * url 'https://jsonplaceholder.typicode.com'
        * def authToken = 'Bearer 12345'
        * configure headers = { Authorization: '#(authToken)' }

    Scenario: Create and Fetch User
        # 1. CREATE
        Given path 'users'
        And request { name: 'John Wick', job: 'Assassin' }
        When method post
        Then status 201
        And def userId = response.id

        # 2. FETCH (Chaining variables)
        Given path 'users', userId
        When method get
        Then status 200
        And match response contains { name: 'John Wick' }
    """, language="gherkin")

# ----------------------------------------------------------------------------
# TAB 2: API
# ----------------------------------------------------------------------------
with tabs[1]:
    st.subheader("⚡ Advanced Fuzzy Matching")
    
    st.markdown("""
    **The "Shape Sorter" Analogy**
    
    Validating exact values is brittle (IDs change).
    Karate validates the **SHAPE** of the data. 
    *   "I don't care what the ID is, as long as it's a number."
    *   "I don't care what the email is, as long as it looks like an email."
    """)
    

    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/karate_fuzzy_matching_1765636302212.png", caption="Fuzzy Matching Visualization")
    
    st.markdown("### 🧬 Expert Validation Patterns")
    st.code("""
Scenario: Validate Complex Dynamic Response
    * def userSchema = 
    \"\"\"
    {
        id: '#number',              # Type validation
        uuid: '#uuid',              # UUID format check
        email: '#regex ^[a-z]+@.*', # Regex pattern
        tags: '#[] #string',        # Array of Strings
        address: {                  # Nested Object
            city: '#string',
            zip: '#? _ > 0'         # Self-validation check (Groovy) -- Zip must be positive
        },
        metadata: '#ignore'         # Ignore dynamic fields
    }
    \"\"\"
    
    Given path 'users/1'
    When method get
    Then match response == userSchema
    """, language="gherkin")

# ----------------------------------------------------------------------------
# TAB 3: PERFORMANCE
# ----------------------------------------------------------------------------
with tabs[2]:
    st.subheader("🚀 Reuse Functional Tests as Load Tests")
    st.warning("Stop rewriting API tests in JMeter! Karate integrates natively with **Gatling**.")
    

    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/gatling_performance_integration_1765636322718.png", caption="Zero-Code Refactoring Workflow")
    
    st.markdown("#### Scala Simulation Wrapper")
    st.code("""
// PerformanceTest.scala
class PerformanceTest extends Simulation {

  // 1. REUSE the Feature File
  val protocol = karateProtocol(
    "/users/{id}" -> Nil, // Handle URL patterns
  )
  
  val createUsers = scenario("Create Users")
    .exec(karateFeature("classpath:create-user.feature")) // <--- MAGIC
    
  // 2. DEFINE LOAD PROFILE
  setUp(
    createUsers.inject(
        rampUsers(100) during (5 seconds),
        constantUsersPerSec(50) during (10 seconds)
    ).protocols(protocol)
  )
}
    """, language="scala")

# ----------------------------------------------------------------------------
# TAB 4: MOCKS
# ----------------------------------------------------------------------------
with tabs[3]:
    st.subheader("🎭 Service Virtualization (Mocks)")
    
    st.markdown("""
    **The "Stunt Double" Analogy**
    
    If the real backend is the generic "Lead Actor" who is expensive and often unavailable, Karate Mocks are the "Stunt Double".
    They look the same, act the same, but are always available and do exactly what you tell them (even crash on command).
    """)
    

    
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image("assets/mock_server_flow_1765636342641.png", caption="Mocking Architecture")
    
    st.markdown("### 💻 Standalone Mock Server")
    st.code("""
Feature: Payment Service Mock

    Background:
        * def paymentId = 0

    Scenario: pathMatches('/pay') && methodIs('post')
        * def req = request
        * def response = { success: true, txnId: '#(paymentId + 1)' }
        * def responseDelay = 500 // Simulate 500ms network lag
        * def responseStatus = 200

    Scenario: pathMatches('/pay') && bodyPath('$.amount') < 0
        * def response = { error: 'Invalid Amount' }
        * def responseStatus = 400
    """, language="gherkin")

# ----------------------------------------------------------------------------
# TAB 5: UI
# ----------------------------------------------------------------------------
with tabs[4]:
    st.subheader("🖥️ Hybrid UI + API Automation")
    st.markdown("Use API calls to set up data, then drive the browser. **Faster than pure UI testing.**")
    
    st.code("""
Scenario: Order History Check
    # 1. API: Create Order (Backend)
    * url 'https://api.shop.com'
    * path 'orders'
    * request { item: 'Laptop', price: 1000 }
    * method post
    * def orderId = response.id

    # 2. UI: Verify in Fractal
    * configure driver = { type: 'chrome' }
    Given driver 'https://shop.com/login'
    And input('#user', 'admin')
    And click('#login')
    
    # 3. Validation
    And waitForUrl('/dashboard')
    Then match text('.order-list') contains orderId
    """, language="gherkin")
