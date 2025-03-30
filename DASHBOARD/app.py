import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data-Driven Insights for Viksit Bharat",
    page_icon=" ⚡ ",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv('results.csv')
    return df

df = load_data()

st.sidebar.title("Dashboard Navigation")
viz_option = st.sidebar.radio("Select Visualization", [
    "Overview",
    "Internet Facility Distribution",
    "Online Purchases by Category",
    "Payment Method Distribution",
    "Households by Sector",
    "Online Purchases Over Time",
    "Correlation Heatmap"
])

if 'Year' in df.columns:
    year_list = sorted(df['Year'].dropna().unique())
    selected_year = st.sidebar.selectbox("Select Year", options=year_list)
    df_filtered = df[df['Year'] == selected_year]
else:
    df_filtered = df

online_purchase_categories = [
    'Whether_any_online_purchase/payment_has_been_made_during_the_reference_period_to_buy_-_Fuel_&_light',
    'Whether_any_online_purchase/payment_has_been_made_during_the_reference_period_to_buy_-_Toilet_articles_&_other_household_consumables',
    'Whether_any_online_purchase/payment_has_been_made_during_the_reference_period_to_buy_-_Education',
    'Whether_any_online_purchase/payment_has_been_made_during_the_reference_period_to_buy-_Medicine_&_other_medical_services',
    'Whether_any_online_purchase/payment_has_been_made_during_the_reference_period_to_buy-_Services_(Travel,_Recharges,_Bill_payment,_Cinema/Theatre,_internet,_etc.)_'
]

if viz_option == "Overview":
    st.title("Data-Driven Insights for Viksit Bharat")
    st.markdown("### Overview")
    st.dataframe(df.head(10))
    st.markdown(f"**Total Records:** {df.shape[0]}  |  **Columns:** {df.shape[1]}")

elif viz_option == "Internet Facility Distribution":
    st.title("Internet Facility Distribution in Households")
    if 'Household_has_internet_facility_as_on_the_date_of_the_survey' in df_filtered.columns:
        internet_counts = df_filtered['Household_has_internet_facility_as_on_the_date_of_the_survey'].value_counts()
        fig = px.pie(
            names=internet_counts.index,
            values=internet_counts.values,
            title="Internet Facility Availability",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig, use_container_width=True)

elif viz_option == "Online Purchases by Category":
    st.title("Online Purchases by Category")

    for col in online_purchase_categories:
        if col in df_filtered.columns:
            df_filtered[col] = df_filtered[col].map({'Yes': 1, 'No': 0}).fillna(0)

    category_counts = df_filtered[online_purchase_categories].apply(pd.Series.value_counts).fillna(0)
    
    if category_counts.shape[1] == 2:
        category_counts.columns = ['No', 'Yes']
    elif category_counts.shape[1] == 1:
        only_response = category_counts.columns[0]
        if only_response == 0:
            category_counts = category_counts.rename(columns={0: 'No'})
            category_counts['Yes'] = 0
        elif only_response == 1:
            category_counts = category_counts.rename(columns={1: 'Yes'})
            category_counts['No'] = 0
    
    fig = px.bar(
        category_counts,
        barmode='stack',
        title="Online Purchases Made During the Reference Period",
        labels={"value": "Number of Households", "index": "Category"},
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

elif viz_option == "Payment Method Distribution":
    st.title("Payment Method Distribution")
    payment_col = 'If_yes_in_Q4.2.9_Amount_?'
    if payment_col in df_filtered.columns:
        payment_counts = df_filtered[payment_col].value_counts()
        fig = px.pie(
            names=payment_counts.index,
            values=payment_counts.values,
            title="Distribution of Online Payment Methods",
            color_discrete_sequence=px.colors.sequential.Blues
        )
        st.plotly_chart(fig, use_container_width=True)

elif viz_option == "Households by Sector":
    st.title("Households by Sector")
    if 'Sector' in df_filtered.columns:
        sector_counts = df_filtered['Sector'].value_counts().reset_index()
        sector_counts.columns = ['Sector', 'Count']
        fig = px.bar(
            sector_counts,
            x='Sector',
            y='Count',
            title="Households by Sector (Urban vs Rural)",
            color='Sector',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig, use_container_width=True)

elif viz_option == "Online Purchases Over Time":
    st.title("Online Purchases Over Time")
    if 'Year' in df.columns:
        time_trend = df.groupby('Year').size().reset_index(name='Purchases')
        fig = px.line(
            time_trend,
            x='Year',
            y='Purchases',
            markers=True,
            title="Trend of Online Purchases Over the Years",
            color_discrete_sequence=['#17becf']
        )
        st.plotly_chart(fig, use_container_width=True)

elif viz_option == "Correlation Heatmap":
    st.title("Correlation Between Purchase Categories")
    df_corr = df_filtered.copy()
    for col in online_purchase_categories:
        if col in df_corr.columns:
            df_corr[col] = pd.to_numeric(df_corr[col].map({'Yes': 1, 'No': 0}), errors='coerce')
    corr_matrix = df_corr[online_purchase_categories].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.markdown("Download Cleaned Data")
st.sidebar.download_button(
    label="Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="online_purchase_data.csv",
    mime="text/csv"
)

st.sidebar.text("Created by Abhishek Sharma")
