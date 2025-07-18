import time

import streamlit as st

from streamlit_extras.stylable_container import stylable_container


def _sleep_and_show_spinner():
    with st.spinner():
        time.sleep(3)


def main():
    st.title("Spinner Test Page")

    button_cols = st.sidebar.columns([1, 4, 2, 4, 1])
    with button_cols[1]:
        with stylable_container(
                key="test_container",
                css_styles="""
                    button {
                        background-color: #1D867F;
                        color: white;
                    }"""):
            st.button("**Test Timer**", on_click=_sleep_and_show_spinner,
                      use_container_width=True)


if __name__ == '__main__':
    main()