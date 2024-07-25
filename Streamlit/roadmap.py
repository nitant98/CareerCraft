
import streamlit as st

def main():
   
    # Create tabs
    tab1, tab2 = st.tabs(["Roadmap", "Job Listings"])
    #tab1, tab2, tab3 = st.tabs(["Main", "Feedback", "Label"])
    with tab1: 
        st.title("Roadmap")
        show_content()

    with tab2:
        st.title("Job Listings")
        show_job_listings()

def show_content():
    streams = ["Data Engineering", "Front End Developer", "Data Analyst", "Business Analyst"]
    
    selected_stream = st.sidebar.radio("Select Stream", streams)

    st.header(f"{selected_stream}")
        
    topics = ["SQL", "Python", "Big Data"]  

    for topic in topics:
        # Outline box for the topic button and sub-header buttons
        topic_expander = st.expander(f"{topic}", expanded=False)
        
        with topic_expander:
            st.markdown("""
                <style>
                    div.st-expander.expander-container {
                        border: 2px solid #3498db;
                        border-radius: 5px;
                        padding: 10px;
                        background-color: #3498db;
                    }
                    div.st-expander.expander-container:hover {
                        border: 20px solid #fcfcfc;
                    }
                    div.st-expander-header {
                        color: white;
                    }
                </style>
            """, unsafe_allow_html=True)
            
            # Course button with unique key
            show_courses = st.button(f"Courses {topic}")
            
            if show_courses:
                courses = {
                    "The Complete SQL Bootcamp": {
                        "logo": "/Users/rutu/Downloads/Big Data /Case Study 0/Roadmap/udemy.png",
                        "link": "https://www.udemy.com/course/the-complete-sql-bootcamp/"
                    },
                    "Introduction to Structured Query Language (SQL)": {
                        "logo": "/Users/rutu/Downloads/Big Data /Case Study 0/Roadmap/coursera.png",
                        "link": "https://www.coursera.org/learn/intro-sql"
                    },
                }
                for course, details in courses.items():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.markdown(f"[{course}]({details['link']})")
                    with col2:
                        st.image(details["logo"], use_column_width=False, caption="", width=80)
   
            # Reading Material button with unique key
            show_reading_material = st.button(f"Reading Material {topic}")
            if show_reading_material:
                reading_material = {
                    "SQL": {
                        "logo": "/Users/rutu/Downloads/Big Data /Case Study 0/Roadmap/w3.png",
                        "link": "https://www.w3schools.com/sql/"
                    },
                }
                for reading_material, details in reading_material.items():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.markdown(f"[{reading_material}]({details['link']})")
                    with col2:
                        st.image(details["logo"], use_column_width=False, caption="", width=80)

            # Hands-on Resources button with unique key
            show_hands_on_resources = st.button(f"Hands-on Resources {selected_stream} {topic}")
            if show_hands_on_resources:
                hands_on_resources = {
                     "Data Lemur": {
                        "logo": "/Users/rutu/Downloads/Big Data /Case Study 0/Roadmap/data lemur.png",
                        "link": "https://datalemur.com/"
                    },
                }
                for hands_on_resources, details in hands_on_resources.items():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.markdown(f"[{hands_on_resources}]({details['link']})")
                    with col2:
                        st.image(details["logo"], use_column_width=False, caption="", width=80)

def show_job_listings():
    job_listings = [
        {"title": "Data Engineer : Chicago Bulls ", "linkedin": "https://www.linkedin.com/jobs/view/3802878490"},
        {"title": "Data Engineer : Spurs Sports & Entertainment", "linkedin": "https://www.linkedin.com/jobs/view/3768084197"},
        {"title": "Data Engineer III: Hinge", "linkedin": "https://www.linkedin.com/jobs/view/3802548884"}
       
    ]

    for job in job_listings:
        st.write(f"{job['title']}")
        st.write(f"LinkedIn: [{job['title']}]({job['linkedin']})")
        st.write("---")  # Add a separator between job listings

   

if __name__ == "__main__":
    main()
