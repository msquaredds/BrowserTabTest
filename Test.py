import time

import streamlit as st


def _sleep_and_show_spinner():
    time.sleep(3)
    with st.spinner():
        time.sleep(3)


def main():
    st.title("Spinner Test Page")

    # THIS KEEPS THE TAB TITLE / IMAGE
    # with st.spinner():
    #     time.sleep(3)

    # THIS DOES NOT KEEP THE TAB TITLE / IMAGE
    st.button("Test Timer", on_click=_sleep_and_show_spinner)


if __name__ == '__main__':
    main()