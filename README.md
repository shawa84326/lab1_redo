# TECHIN 510 Lab 1

A personal website for TECHIN 510 Lab 1.

## How to Run

Open the terminal and run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
for output visit go to ankit25-tenchin510-lab1.azurewebsites.net

## What's Included

- `app.py`: The main Flask application
- 'picture.jpg' : Personal photo for website
- 'requirements.txt': All the dependecies to be installed 

## Lessons Learned

- How to use Streamlit to create a simple website
- How to use requirements.txt to manage Python dependencies
- How to use GitHub Actions to deploy a website to Azure App Service

## Questions / Uncertainties

- What if I want to make the profile picture round?

- I guess by using CSS we can achieve this
-  st.markdown(
        f"""
        <style>
            img {{
                border-radius: 50%;
                object-fit: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
- How to use a two column layout?
- Two-Column Layout: st.columns(2) creates two columns, col1 and col2. The with col1 and with col2 blocks define the content within each column.
