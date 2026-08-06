import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#F8FAFC;
    }

    .main-title{

        text-align:center;
        color:#2563EB;
        font-size:42px;
        font-weight:bold;
        margin-bottom:5px;

    }

    .sub-title{

        text-align:center;
        color:#64748B;
        font-size:18px;
        margin-bottom:30px;

    }

    .card{

        background:white;
        padding:20px;
        border-radius:10px;
        border:1px solid #E2E8F0;

    }

    .footer{

        text-align:center;
        color:gray;
        margin-top:40px;

    }

    </style>
    """, unsafe_allow_html=True)