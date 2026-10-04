import streamlit as st
import requests

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")

st.title("✈️ AI Travel Planner")
st.write("Enter any destination to get 3 curated spots from our AI guide.")

city = st.text_input("Enter a city:", placeholder="e.g. Kyoto, Jaipur, Barcelona")

if st.button("Get Recommendations"):
    if not city:
        st.warning("Please type a city name first.")
    else:
        with st.spinner(f"Agent is scouting recommendations for {city}..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/plan",
                    json={"city": city},
                    timeout=60
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("Recommendations Ready!")
                    st.markdown(data["recommendations"])
                else:
                    st.error("Failed to generate recommendations. Please try again.")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")