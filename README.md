# Toxic_Classification


### Abstract 

In the era of widespread social media usage, individuals freely express their opinions online, yet this has led to a surge in conflicts and hate speech, creating unwelcoming digital environments. Despite recognizing hate as a pervasive issue across various platforms, there exists a dearth of effective models for detecting online hate. The prevalence of abusive language, aggression, and cyberbullying on social media platforms poses a significant threat, particularly affecting celebrities and influencers who endure hateful comments, potentially leading to mental health issues. 
To address this challenge, I aim to develop a prototype for an online hate and abuse comment classifier. This classifier aims to identify and tag comments containing offensive language, enabling better control and restriction of the spread of hatred and cyberbullying online. By leveraging machine learning, I aspire to create a tool that contributes to fostering a more positive and respectful online environment.
This indirectly would allow the users to flag those comments as bad or even report them if used in an inappropriate manner.. 


### Data Description 

The dataset comprises a training set with around 159,000 samples. Each data sample consists of eight fields:

1. Id: Unique identifiers associated with each comment text.
2. Comments: The actual comments extracted from various social media platforms.
3. Toxic: A binary label (0 or 1) indicating whether the comment is toxic or not.
4. Severe Toxic: Denotes comments that are highly malignant and hurtful.
5. Obscene: Indicates comments that are very rude and offensive.
6. Threat: Contains an indication of comments that involve giving threats to someone.
7. Insult: Pertains to comments that are abusive in nature.
8. Identity Hate: Describes comments that are hateful and express loathing.

The label column, "Toxic," plays a central role in classifying comments as either toxic (1) or non-toxic (0). Additionally, specific categories such as severe toxic, obscene, threat, insult, and identity hate provide further insights into the nature of offensive content within the dataset. The unique Ids associated with each comment text facilitate data organization and tracking. Overall, this dataset aims to support the development of models for identifying and categorizing offensive language in social media comments.

### Algorithm Description. 
//Outline the algorithm(s) driving your web app.
Tried to figure out which classifier is best for identifying Toxicity. Following are the classifiers which I tried -
1. Logistic Regression 
2. BernoulliNB
3. MultinomialNB
4. LinearSVC

Calculated the metrics for each classifier -
![image](https://github.com/AmrithaP/Toxic_Classification/assets/52408359/a572f2eb-1c21-4381-97e2-7910e58be55b)

From above Table and comparison between various classifiers, am going to take in LinearSVC classifier for being the best when compared among others for the performance of the model.

#### Algo for LinearSVC 
1. Data Preprocessing:
- Load and explore the dataset.
- Handle missing data if any.
- Tokenize the text data into words or subword tokens.
- Remove stop words, punctuation, and irrelevant characters.
- Convert text data into numerical representations using techniques like TF-IDF or word embeddings (e.g., Word2Vec, GloVe).

2. Data Splitting:
- Split the dataset into training and testing sets.

3. Model Initialization:
- Initialize the Linear Support Vector Classifier with the desired parameters.
- Choose a linear kernel since it's suitable for text classification.

4. Feature Extraction:
- Convert the preprocessed text data into a feature matrix.
- If using TF-IDF, transform the text data into numerical feature vectors.

5. Model Training:
- Train the Linear SVC using the training set.
- Adjust hyperparameters if necessary, such as the regularization parameter (C).

6. Model Evaluation:
- Evaluate the model on the testing set to assess its performance.
- Use metrics such as accuracy, precision, recall, and F1-score.

7. Hyperparameter Tuning (Optional):

- Fine-tune hyperparameters, such as the regularization parameter (C), to optimize model performance.

8. Prediction:
- Make predictions on new or unseen text data using the trained Linear SVC.
Model Interpretation (Optional):

9. Deployment (Optional):
- If satisfied with the model performance, deploy the Linear SVC for making real-world predictions.

### Tools Used:
1. Python: The primary programming language used for the entire project, including data preprocessing, model development, and evaluation.
2. Pandas: Employed for data manipulation and exploration, allowing seamless handling of the dataset and extraction of meaningful insights.
3. Scikit-learn: Utilized for implementing machine learning algorithms, model training, and performance evaluation. Scikit-learn provides a comprehensive set of tools for data mining and data analysis.
4. NLTK (Natural Language Toolkit): Incorporated for text data preprocessing, including tokenization, removal of stop words, and other essential natural language processing tasks.\
5. Matplotlib and Seaborn: These visualization libraries were used to create insightful graphs and charts, aiding in the interpretation of model performance metrics.
6. Jupyter Notebooks: Facilitated an interactive and collaborative development environment, enabling a step-by-step walkthrough of the project, from data exploration to model training.
7. Linear Support Vector Classifier (LinearSVC): Selected as the final classifier due to its superior performance, this tool plays a crucial role in accurately identifying and categorizing toxic comments.
8. TF-IDF (Term Frequency-Inverse Document Frequency): Employed as a feature extraction technique to convert text data into numerical representations, enhancing the model's ability to understand and classify toxic comments.
9. GitHub: Used for version control and collaborative development, ensuring project integrity and providing a platform for seamless collaboration.
10. Web App Development Tools (if applicable): Streamlit tool was used for developing the web application for hosting the toxic comment classifier.

By leveraging these tools, the project was able to efficiently address the challenges posed by toxic comments in social media, providing a comprehensive solution with a focus on model accuracy and interpretability.

### Application Link - 

URL : https://toxic-classification.streamlit.app/
