import random

def generate_questions(skills):

    questions = []

    question_bank = {

        "python": [

            "Explain Object Oriented Programming in Python.",

            "What is the difference between list and tuple?",

            "Explain Python decorators.",

            "What are lambda functions in Python?",

            "What is the use of NumPy in Python?"
        ],

        "sql": [

            "What is the difference between INNER JOIN and LEFT JOIN?",

            "What are primary keys and foreign keys?",

            "Explain normalization in SQL.",

            "What is the difference between DELETE and TRUNCATE?",

            "What is indexing in databases?"
        ],

        "machine learning": [

            "What is overfitting in Machine Learning?",

            "Explain supervised and unsupervised learning.",

            "What is the difference between classification and regression?",

            "What is cross validation?",

            "Explain bias and variance."
        ],

        "deep learning": [

            "What is Deep Learning?",

            "Explain CNN and its applications.",

            "What is backpropagation?",

            "What are activation functions?",

            "What is gradient descent?"
        ],

        "tensorflow": [

            "Explain neural networks.",

            "What is TensorFlow used for?",

            "What is a tensor?",

            "Explain Keras in TensorFlow.",

            "What is GPU acceleration in TensorFlow?"
        ],

        "pandas": [

            "What is a DataFrame in Pandas?",

            "Explain groupby() in Pandas.",

            "How do you handle missing values?",

            "Difference between loc and iloc?",

            "How to merge datasets in Pandas?"
        ],

        "numpy": [

            "What is NumPy?",

            "Difference between NumPy arrays and Python lists?",

            "Explain vectorization in NumPy.",

            "What are NumPy dimensions?",

            "What is broadcasting in NumPy?"
        ],

        "data science": [

            "Explain the Data Science lifecycle.",

            "What is data preprocessing?",

            "Explain feature engineering.",

            "What is exploratory data analysis?",

            "Why is data cleaning important?"
        ],

        "power bi": [

            "What is Power BI?",

            "Explain dashboards in Power BI.",

            "What are KPIs?",

            "Difference between report and dashboard?",

            "What is DAX in Power BI?"
        ],

        "excel": [

            "What are pivot tables in Excel?",

            "Explain VLOOKUP.",

            "What are Excel macros?",

            "Difference between COUNT and COUNTA?",

            "Explain conditional formatting."
        ],

        "java": [

            "What is JVM?",

            "Explain inheritance in Java.",

            "What is polymorphism?",

            "Difference between JDK and JRE?",

            "Explain exception handling in Java."
        ],

        "c++": [

            "What is object oriented programming in C++?",

            "Explain constructors and destructors.",

            "What is function overloading?",

            "Difference between stack and heap memory?",

            "Explain pointers in C++."
        ]
    }

    for skill in skills:

        skill = skill.lower()

        if skill in question_bank:

            random_questions = random.sample(
                question_bank[skill],
                min(3, len(question_bank[skill]))
            )

            questions.extend(random_questions)

    return questions