import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .prediction-box {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'model_trained' not in st.session_state:
    st.session_state.model_trained = False
if 'models' not in st.session_state:
    st.session_state.models = {}
if 'scaler' not in st.session_state:
    st.session_state.scaler = None
if 'feature_names' not in st.session_state:
    st.session_state.feature_names = []

# Sample data generation function
@st.cache_data
def generate_sample_data():
    """Generate sample real estate data for demonstration"""
    np.random.seed(42)
    n_samples = 1000
    
    # Generate synthetic real estate data
    locations = ['Downtown', 'Suburb', 'Urban', 'Rural', 'Coastal']
    property_types = ['Apartment', 'House', 'Condo', 'Villa']
    
    data = {
        'location': np.random.choice(locations, n_samples),
        'property_type': np.random.choice(property_types, n_samples),
        'square_footage': np.random.normal(1800, 600, n_samples),
        'bedrooms': np.random.choice([1, 2, 3, 4, 5], n_samples),
        'bathrooms': np.random.choice([1, 2, 3, 4], n_samples),
        'age': np.random.randint(1, 50, n_samples),
        'garage': np.random.choice([0, 1, 2], n_samples),
        'pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
        'garden': np.random.choice([0, 1], n_samples, p=[0.6, 0.4]),
        'latitude': np.random.uniform(40.7, 40.8, n_samples),
        'longitude': np.random.uniform(-74.0, -73.9, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Create realistic price based on features
    price_base = 200000
    location_multiplier = {'Downtown': 1.5, 'Suburb': 1.2, 'Urban': 1.3, 'Rural': 0.8, 'Coastal': 1.6}
    type_multiplier = {'Apartment': 0.8, 'House': 1.2, 'Condo': 1.0, 'Villa': 1.5}
    
    df['price'] = (
        price_base +
        df['square_footage'] * 150 +
        df['bedrooms'] * 20000 +
        df['bathrooms'] * 15000 +
        df['garage'] * 10000 +
        df['pool'] * 25000 +
        df['garden'] * 15000 +
        (50 - df['age']) * 2000 +
        np.random.normal(0, 30000, n_samples)
    )
    
    # Apply location and type multipliers
    df['price'] = df['price'] * df['location'].map(location_multiplier) * df['property_type'].map(type_multiplier)
    df['price'] = df['price'].clip(lower=100000)  # Minimum price
    
    return df

# Data preprocessing function
def preprocess_data(df):
    """Preprocess the dataset for model training"""
    # Handle missing values
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    
    # Encode categorical variables
    le_location = LabelEncoder()
    le_property_type = LabelEncoder()
    
    df_clean['location_encoded'] = le_location.fit_transform(df_clean['location'])
    df_clean['property_type_encoded'] = le_property_type.fit_transform(df_clean['property_type'])
    
    # Select features for modeling
    feature_columns = ['location_encoded', 'property_type_encoded', 'square_footage', 
                      'bedrooms', 'bathrooms', 'age', 'garage', 'pool', 'garden']
    
    X = df_clean[feature_columns]
    y = df_clean['price']
    
    return X, y, le_location, le_property_type, feature_columns

# Model training function
def train_models(X, y):
    """Train multiple regression models and return the best one"""
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize models
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    # Train and evaluate models
    results = {}
    trained_models = {}
    
    for name, model in models.items():
        # Create pipeline with scaling
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', model)
        ])
        
        # Train the model
        pipeline.fit(X_train, y_train)
        
        # Make predictions
        y_pred = pipeline.predict(X_test)
        
        # Calculate metrics
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            'RMSE': rmse,
            'MAE': mae,
            'R²': r2,
            'model': pipeline
        }
        
        trained_models[name] = pipeline
    
    # Find best model (lowest RMSE)
    best_model_name = min(results.keys(), key=lambda x: results[x]['RMSE'])
    best_model = results[best_model_name]['model']
    
    return trained_models, results, best_model_name, best_model

# Prediction function
def predict_price(model, features, feature_names):
    """Make price prediction using the trained model"""
    feature_array = np.array(features).reshape(1, -1)
    feature_df = pd.DataFrame(feature_array, columns=feature_names)
    prediction = model.predict(feature_df)[0]
    return prediction

# Main application
def main():
    st.markdown("<h1 class='main-header'>🏠 Real Estate Price Prediction Dashboard</h1>", unsafe_allow_html=True)
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data Analysis", "Model Training", "Price Prediction", "Batch Prediction"])
    
    # Load or generate data
    if st.sidebar.button("Load Sample Data"):
        df = generate_sample_data()
        st.session_state.data = df
        st.success("Sample data loaded successfully!")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload your dataset", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.data = df
        st.success("Data uploaded successfully!")
    
    # Main content based on page selection
    if page == "Home":
        home_page()
    elif page == "Data Analysis":
        if 'data' in st.session_state:
            data_analysis_page()
        else:
            st.warning("Please load data first!")
    elif page == "Model Training":
        if 'data' in st.session_state:
            model_training_page()
        else:
            st.warning("Please load data first!")
    elif page == "Price Prediction":
        if st.session_state.model_trained:
            prediction_page()
        else:
            st.warning("Please train a model first!")
    elif page == "Batch Prediction":
        if st.session_state.model_trained:
            batch_prediction_page()
        else:
            st.warning("Please train a model first!")

