import streamlit as st

def main():
    # Page layout
    st.set_page_config(
        page_title="My Personal Website",
        page_icon="🚀",
        layout="wide",
    )

    # Sidebar
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", ["Home", "About", "Education", "Work Experience", "Hobbies and Interests", "Projects"])

    # Main content
    if selected_page == "Home":
        show_home()
    elif selected_page == "About":
        show_about()
    elif selected_page == "Education":
        show_education()
    elif selected_page == "Work Experience":
        show_work_experience()
    elif selected_page == "Hobbies and Interests":
        show_hobbies_interests()
    elif selected_page == "Projects":
        show_projects()

def show_home():
    st.title("Welcome to My Personal Website")
    st.image("picture.jpg", caption="My Profile Picture", use_column_width=True)

def show_about():
    st.title("About Me")
    st.write("My name is Ankit Shaw.")

def show_education():
    st.title("Education")
    st.write("M.S.(Robotics) UW.")

def show_work_experience():
    st.title("Work Experience")
    st.write("Tech engineer")

def show_hobbies_interests():
    st.title("Hobbies and Interests")
    st.write("Exploring app")

def show_projects():
    st.title("Interesting Projects")
    st.write("Face recognisation with opencv")

if __name__ == "__main__":
    main()
