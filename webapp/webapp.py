import streamlit as st
import pandas as pd
import numpy as np

def load_theme_from_toml(toml_file):
    # Load theme settings from the TOML file
    with open(toml_file, "r") as file:
        theme_settings = toml.load(file)
    return theme_settings

def main():
    # Set the page configuration
    st.set_page_config(
        page_title="My Streamlit App",
        page_icon=":racehorse:",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # Your Streamlit app code goes here
    st.title("My Streamlit App")
    st.write("Welcome to my Streamlit app!")

if __name__ == "__main__":
    main()

# Your data loading and cleaning functions go here
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
# Define the pages
pages = ['Home', 'About Us', 'Which Horse', 'Performance Metrics', 'Project Challenges', 'Project Outcomes']

# Sidebar navigation
selected_page = st.sidebar.selectbox('Navigation', pages)

# Display content based on the selected page
if selected_page == 'Home':
    st.markdown('## Which Horse')


elif selected_page == 'About Us':
    st.markdown('## Meet the Which Horse Team')
    st.write('''Horse racing holds significant economic and entertainment value, attracting widespread attention from enthusiasts and bettors.

             \nCreating machine learning models to predict horserace outcomes is crucial for enhancing betting strategies, improving the accuracy of odds, and providing valuable insights to both industry professionals and casual participants, ultimately contributing to a more informed and engaging horse racing experience.
             ''')


    team_data = [
        {"name": "Harlequin", "image_url": "../raw_data/team_photos/harlequin_photo.jpeg", "bio": "Bio for Team Member 1"},
        {"name": "Rob", "image_url": "../raw_data/team_photos/rob_photo.jpeg", "bio": "Bio for Team Member 2"},
        {"name": "Amanda", "image_url": "../raw_data/team_photos/amanda_photo.jpeg", "bio": "Bio for Team Member 3"},
        {"name": "Tomi", "image_url": "../raw_data/team_photos/tomi_photo.jpeg", "bio": "Bio for Team Member 4"},
        {"name": "David", "image_url": "../raw_data/team_photos/david_photo.jpeg", "bio": "Bio for Team Member 5"},
    ]

    for team_member in team_data:
        st.subheader(team_member["name"])
        st.image(team_member["image_url"], width=150,  use_column_width=False, caption=f"Image of {team_member['name']}")
        st.text(team_member["bio"])
        st.markdown('---')  # Add a horizontal line between team members

elif selected_page == 'Which Horse':
    st.markdown('## Which Horse')
    st.write('''Horse racing holds significant economic and entertainment value, attracting widespread attention from enthusiasts and bettors.

             \nCreating machine learning models to predict horserace outcomes is crucial for enhancing betting strategies, improving the accuracy of odds, and providing valuable insights to both industry professionals and casual participants, ultimately contributing to a more informed and engaging horse racing experience.
             ''')

    st.markdown('## Model 1')
    @st.cache_data
    def get_line_chart_data():

        return pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c']
            )

    df = get_line_chart_data()

    st.line_chart(df)

    st.markdown('## Model 2')
    @st.cache_data
    def get_line_chart_data():

        return pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c']
            )

    df = get_line_chart_data()

    st.line_chart(df)

    st.markdown('## Model 3')
    @st.cache_data
    def get_line_chart_data():

        return pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c']
            )

    df = get_line_chart_data()

    st.line_chart(df)

    st.markdown('## Model 4')
    @st.cache_data
    def get_line_chart_data():

        return pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c']
            )

    df = get_line_chart_data()

    st.line_chart(df)

    # Add more content as needed

elif selected_page == 'Performance Metrics':
    st.markdown('## Performance Metrics')
    st.write('''Comparison of loss functions across all of our models. We could include all sorts
             of pretty graphs if we really wanted ! :)
             ''')
    @st.cache_data
    def get_line_chart_data():

        return pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c']
            )

    df = get_line_chart_data()

    st.line_chart(df)
    st.write('''Look! We can add multiple graphs. Big fun, many happy!
             ''')
    st.line_chart(df)
    st.write('''And once more, we can add a 3rd graph!
             ''')
    st.line_chart(df)

    # Add more content as needed

elif selected_page == 'Project Challenges':
    st.markdown('## Project Challenges')
    st.write('''Project challenge #1
             \n Project challenge #2
             \n Project challenge #3
                 ''')
    # Add a placeholder for dynamic scrolling
    st.markdown('<div style="height:1000px;"></div>', unsafe_allow_html=True)

        # Create sections with dynamic headings

        # Rest of your Streamlit app code (e.g., data display, graphs, etc.)
        # ...

elif selected_page == 'Project Outcomes':
    st.markdown('## Project Challenges')
    st.write('''Project outcome #1
             \n Project outcome #2
             \n Project outcome #3
                 ''')
    # Add a placeholder for dynamic scrolling
    st.markdown('<div style="height:1000px;"></div>', unsafe_allow_html=True)

        # Create sections with dynamic headings

        # Rest of your Streamlit app code (e.g., data display, graphs, etc.)
