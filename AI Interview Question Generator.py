import streamlit as st
import random
import time

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Interview Generator",
    page_icon="🎯",
    layout="wide"
)

# ============================================================
# QUESTION DATABASE
# ============================================================

QUESTIONS = {

    "Python": {

        "Easy": [
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "answer": "def",
                "explanation": "Python uses the 'def' keyword to define functions."
            },
            {
                "question": "Which data type is immutable?",
                "options": ["List", "Dictionary", "Set", "Tuple"],
                "answer": "Tuple",
                "explanation": "Tuples are immutable collections."
            },
            {
                "question": "What is the output of len('Python')?",
                "options": ["5", "6", "7", "Error"],
                "answer": "6",
                "explanation": "Python has six characters."
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#",
                "explanation": "Python uses # for single-line comments."
            }
        ],

        "Medium": [
            {
                "question": "What is the average time complexity of dictionary lookup in Python?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "answer": "O(1)",
                "explanation": "Python dictionaries use hash tables and provide average O(1) lookup."
            },
            {
                "question": "What does list comprehension primarily provide?",
                "options": [
                    "Database access",
                    "Compact list creation",
                    "Memory allocation",
                    "Multithreading"
                ],
                "answer": "Compact list creation",
                "explanation": "List comprehensions provide a concise way to create lists."
            },
            {
                "question": "Which keyword handles exceptions?",
                "options": ["catch", "except", "error", "handle"],
                "answer": "except",
                "explanation": "Python uses try/except for exception handling."
            }
        ],

        "Hard": [
            {
                "question": "What is a Python generator?",
                "options": [
                    "A function that uses yield",
                    "A compiler",
                    "A database",
                    "A class decorator"
                ],
                "answer": "A function that uses yield",
                "explanation": "Generators use yield to produce values lazily."
            },
            {
                "question": "What does the GIL primarily affect?",
                "options": [
                    "Python syntax",
                    "CPython thread execution",
                    "Database queries",
                    "File compression"
                ],
                "answer": "CPython thread execution",
                "explanation": "The Global Interpreter Lock affects execution of Python bytecode in CPython threads."
            }
        ]
    },

    "Data Structures": {

        "Easy": [
            {
                "question": "Which data structure follows FIFO?",
                "options": ["Stack", "Queue", "Tree", "Graph"],
                "answer": "Queue",
                "explanation": "FIFO means First In First Out, which is the behavior of a queue."
            },
            {
                "question": "Which data structure follows LIFO?",
                "options": ["Queue", "Stack", "Array", "Graph"],
                "answer": "Stack",
                "explanation": "LIFO means Last In First Out."
            },
            {
                "question": "Which structure uses nodes and edges?",
                "options": ["Array", "Graph", "Stack", "Queue"],
                "answer": "Graph",
                "explanation": "Graphs consist of vertices/nodes connected by edges."
            }
        ],

        "Medium": [
            {
                "question": "What is the average search complexity in a balanced BST?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(log n)",
                "explanation": "A balanced binary search tree reduces the search space by half."
            },
            {
                "question": "Which traversal uses a queue?",
                "options": [
                    "DFS",
                    "BFS",
                    "Inorder",
                    "Postorder"
                ],
                "answer": "BFS",
                "explanation": "Breadth First Search typically uses a queue."
            }
        ],

        "Hard": [
            {
                "question": "What is the worst-case complexity of Quick Sort?",
                "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                "answer": "O(n²)",
                "explanation": "Poor pivot selection can cause Quick Sort to degrade to O(n²)."
            }
        ]
    },

    "DBMS": {

        "Easy": [
            {
                "question": "What does SQL stand for?",
                "options": [
                    "Structured Query Language",
                    "Simple Query Language",
                    "System Query Logic",
                    "Structured Question Language"
                ],
                "answer": "Structured Query Language",
                "explanation": "SQL stands for Structured Query Language."
            },
            {
                "question": "Which command is used to retrieve data?",
                "options": ["GET", "SELECT", "FETCH", "READ"],
                "answer": "SELECT",
                "explanation": "SELECT retrieves records from a database."
            }
        ],

        "Medium": [
            {
                "question": "Which normal form removes partial dependency?",
                "options": ["1NF", "2NF", "3NF", "BCNF"],
                "answer": "2NF",
                "explanation": "Second Normal Form removes partial functional dependency."
            },
            {
                "question": "Which key uniquely identifies a row?",
                "options": [
                    "Foreign Key",
                    "Primary Key",
                    "Candidate Key",
                    "Composite Key"
                ],
                "answer": "Primary Key",
                "explanation": "A primary key uniquely identifies each row."
            }
        ],

        "Hard": [
            {
                "question": "Which property means a transaction is completed entirely or not at all?",
                "options": [
                    "Consistency",
                    "Isolation",
                    "Atomicity",
                    "Durability"
                ],
                "answer": "Atomicity",
                "explanation": "Atomicity guarantees all-or-nothing transaction execution."
            }
        ]
    },

    "Machine Learning": {

        "Easy": [
            {
                "question": "Which type of learning uses labeled data?",
                "options": [
                    "Unsupervised Learning",
                    "Supervised Learning",
                    "Reinforcement Learning",
                    "Random Learning"
                ],
                "answer": "Supervised Learning",
                "explanation": "Supervised learning trains models using labeled examples."
            },
            {
                "question": "Which algorithm is commonly used for classification?",
                "options": [
                    "Linear Regression",
                    "Logistic Regression",
                    "K-Means",
                    "PCA"
                ],
                "answer": "Logistic Regression",
                "explanation": "Logistic Regression is commonly used for binary classification."
            }
        ],

        "Medium": [
            {
                "question": "What is overfitting?",
                "options": [
                    "Model performs poorly on training data",
                    "Model memorizes training data and performs poorly on unseen data",
                    "Model has no parameters",
                    "Model has no features"
                ],
                "answer": "Model memorizes training data and performs poorly on unseen data",
                "explanation": "Overfitting occurs when a model learns training-specific patterns too closely."
            },
            {
                "question": "Which technique can reduce overfitting?",
                "options": [
                    "Regularization",
                    "Removing all data",
                    "Increasing noise",
                    "Removing validation"
                ],
                "answer": "Regularization",
                "explanation": "Regularization penalizes overly complex models."
            }
        ],

        "Hard": [
            {
                "question": "What is the purpose of gradient descent?",
                "options": [
                    "Increase model size",
                    "Minimize a loss function",
                    "Remove labels",
                    "Create databases"
                ],
                "answer": "Minimize a loss function",
                "explanation": "Gradient descent updates parameters to minimize the objective/loss function."
            }
        ]
    }
}

# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

INTERVIEW_QUESTIONS = {

    "Python": [
        "Explain the difference between a list and a tuple.",
        "What are decorators in Python?",
        "Explain shallow copy vs deep copy.",
        "What are generators and why are they useful?",
        "Explain exception handling in Python.",
        "What is the difference between == and is?",
        "Explain Python's memory management.",
        "What is the Global Interpreter Lock?"
    ],

    "Data Structures": [
        "Explain the difference between a stack and a queue.",
        "What is the difference between an array and a linked list?",
        "Explain binary search and its complexity.",
        "What is a hash table?",
        "Explain BFS and DFS.",
        "What is a binary search tree?",
        "Explain recursion with an example.",
        "What is dynamic programming?"
    ],

    "DBMS": [
        "What is normalization?",
        "Explain primary key and foreign key.",
        "What are ACID properties?",
        "What is indexing?",
        "Explain SQL joins.",
        "What is a transaction?",
        "Difference between DELETE, DROP and TRUNCATE.",
        "What is database normalization?"
    ],

    "Machine Learning": [
        "What is supervised learning?",
        "Explain overfitting and underfitting.",
        "What is cross-validation?",
        "Explain precision and recall.",
        "What is gradient descent?",
        "What is feature engineering?",
        "Explain classification vs regression.",
        "What is regularization?"
    ]
}

# ============================================================
# SESSION STATE
# ============================================================

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "interview_question" not in st.session_state:
    st.session_state.interview_question = ""

# ============================================================
# HEADER
# ============================================================

st.title("🎯 AI Interview Question Generator")

