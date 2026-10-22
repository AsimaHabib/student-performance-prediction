
from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake database
students = [
    {"id": 1, "name": "Ali", "grade": "A"},
    {"id": 2, "name": "Sara", "grade": "B"}
]


# Home route
@app.route('/')
def home():
    return "Welcome to Students API!"


# Get all students
@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students)


# Get one student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_one_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


# Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error": "name is required"}), 400

    new_student = {
        "id": max((s["id"] for s in students), default=0) + 1,
        "name": data["name"],
        "grade": data.get("grade", "N/A")
    }

    students.append(new_student)

    return jsonify(new_student), 201


# Update a student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json() or {}

    for student in students:
        if student["id"] == student_id:
            student["name"] = data.get(
                "name", student["name"]
            )
            student["grade"] = data.get(
                "grade", student["grade"]
            )

            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for i, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(i)

            return jsonify({
                "message": f"Student {student_id} deleted"
            })

    return jsonify({"error": "Student not found"}), 404


# Start Flask server
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
