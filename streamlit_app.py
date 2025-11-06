import streamlit as st
import langchain_helper 
st.title("BusinessLaunch AI")
company = st.sidebar.selectbox("Pick a Company Type", 
                     ["IT & Technology Services", 
                      "Food & Beverage", 
                      "Health & Wellness",
                      "Retail & E-commerce",
                      "Education & Training"]
                      ) 



if company:
    with st.spinner("Generating your business idea..."):
        response = langchain_helper.generate_business_idea(company)

    business_name = response.get("company_name", "Unnamed Company")
    ideas = response.get("investment_details", "").split(",")

    st.subheader(f"💡 Generated Business Idea: **{business_name}**")
    st.write("### Here are some key things to consider:")
    for idea in ideas:
        st.markdown(f"- {idea.strip()}")

if __name__ == "__main__":
    print("Streamlit app loaded successfully.")