st.write(
    "Practice technical interviews, MCQs and "
    "role-based questions in one place."
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Interview Setup")

    topic = st.selectbox(
        "Choose Topic",
        list(QUESTIONS.keys())
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    number_questions = st.slider(
        "Number of Questions",
        1,
        10,
        5
    )

# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3 = st.tabs(
    [
        "📝 MCQ Practice",
        "🎤 Interview Mode",
        "📊 Performance"
    ]
)

# ============================================================
# MCQ TAB
# ============================================================

with tab1:

    st.header("📝 Technical MCQ Practice")

    if st.button(
        "🚀 Generate Quiz",
        type="primary"
    ):

        available = QUESTIONS[
            topic
        ][difficulty]

        count = min(
            number_questions,
            len(available)
        )

        st.session_state.quiz_questions = random.sample(
            available,
            count
        )

        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.session_state.answered = False

    if st.session_state.quiz_questions:

        questions = st.session_state.quiz_questions

        index = st.session_state.quiz_index

        if index < len(questions):

            q = questions[index]

            st.progress(
                index / len(questions)
            )

            st.subheader(
                f"Question {index + 1} / {len(questions)}"
            )

            st.write(
                f"### {q['question']}"
            )

            answer = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"question_{index}"
            )

            if st.button(
                "Submit Answer",
                key=f"submit_{index}"
            ):

                if answer == q["answer"]:

                    st.success(
                        "✅ Correct!"
                    )

                    st.session_state.score += 1

                else:

                    st.error(
                        f"❌ Incorrect. Correct answer: "
                        f"{q['answer']}"
                    )

                st.info(
                    q["explanation"]
                )

                st.session_state.answered = True

            if st.session_state.answered:

                if st.button(
                    "Next Question →",
                    key=f"next_{index}"
                ):

                    st.session_state.quiz_index += 1
                    st.session_state.answered = False
                    st.rerun()

        else:

            final_score = st.session_state.score

            total = len(questions)

            percentage = int(
                final_score / total * 100
            )

            st.balloons()

            st.success(
                f"🎉 Quiz Completed!"
            )

            st.metric(
                "Final Score",
                f"{final_score}/{total}"
            )

            st.progress(
                percentage / 100
            )

            st.write(
                f"Accuracy: **{percentage}%**"
            )

            if percentage >= 80:

                st.success(
                    "🔥 Excellent performance!"
                )

            elif percentage >= 60:

                st.warning(
                    "👍 Good performance. Keep practicing."
                )

            else:

                st.error(
                    "📚 Revise the topic and try again."
                )

# ============================================================
# INTERVIEW MODE
# ============================================================

with tab2:

    st.header("🎤 Interview Mode")

    st.write(
        "Practice answering real interview-style questions."
    )

    interview_topic = st.selectbox(
        "Interview Topic",
        list(INTERVIEW_QUESTIONS.keys()),
        key="interview_topic"
    )

    if st.button(
        "🎲 Generate Interview Question"
    ):

        st.session_state.interview_question = random.choice(
            INTERVIEW_QUESTIONS[interview_topic]
        )

    if st.session_state.interview_question:

        st.info(
            st.session_state.interview_question
        )

        answer = st.text_area(
            "Your Answer",
            height=180,
            placeholder="Type your interview answer here..."
        )

        if st.button(
            "Evaluate My Answer"
        ):

            if len(answer.strip()) < 30:

                st.warning(
                    "Your answer is too short. "
                    "Try explaining the concept with an example."
                )

            else:

                words = len(answer.split())

                if words >= 100:

                    score = random.randint(80, 95)

                elif words >= 60:

                    score = random.randint(65, 80)

                else:

                    score = random.randint(50, 65)

                st.metric(
                    "Answer Score",
                    f"{score}/100"
                )

                if score >= 80:

                    st.success(
                        "Strong answer. Good explanation and detail."
                    )

                elif score >= 60:

                    st.warning(
                        "Decent answer. Add examples and technical details."
                    )

                else:

                    st.error(
                        "Needs improvement. Explain the concept more clearly."
                    )

                st.write(
                    "### 💡 Interview Tip"
                )

                st.write(
                    "Use this structure:"
                )

                st.write(
                    "1. Definition → 2. Explanation → "
                    "3. Example → 4. Complexity / Advantage"
                )

# ============================================================
# PERFORMANCE TAB
# ============================================================

with tab3:

    st.header("📊 Performance Dashboard")

    score = st.session_state.score

    if st.session_state.quiz_questions:

        total = len(
            st.session_state.quiz_questions
        )

        st.metric(
            "Current Score",
            f"{score}/{total}"
        )

        if total > 0:

            accuracy = (
                score / total
            ) * 100

            st.metric(
                "Accuracy",
                f"{accuracy:.0f}%"
            )

            st.progress(
                accuracy / 100
            )

    else:

        st.info(
            "Complete a quiz to see your performance."
        )

    st.divider()

    st.subheader("🎯 Preparation Tips")

    tips = [
        "Understand concepts instead of memorizing answers.",
        "Practice coding problems every day.",
        "Explain your projects clearly.",
        "Learn time and space complexity.",
        "Practice speaking your answers aloud.",
        "Review mistakes after every test."
    ]

    for tip in tips:

        st.write(
            f"• {tip}"
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Interview Question Generator • "
    "Python + Streamlit"
)