def home_page():
    st.markdown("<h2 class='sub-header'>Welcome to Real Estate Price Predictor</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    This dashboard provides a comprehensive solution for real estate price prediction using machine learning.
    
    ### Features:
    - **Interactive Data Analysis**: Explore your real estate dataset with visualizations
    - **Model Training**: Train and compare multiple regression models
    - **Real-time Predictions**: Get instant price predictions for individual properties
    - **Batch Processing**: Upload CSV files for bulk predictions
    - **Interactive Maps**: Visualize property locations and price trends
    
    ### How to Use:
    1. **Load Data**: Use the sidebar to upload your dataset or load sample data
    2. **Analyze**: Explore the data with built-in visualizations
    3. **Train Models**: Train multiple ML models and compare their performance
    4. **Predict**: Use the trained model to predict prices for new properties
    
    ### Get Started:
    Click on "Load Sample Data" in the sidebar to begin with a demonstration dataset!
    """)
    
    # Display sample data info if available
    if 'data' in st.session_state:
        st.markdown("### Current Dataset Info:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Records", len(st.session_state.data))
        with col2:
            st.metric("Features", len(st.session_state.data.columns) - 1)
        with col3:
            st.metric("Average Price", f"${st.session_state.data['price'].mean():,.0f}")

def data_analysis_page():
    st.markdown("<h2 class='sub-header'>📊 Data Analysis</h2>", unsafe_allow_html=True)
    
    df = st.session_state.data
    
    # Display basic statistics
    st.markdown("### Dataset Overview")
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(df.head())
    
    with col2:
        st.dataframe(df.describe())
    
    # Visualizations
    st.markdown("### Price Distribution")
    fig_hist = px.histogram(df, x='price', nbins=30, title='Price Distribution')
    st.plotly_chart(fig_hist, use_container_width=True)
    
    # Price by location
    st.markdown("### Price by Location")
    fig_box = px.box(df, x='location', y='price', title='Price Distribution by Location')
    st.plotly_chart(fig_box, use_container_width=True)
    
    # Correlation heatmap
    st.markdown("### Feature Correlations")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0
    ))
    fig_heatmap.update_layout(title='Feature Correlation Matrix')
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Interactive map
    if 'latitude' in df.columns and 'longitude' in df.columns:
        st.markdown("### Property Locations")
        
        # Create folium map
        center_lat = df['latitude'].mean()
        center_lon = df['longitude'].mean()
        
        m = folium.Map(location=[center_lat, center_lon], zoom_start=11)
        
        # Add markers for properties
        for idx, row in df.sample(100).iterrows():  # Sample 100 points for performance
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                popup=f"Price: ${row['price']:,.0f}<br>Location: {row['location']}<br>Bedrooms: {row['bedrooms']}",
                color='red',
                fill=True,
                fillColor='red'
            ).add_to(m)
        
        st_folium(m)

def model_training_page():
    st.markdown("<h2 class='sub-header'>🤖 Model Training</h2>", unsafe_allow_html=True)
    
    df = st.session_state.data
    
    if st.button("Train Models"):
        with st.spinner("Training models..."):
            # Preprocess data
            X, y, le_location, le_property_type, feature_names = preprocess_data(df)
            
            # Train models
            trained_models, results, best_model_name, best_model = train_models(X, y)
            
            # Store in session state
            st.session_state.models = trained_models
            st.session_state.model_results = results
            st.session_state.best_model = best_model
            st.session_state.best_model_name = best_model_name
            st.session_state.le_location = le_location
            st.session_state.le_property_type = le_property_type
            st.session_state.feature_names = feature_names
            st.session_state.model_trained = True
            
        st.success("Models trained successfully!")
        
        # Display results
        st.markdown("### Model Performance Comparison")
        
        results_df = pd.DataFrame(results).T
        results_df = results_df.drop('model', axis=1)  # Remove model column for display
        st.dataframe(results_df)
        
        # Best model highlight
        st.markdown(f"### 🏆 Best Model: {best_model_name}")
        best_metrics = results[best_model_name]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("RMSE", f"{best_metrics['RMSE']:,.0f}")
        with col2:
            st.metric("MAE", f"{best_metrics['MAE']:,.0f}")
        with col3:
            st.metric("R² Score", f"{best_metrics['R²']:.3f}")
        
        # Model comparison chart
        metrics_df = pd.DataFrame({
            'Model': list(results.keys()),
            'RMSE': [results[model]['RMSE'] for model in results.keys()],
            'MAE': [results[model]['MAE'] for model in results.keys()],
            'R²': [results[model]['R²'] for model in results.keys()]
        })
        
        fig_comparison = px.bar(metrics_df, x='Model', y='RMSE', title='Model RMSE Comparison')
        st.plotly_chart(fig_comparison, use_container_width=True)

def prediction_page():
    st.markdown("<h2 class='sub-header'>🎯 Price Prediction</h2>", unsafe_allow_html=True)
    
    # Input form
    st.markdown("### Enter Property Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.selectbox("Location", ['Downtown', 'Suburb', 'Urban', 'Rural', 'Coastal'])
        property_type = st.selectbox("Property Type", ['Apartment', 'House', 'Condo', 'Villa'])
        square_footage = st.number_input("Square Footage", min_value=500, max_value=5000, value=1800)
        bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
        bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
    
    with col2:
        age = st.number_input("Age (years)", min_value=0, max_value=100, value=10)
        garage = st.selectbox("Garage Spaces", [0, 1, 2])
        pool = st.selectbox("Pool", [0, 1])
        garden = st.selectbox("Garden", [0, 1])
    
    if st.button("Predict Price", type="primary"):
        # Encode categorical variables
        location_encoded = list(st.session_state.le_location.classes_).index(location)
        property_type_encoded = list(st.session_state.le_property_type.classes_).index(property_type)
        
        # Create feature array
        features = [location_encoded, property_type_encoded, square_footage, bedrooms, bathrooms, age, garage, pool, garden]
        
        # Make prediction
        predicted_price = predict_price(st.session_state.best_model, features, st.session_state.feature_names)
        
        # Display prediction
        st.markdown(f"""
        <div class='prediction-box'>
            <h2>Predicted Price</h2>
            <h1>${predicted_price:,.0f}</h1>
            <p>Based on {st.session_state.best_model_name} model</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional insights
        st.markdown("### Property Summary")
        summary_data = {
            'Feature': ['Location', 'Property Type', 'Square Footage', 'Bedrooms', 'Bathrooms', 'Age', 'Garage', 'Pool', 'Garden'],
            'Value': [location, property_type, f"{square_footage:,} sq ft", bedrooms, bathrooms, f"{age} years", garage, 'Yes' if pool else 'No', 'Yes' if garden else 'No']
        }
        st.table(pd.DataFrame(summary_data))

def batch_prediction_page():
    st.markdown("<h2 class='sub-header'>📋 Batch Prediction</h2>", unsafe_allow_html=True)
    
    st.markdown("### Upload CSV for Batch Predictions")
    st.markdown("Your CSV should contain columns: location, property_type, square_footage, bedrooms, bathrooms, age, garage, pool, garden")
    
    uploaded_file = st.file_uploader("Choose CSV file", type="csv")
    
    if uploaded_file is not None:
        # Load the data
        batch_df = pd.read_csv(uploaded_file)
        st.markdown("### Uploaded Data Preview")
        st.dataframe(batch_df.head())
        
        if st.button("Generate Predictions"):
            with st.spinner("Generating predictions..."):
                # Preprocess the batch data
                try:
                    batch_df['location_encoded'] = batch_df['location'].map(
                        {loc: i for i, loc in enumerate(st.session_state.le_location.classes_)}
                    )
                    batch_df['property_type_encoded'] = batch_df['property_type'].map(
                        {ptype: i for i, ptype in enumerate(st.session_state.le_property_type.classes_)}
                    )
                    
                    # Create features
                    feature_cols = ['location_encoded', 'property_type_encoded', 'square_footage', 
                                  'bedrooms', 'bathrooms', 'age', 'garage', 'pool', 'garden']
                    X_batch = batch_df[feature_cols]
                    
                    # Make predictions
                    predictions = st.session_state.best_model.predict(X_batch)
                    
                    # Add predictions to dataframe
                    batch_df['predicted_price'] = predictions
                    
                    st.success("Predictions generated successfully!")
                    
                    # Display results
                    st.markdown("### Prediction Results")
                    st.dataframe(batch_df[['location', 'property_type', 'square_footage', 'bedrooms', 'predicted_price']])
                    
                    # Download button
                    csv = batch_df.to_csv(index=False)
                    st.download_button(
                        label="Download Predictions CSV",
                        data=csv,
                        file_name="property_predictions.csv",
                        mime="text/csv"
                    )
                    
                    # Summary statistics
                    st.markdown("### Prediction Summary")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Properties", len(batch_df))
                    with col2:
                        st.metric("Average Predicted Price", f"${batch_df['predicted_price'].mean():,.0f}")
                    with col3:
                        st.metric("Price Range", f"${batch_df['predicted_price'].min():,.0f} - ${batch_df['predicted_price'].max():,.0f}")
                
                except Exception as e:
                    st.error(f"Error processing data: {str(e)}")
                    st.markdown("Please ensure your CSV has the correct column names and data types.")

if __name__ == "__main__":
    main()
