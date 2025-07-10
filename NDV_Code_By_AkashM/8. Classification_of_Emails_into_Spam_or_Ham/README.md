📧 Classification of Emails into Spam or Ham

📝 Overview
    This project demonstrates text classification of SMS messages as spam or ham (not spam) using machine learning models. It includes preprocessing, feature extraction, model training, evaluation, and hyperparameter tuning.

🎯 Objectives
    Clean and prepare text data

    Convert messages into numerical features using CountVectorizer

    Train classification models:

    Logistic Regression

    Random Forest

    Evaluate and compare model performance

    Visualize results (Confusion Matrix, ROC Curve, Feature Importance)

📂 Dataset
    SMSSpamCollection
    Format: Tab-separated text file with two columns:
    label: "spam" or "ham"
    message: SMS content

⚙️ Workflow
    **Load Data**
    **Read dataset and display sample rows**
    **Preprocessing**
    **Label encoding: Convert labels to numeric (spam = 1, ham = 0)**
    **Text vectorization with CountVectorizer**
    **Train/Test Split**
    **80% training, 20% testing**
    **Model Training**
    **Logistic Regression (max_iter=1000)**
    **Random Forest Classifier**
    **Evaluation Metrics**
    **Accuracy, Precision, Recall, F1 Score**
    **Classification report**
    **Confusion Matrix visualization**
    **ROC Curve plotting**
    **Hyperparameter Tuning**
    **GridSearchCV to optimize Random Forest parameters**
    **Feature Importance**
    **Display top 10 most significant words in classification**

🚀 How to Run
    Note: This project was tested in Google Colab.

    1️⃣ Upload the SMSSpamCollection dataset
    2️⃣ Run each notebook cell in sequence
    3️⃣ Models are trained and evaluated automatically
    4️⃣ Review metrics and plots for insights

📊 Key Results
    Both Logistic Regression and Random Forest achieved high classification performance.
    The optimized Random Forest (via GridSearchCV) provided robust results.

Important features (top indicative words) were visualized to understand model decisions.

🛠️ Dependencies
    scikit-learn
    pandas
    numpy
    matplotlib
    seaborn

📁 Files
    Classification_of_Emails.ipynb: Main notebook containing all code
    SMSSpamCollection: Dataset file

✅ Conclusion
    This project illustrates an end-to-end workflow to classify messages as spam or ham using machine learning techniques and feature importance analysis.