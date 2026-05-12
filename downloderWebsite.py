import streamlit as st
if "clicked" not in st.session_state:
    st.session_state.clicked=False
def setFlag():
    st.session_state.clicked=True

st.title("Download TermCode 1.29.0 Executable Here.")
st.divider()
with open("TermCode.exe", "rb") as f:
    st.download_button(label="TermCode",
                       data=f,
                       file_name=r"TermCode.exe",
                       mime="application/octet-stream",
                       on_click=setFlag())
if st.session_state.clicked==True:
    st.success("Thank you!")
    st.divider()
    st.info("Hope you enjoy your editor!")
    st.divider()
    st.write("""
            1. Move the TermCode.exe file to Desktop.
            2. Add it to path if you want.""")
    st.caption("The developer isn't attributed to any malicious effect. It's not malicious actually, btw.")
