import streamlit as st
import pandas as pd

# Title
st.title("🌾 AgriChatBot – Rainfall Q&A System (Prototype)")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("rainfall.csv")
    return df

df = load_data()

st.subheader("📊 Dataset Preview")
st.write(df.head())

# Ask user question
question = st.text_input("Ask a question about rainfall (e.g. 'highest rainfall district in Maharashtra'):")

if question:
    question_lower = question.lower()
    
    # Example logic (you can expand this later)
    if "highest" in question_lower and "rainfall" in question_lower:
        if "district" in df.columns.str.lower():
            # Find highest rainfall value
            rainfall_col = [c for c in df.columns if "rain" in c.lower()][0]
            district_col = [c for c in df.columns if "district" in c.lower()][0]
            max_row = df.loc[df[rainfall_col].idxmax()]
            st.success(f"🏆 Highest rainfall: {max_row[district_col]} with {max_row[rainfall_col]} mm")
        else:
            st.warning("Couldn't find district column in your data.")
    else:
        st.info("❓ Sorry, I can currently answer only 'highest rainfall' type questions.")