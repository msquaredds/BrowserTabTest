import streamlit as st



def main():
    st.set_page_config(
        page_title="Test Title",
        layout="wide",
        page_icon="🕒")

    # st.markdown(
    #     """
    #     <style>
    #         section[data-testid="stSidebar"] {
    #             width: 400px !important;
    #         }
    #     </style>
    #     """,
    #     unsafe_allow_html=True)

    # col_title = st.columns(3)
    # with col_title[1]:
    #     st.image("Sharp_Shares_Title_Logo_Subtitle_06_27_2025.png")

    pages = [st.Page("Test.py", title="Test")]
    pg = st.navigation(pages)
    pg.run()


if __name__ == '__main__':
    main()
