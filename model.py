import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Read dataset
data = pd.read_csv(
    "data/student_data.csv"
)


# Inputs
X = data[
    [
        'Hours_Studied',
        'Attendance',
        'Previous_Marks',
        'Assignments_Submitted'
    ]
]


# Output
y = data['Grade']


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = KNeighborsClassifier(
    n_neighbors=3
)


# Train model
model.fit(
    X_train,
    y_train
)

student = pd.DataFrame(
    [[5,90,80,8]],
    columns=[
        'Hours_Studied',
        'Attendance',
        'Previous_Marks',
        'Assignments_Submitted'
    ]
)

prediction = model.predict(student)

print(
    "Predicted Grade:",
    prediction[0]
)