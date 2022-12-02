import streamlit as st
from pathlib import Path


def st_directory_picker(initial_path=Path()):

    st.sidebar.markdown("#### Directory picker")

    if "path" not in st.session_state:
        st.session_state.path = initial_path.absolute()

    manual_input = st.sidebar.text_input("Selected directory:", st.session_state.path)

    manual_input = Path(manual_input)
    if manual_input != st.session_state.path:
        st.session_state.path = manual_input
        st.experimental_rerun()

    col1, col2, col3 = st.sidebar.columns([1, 3, 1])

    with col1:
        col1.markdown("#")
        if col1.button("⬅️") and "path" in st.session_state:
            st.session_state.path = st.session_state.path.parent
            st.experimental_rerun()

    with col2:
        subdirs = [
            f.stem
            for f in st.session_state.path.iterdir()
            if f.is_dir()
            and (not f.stem.startswith(".") and not f.stem.startswith("__"))
        ]
        if subdirs:
            st.session_state.new_dir = st.selectbox(
                "Subdirectories", sorted(subdirs)
            )
        else:
            col2.markdown("#")
            col2.markdown(
                "<font color='#FF0000'>No subdir</font>", unsafe_allow_html=True
            )

    with col3:
        if subdirs:
            col3.markdown("#")
            if col3.button("➡️") and "path" in st.session_state:
                st.session_state.path = Path(
                    st.session_state.path, st.session_state.new_dir
                )
                st.experimental_rerun()

    return st.session_state.path