import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Custom E-commerce Homepage", layout="wide")

# 1. Search Bar Section
st.write("## Search for Products")
search_query = st.text_input("Enter product name or keyword...")

# 2. Category Selection Section
st.write("## Select a Category")
categories = ["Clothing", "Electronics", "Home Goods", "Beauty", "Sports"]
selected_category = st.selectbox("Choose a category:", categories)

# 3. Sub-category Display
sub_categories = {
    "Clothing": ["Men", "Women", "Kids", "Accessories"],
    "Electronics": ["Mobile Phones", "Laptops", "Tablets", "Accessories"],
    "Home Goods": ["Furniture", "Kitchen", "Decor", "Bedding"],
    "Beauty": ["Skincare", "Makeup", "Haircare", "Fragrance"],
    "Sports": ["Fitness", "Outdoor", "Team Sports", "Accessories"]
}

if selected_category:
    st.write(f"### {selected_category} - Subcategories")
    selected_sub_category = st.radio(f"Select a subcategory within {selected_category}:", sub_categories[selected_category])

# Display the selected options
if search_query:
    st.write(f"Searching for: {search_query}")

if selected_category and selected_sub_category:
    st.write(f"You selected: {selected_category} > {selected_sub_category}")
