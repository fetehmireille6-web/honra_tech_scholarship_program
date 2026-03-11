import streamlit as st
import requests
API_URL = "http://127.0.0.1:8000"
st.title("Mireille's Item Store")
tab1, tab2, tab3 = st.tabs(["Create Item", "View Items", "Statistics"])
with tab1:
    st.header("Create a New Item")
    with st.form("create_item_form"):
        item_id = st.number_input("Item ID", min_value=0, step=1)
        name = st.text_input("Item Name")
        price = st.number_input("Price", min_value=0.01,)
        quantity = st.number_input("Quantity", min_value=0)
        category = st.selectbox("Category", ["Electronics", "Clothing", "Books", "Home", "Toys"])
        if st.form_submit_button("Create Item"):
            item_data = {"id": item_id, "name": name, "price": price, "quantity": quantity, "category": category}
            response = requests.post(f"{API_URL}/items", json=item_data)
            if response.status_code == 200:
                st.success("Item created successfully!")
                st.json(response.json())
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
with tab2:
    st.header("View Items")
    category_filter = st.selectbox("Filter by Category", ["All", "Electronics", "Clothing", "Books", "Home", "Toys"])
    min_price_filter = st.number_input("Minimum Price", min_value=0.0)
    max_price_filter = st.number_input("Maximum Price", min_value=0.0)
    if st.button("Apply Filters"):
        params = {}
        if category_filter != "All":
            params["category"] = category_filter
        if min_price_filter > 0:
            params["min_price"] = min_price_filter
        if max_price_filter > 0:
            params["max_price"] = max_price_filter
        response = requests.get(f"{API_URL}/items", params=params)
        if response.status_code == 200:
            items = response.json().get("items", [])
            if items:
                st.json(items)
            else:
                st.info("No items found with the applied filters.")
        else:
            st.error("Error fetching items.")
with tab3:
    st.header("store stats")
    if st.button("Get Statistics"):
        response = requests.get(f"{API_URL}/stats").json()
        col1, col2 = st.columns(2)
        col1.metric("Total Items", response.get("total_items", 0))
        col2.metric("Total Inventory Value", f"${response.get('total_inventory_value', 0.0):.2f}")
        most_expensive_item = response.get("most_expensive_item")
        if most_expensive_item:
            st.subheader("Most Expensive Item")
            st.json(most_expensive_item)
            
        else:
            st.error("Error fetching statistics.")
    
