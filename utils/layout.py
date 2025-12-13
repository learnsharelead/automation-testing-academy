import streamlit as st
from streamlit_option_menu import option_menu

def render_header():
    """Renders the application header."""
    st.markdown("""
    <div style="
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    ">
        <div style="
            background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: white;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
            margin-right: 16px;
        ">
            🚀
        </div>
        <div>
            <h1 style="margin: 0; font-size: 24px; color: #1e293b;">Automation Testing Academy</h1>
            <p style="margin: 0; font-size: 14px; color: #64748b;">Master the Modern Testing Stack</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_navigation():
    nav_options = ["Home", "Playwright", "WebdriverIO", "Karate", "Comparisons"]
    icons = ["house", "play-circle", "robot", "lightning", "bar-chart"]
    
    default_index = 0
    if "nav_selection" in st.session_state:
        try:
            default_index = nav_options.index(st.session_state.nav_selection)
        except ValueError:
            default_index = 0
            
    selected = option_menu(
        menu_title=None,
        options=nav_options,
        icons=icons,
        default_index=default_index,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "8px", 
                "background-color": "#ffffff", 
                "border-radius": "16px",
                "box-shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)",
                "border": "1px solid rgba(0,0,0,0.05)"
            },
            "icon": {"color": "#64748b", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0px 6px",
                "--hover-color": "#eff6ff",
                "border-radius": "10px",
                "padding": "10px 20px",
                "font-weight": "500",
                "color": "#64748b"
            },
            "nav-link-selected": {
                "background-color": "#2563eb",
                "color": "white",
                "font-weight": "600",
                "box-shadow": "0 4px 12px rgba(37, 99, 235, 0.3)"
            },
        }
    )
    st.session_state.nav_selection = selected
    st.markdown("<br>", unsafe_allow_html=True)
    return selected

def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #999; font-size: 12px;'>
            <p>Built with ❤️ for Automation Engineers | © 2025 Automation Academy</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
