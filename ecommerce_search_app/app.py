import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# Function to search Amazon (placeholder)
def search_amazon(query):
    try:
        # Implement web scraping or API call to Amazon here
        # Example using requests and BeautifulSoup:
        url = f"https://www.amazon.com/s?k={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract product information from the soup object
        time.sleep(1) # Delay to avoid rate limiting
        return f"Amazon: Results for '{query}' (Placeholder - Implement web scraping here)"
    except requests.exceptions.RequestException as e:
        return f"Amazon: Request failed - {e}"
    except Exception as e:
        return f"Amazon: An unexpected error occurred - {e}"

# Function to search Ebay (placeholder)
def search_ebay(query):
    try:
        # Implement web scraping or API call to Ebay here
        # Example using requests and BeautifulSoup:
        url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract product information from the soup object
        time.sleep(1) # Delay to avoid rate limiting
        return f"Ebay: Results for '{query}' (Placeholder - Implement web scraping here)"
    except requests.exceptions.RequestException as e:
        return f"Ebay: Request failed - {e}"
    except Exception as e:
        return f"Ebay: An unexpected error occurred - {e}"

# Function to search MercadoLibre (placeholder)
def search_mercadolibre(query):
    try:
        # Implement web scraping or API call to MercadoLibre here
        # Example using requests and BeautifulSoup:
        url = f"https://listado.mercadolibre.com.ar/{query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract product information from the soup object
        time.sleep(1) # Delay to avoid rate limiting
        return f"MercadoLibre: Results for '{query}' (Placeholder - Implement web scraping here)"
    except requests.exceptions.RequestException as e:
        return f"MercadoLibre: Request failed - {e}"
    except Exception as e:
        return f"MercadoLibre: An unexpected error occurred - {e}"

# Function to search Aliexpress (placeholder)
def search_aliexpress(query):
    try:
        # Implement web scraping or API call to Aliexpress here
        url = f"https://www.aliexpress.com/wholesale?SearchText={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract product information from the soup object
        time.sleep(1) # Delay to avoid rate limiting
        return f"Aliexpress: Results for '{query}' (Placeholder - Implement web scraping here)"
    except requests.exceptions.RequestException as e:
        return f"Aliexpress: Request failed - {e}"
    except Exception as e:
        return f"Aliexpress: An unexpected error occurred - {e}"

# Function to search Walmart (placeholder)
def search_walmart(query):
    try:
        # Implement web scraping or API call to Walmart here
        url = f"https://www.walmart.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract product information from the soup object
        time.sleep(1) # Delay to avoid rate limiting
        return f"Walmart: Results for '{query}' (Placeholder - Implement web scraping here)"
    except requests.exceptions.RequestException as e:
        return f"Walmart: Request failed - {e}"
    except Exception as e:
        return f"Walmart: An unexpected error occurred - {e}"

# Function to save feedback to CSV
def save_feedback(name, country, query, satisfaction, comment):
    df = pd.DataFrame([[name, country, query, satisfaction, comment]],
                      columns=['Name', 'Country', 'Query', 'Satisfaction', 'Comment'])
    try:
        existing_df = pd.read_csv('feedback.csv')
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv('feedback.csv', index=False)

# Main application
def main():
    st.title("E-commerce Search Engine")

    # Initialize search_query in session state if it doesn't exist
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""

    # Sidebar navigation
    page = st.sidebar.selectbox("Choose a page", ["Index", "Search Results", "Feedback"])
    st.sidebar.image("static/aliexpress_logo.png", width=100)
    st.sidebar.image("static/amazon_logo.png", width=100)
    st.sidebar.image("static/ebay_logo.png", width=100)
    st.sidebar.image("static/mercadolibre_logo.png", width=100)
    st.sidebar.image("static/walmart_logo.png", width=100)
    
    st.markdown(
    """
    <div style="position: fixed !important; bottom: 10px !important; left: 10px !important; background-color: white; padding: 10px; border-radius: 5px; color: black;">
        <b>Autor:</b> Walter Ariel Pelourson<br>
        <b>Profesión:</b> Analista de sistemas y data science<br>
        <b>Email de contacto:</b> <a href="mailto:walterarielpelourson@gmail.com" style="color: black;">walterarielpelourson@gmail.com</a>
    </div>
    """,
    unsafe_allow_html=True,
)

    if page == "Index":
        st.header("Welcome to the E-commerce Search Engine!")
        st.write("Here are some popular items people are buying:")
        st.write("Replace this with image display code.  You can use st.image() to display images from URLs or local files.")
        # Add images of popular items here, e.g., using st.image()

    elif page == "Search Results":
        st.header("Search Results")

        if "search_results" not in st.session_state:
            st.session_state.search_results = {}

        query = st.text_input("Enter your search query:", key="search_query")
        if st.button("Search"):
            st.session_state.search_results = {
                "amazon": search_amazon(query),
                "ebay": search_ebay(query),
                "mercadolibre": search_mercadolibre(query),
                "aliexpress": search_aliexpress(query),
                "walmart": search_walmart(query),
            }

        if st.session_state.get("search_results"):
            #st.write("Replace this with Amazon logo")
            #st.write(st.session_state.search_results["amazon"])
            #st.write(st.session_state.search_results["ebay"])
            if st.button("View Search Results"):
                import requests
                st.write(f"Click the links below to view the search results in new tabs:")
                st.write(f"[Amazon Search Results](https://www.amazon.com/s?k={requests.utils.quote(query)})")
                st.write(f"[Ebay Search Results](https://www.ebay.com/sch/i.html?_nkw={requests.utils.quote(query)})")
                st.write(f"[Mercado Libre Search Results](https://listado.mercadolibre.com.ar/{requests.utils.quote(query)})")
                st.write(f"[Aliexpress Search Results](https://www.aliexpress.com/wholesale?SearchText={requests.utils.quote(query)})")
                st.write(f"[Walmart Search Results](https://www.walmart.com/search?q={requests.utils.quote(query)})")

    elif page == "Feedback":
        st.header("Feedback")
        name = st.text_input("Name:", key="name")
        country = st.text_input("Country:", key="country")
        query = st.text_input("Search Query:", key="query")
        satisfaction = st.selectbox("Satisfaction Level", ["Very Good", "Good", "Bad"], key="satisfaction")
        comment = st.text_area("Comments:", key="comment")

        if st.button("Submit Feedback"):
            save_feedback(name, country, query, satisfaction, comment)
            st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
