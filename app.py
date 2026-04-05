import streamlit as st
import plotly.express as px
from processing import get_data

statistics_df = get_data('data/education_true.csv')

st.set_page_config(page_title="Labour Market in Canada (Statistics Canada)", layout="wide")
st.caption("Source: Statistics Canada. Labour force characteristics by educational attainment, monthly, unadjusted for seasonality.")

st.sidebar.header("Filters")

status = statistics_df['Labour force characteristics'].unique()
education = statistics_df['Educational attainment'].unique()
gender = statistics_df['Gender'].unique()
age = statistics_df['Age group'].unique()

status_filter = st.sidebar.selectbox("Employment Status:", status)
gender_filter = st.sidebar.multiselect("Sex: ", gender, default=gender[0])
age_filter = st.sidebar.selectbox("Age group: ", age)
education_filter = st.sidebar.multiselect("Education Level(s):", education, default=education[5])

statistics_df_filtered = statistics_df[
    (statistics_df['Labour force characteristics'] == status_filter) &
    (statistics_df['Educational attainment'].isin(education_filter)) &
    (statistics_df['Gender'].isin(gender_filter)) &
    (statistics_df['Age group'] == age_filter)
]

st.title("Labour Market in Canada (Statistics Canada)")

graph = px.line(statistics_df_filtered, x='REF_DATE', y='VALUE', color='Educational attainment', facet_col='Gender', facet_col_spacing=0.05, height=500, title=f"{status_filter} for {gender_filter} in Canada ({age_filter})",
                labels={'REF_DATE': 'Date', 'VALUE': 'Rate (%)'})

st.plotly_chart(graph, use_container_width=True)

st.divider()

st.info("""
**Lately, many people have mentioned how the job market has been declining over the years.** Whether it’s through social media, news headlines, or conversations with friends, there is a growing sense of uncertainty. 
But does the data back this up? 

By looking at the numbers from **2019 to 2026**, we can see how events like the pandemic and shifting 
economic cycles have actually impacted different groups in Canada. 
        
This dashboard is designed to not only look at the employment trends, but to focus on educational attainment. Seeing if certain education performs higher than others, 
        and how each education level has been affected over the years.
        
Additionally, we would see other trends in the charts, such as the gender employment gap, and age range differences.
        
Feel free to play around with the filters and make your own analysis!
""")

st.sidebar.write("Future Updates: Adding metrics")
