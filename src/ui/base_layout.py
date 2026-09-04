import streamlit as st

def background_style_layout():
    st.markdown("""
                <style>
                .stApp {
                  background-color:#5865F2 !important;
                }
                
                header {
                  visibility: hidden;
                  }
                   
                /*two box columns*/          
                .stApp div[data-testid="stColumn"]{      
                  background-color:#E0E3FF !important;
                  padding:1.8rem 1.2rem !important;
                  border-radius:3rem !important;
                  display: flex !important;
                  flex-direction: column !important;
                  align-items: center !important;
                }
                
                div[data-testid="stImage"] {
                  position: relative;
                  left: 10rem; 
                  top: 0;
                }
              </style>
              
              """, unsafe_allow_html=True)


def style_background_dashboard():
  
  st.markdown("""
              <style>
                .stApp {
                  background: #E0E3FF !important
                }
                
                header {
                  visibility: hidden;
                  }
                
        
              </style>
              """, unsafe_allow_html=True)
  
  
def style_base_layout():
  
  st.markdown("""
              <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                   
                   
                .block-container {
                  padding-top: 1.5rem !important;
                  padding-bottom: 0.5rem !important;
                  max-width: 1000px !important;
                  }
                  
                /*Hide top bar of streamlit*/
                #MainMenu, footer, header {
                  visibility : hidden;
                }
                h1 {
                  font-family: 'Climate Crisis', sans-serif !important;
                  font-size: 2rem !important;
                  line-height: 0.9 !important;
                  margin:0rem !important;
                  letter-spacing: 2px !important;
                }
                h2 {
                  font-family: 'Climate Crisis', sans-serif !important;
                  font-size: 1.4rem !important;
                  line-height: 1 !important;
                  margin:0rem !important;
                  color:black !important;
                  letter-spacing: 0.5px !important;
                  text-align:center;
                }
                
                h3, h4, p {
                  font-family:"Outfit", sans-serif !important;
                }
                
                button {
                  background-color:#5865F2 !important;
                  border-radius:1.5rem !important;
                  color:white !important;
                  border:none !important;
                  transition:transform 0.25s ease-in-out !important;
                }
                button[kind="secondary"] {
                  background-color:#EB459E !important;
                  border-radius:1.5rem !important;
                  color:white !important;
                  border:none !important;
                  transition:transform 0.25s ease-in-out !important;
                }
                
                button[kind="tertiary"] {
                  background-color : black !important;
                  border-radius:1.5rem !important;
                  color:white !important;
                  border:none !important;
                  transition:transform 0.25s ease-in-out !important;
                }
                
                button:hover{
                  transform:scale(1.05)
                }
                
              </style>
              """, unsafe_allow_html=True)
  