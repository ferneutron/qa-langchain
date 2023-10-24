import streamlit as st
from streamlit_chat import message as st_message

from qa import QAModel

@st.cache_resource()
def initialize_qamodel():
    return QAModel()


class QAApplication:
    def __init__(self):
        self.qamodel = initialize_qamodel()

    def generate_answer(self):

        request = st.session_state.request
        
        response = self.qamodel(request=request)
        
        st.session_state.history.append({"message": request, "is_user": True})
        st.session_state.history.append({"message": response['result'], "is_user": False})
        
        st.session_state.something = st.session_state.request
        st.session_state.input_text = ''

    def run_app(self):
        st.title("Ask me anything about Coffee ☕️")

        if "history" not in st.session_state:
            st.session_state.history = []

        if st.button("Clear"):
            st.session_state.history = []

        st.text_input("", key="request", on_change=self.generate_answer)
        
        for i, chat in enumerate(st.session_state.history):
            st_message(**chat, key=str(i)) #unpacking

if __name__ == '__main__':
    qa = QAApplication()
    qa.run_app()