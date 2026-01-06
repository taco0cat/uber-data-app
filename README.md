# 🚕 Uber Pickups in NYC (Streamlit Demo)

A simple interactive dashboard visualizing Uber pickup data in New York City.

I built this project to learn the basics of **Streamlit** and how to handle data visualization in Python. It processes a dataset of Uber pickups to show how caching, filtering, and 3D mapping work in a real-time web app.

## 🚀 Live Demo
[**View the Live App Here**](https://uber-nyc-demo.streamlit.app/)

## 🔍 What I Learned
Through this project, I explored:
* **Data Caching:** Using `@st.cache_data` to load 10k rows of data without slowing down the app on every interaction.
* **NumPy Histograms:** Converting raw timestamps into a "busiest hours" bar chart.
* **PyDeck Visualization:** Mapping geospatial data into a 3D hexagonal density layer to visualize hotspots.

## 🛠️ Tech Stack
* **Python 3.13**
* **Streamlit**
* **Pandas & NumPy**
* **PyDeck**

## 📦 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/taco0cat/uber-data-app.git](https://github.com/taco0cat/uber-data-app.gitt)
    cd uber-data-app
    ```

2.  **Setup Environment**
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

    # Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App**
    ```bash
    streamlit run streamlit_app.py
    ```

## 📚 Acknowledgements
This project is based on the official [Streamlit "Create an App" tutorial](https://docs.streamlit.io/get-started/tutorials/create-an-app). The source code and dataset are adapted from their documentation for educational purposes.