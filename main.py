import streamlit as st


def main():
    st.set_page_config(
        page_title="Test Title",
        layout="wide",
        page_icon="🕒")

    pages = [st.Page("Test.py", title="Test")]
    pg = st.navigation(pages)
    pg.run()


if __name__ == '__main__':
    main()
