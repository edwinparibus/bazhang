import streamlit as st
import streamlit.components.v1 as components
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

st.set_page_config(
    page_title="Test App",
    #page_icon='./KANTAR_Small_Logo_White_RGB.png',
    layout="centered",
    initial_sidebar_state="expanded"
    )

set_png_as_page_bg('./2514320.jpg')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

components.iframe("""https://www.youtube.com/embed/5oc9cAUo3Jo""" , scrolling = True , height = 350)
