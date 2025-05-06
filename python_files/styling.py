import streamlit as st

def custom_styling():
    st.markdown(
        """
        <style>
            .main {
                background-color: white !important;
                padding: 0 !important;
            }
            
            .title {
                font-family: "Open Sans", sans-serif;
                font-size: 50px;
                font-weight: bold;
                color: black;
            }
            
            .subtitle {
                font-family: "Open Sans", sans-serif;
                font-weight: 300;
                font-size: 35px;
                color: black;
                margin-top: -40px
            }
                
            .subheader {
                font-family: "Open Sans", sans-serif;
                font-size: 25px;
                color: black;
                margin-top: -50px
            }

            .text {
                font-family: "Open Sans", sans-serif;
                font-size: 16px;
                color: black;
                max-width: 500px;
            }
            
            .stTabs [data-baseweb="tab"] {
                font-family: "Open Sans", sans-serif;
                font-size: 30px;
                color: black;
                position : relative
            }
            
            .stTabs [data-baseweb="tab"]:hover {
                font-size: 30px;
                color: #4c416bff;
            }
            
            .stTabs [data-baseweb="tab"][aria-selected="true"] {
                font-weight: bold;
                color: #4c416bff;
            }

            .stButton > button {
                font-family: "Open Sans", sans-serif;
                background-color: white;
                color: black;
                border-color: green;
                padding: 8px 25px;
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .stButton > button:hover {
                background-color: #4c416bff;
                color: white;
            }
            
            .stSelectbox div[data-baseweb="select"] > div {
                background-color:white;
                border: 2px solid #4CAF50;
                color: black;
            }
            
            .stSelectbox div[data-baseweb="select"] .css-1uccc91-singleValue {
                background-color: white;
                border-color: green;
                color: black;
            }
            
            .stSelectbox div[data-baseweb="select"] .css-1n7v3ny-option {
                background-color: white;
                border-color: green;
                text-color: black;
            }
            
            .stNumberInput input {
                background-color: white;
                color: black;
                border: 2px solid #4CAF50;
                border-radius: 10px;
            }
            
            .stNumberInput > div > div > input[type=number] {
                border-radius: 0;
                padding: 0;
                margin: 0;
                border-color: green;
            }
            
            .stNumberInput > div > div > button:first-of-type {
                background-color: green;
                color: black;
                border-color: green;
            }
            
            .stNumberInput > div > div > button:last-of-type {
                background-color: green;
                border-color: green;
            }

            .stDateInput input {
                background-color: white;
                color: black;
                border: 2px solid #4CAF50;
                border-radius: 10px;
            }
            
            .stDateInput input:focus {
                background-color: white;
                border-color: green;
            }
            
            div[data-baseweb="radio"] > div {
                background-color: black;
                border: 1px solid #000;
                border-radius: 50%;
                width: 16px;
                height: 16px;
                display: inline-block;
                position: relative;
                border-color: green;
            }
    
            /* Input field styling */
            .stTextInput > div > div > input {
                background-color: white;
                color: #333;
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 8px 12px;
                border-color: green;
            }

            .stTextInput > div > div > input:focus {
                border-color: #FFC107;
                box-shadow: 0 0 0 2px rgba(255, 193, 7, 0.2);
                border-color: green;
                color: black;
                border-color: green;
            }
            
            .dataframe {
                border-collapse: collapse;
                width: 30%;
                
            }
            
            .dataframe th, .dataframe td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
                color: black;
                font-size: 15px;
            }
            .dataframe th {
                color: white;
            }
            
            .dataframe th {
                background-color: #4c416bff;
            }
            

        </style>
        """,
        unsafe_allow_html=True,
    )
