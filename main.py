from pyasn1_modules.rfc5652 import id_contentType

import streamlit as st


def main():
    st.set_page_config(
        page_title="Test Title",
        layout="wide",
        page_icon="Sharp_Shares_Page_Icon_06_27_2025.png")

    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 400px !important;
            }
        </style>
        """,
        unsafe_allow_html=True)

    col_title = st.columns(3)
    with col_title[1]:
        st.image("Sharp_Shares_Title_Logo_Subtitle_06_27_2025.png")

    pages = [st.Page("Home.py",
                     title="Home",
                     icon="🏠"),
             st.Page("Test.py",
                     title="Test",
                     icon="🕒")]
    pg = st.navigation(pages)
    pg.run()


if __name__ == '__main__':
    main()
