import time

import streamlit as st


def _sleep_and_show_spinner():
    with st.spinner():
        time.sleep(3)


def main():
    st.title("Spinner Test Page")
    with st.spinner():
        time.sleep(3)

    st.button("Test Timer", on_click=_sleep_and_show_spinner)


if __name__ == '__main__':
    main()