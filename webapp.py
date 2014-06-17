from flask import Flask, render_template, request #import Flask class
import hackbright_app

app = Flask(__name__) # instance of Flask class

@app.route("/")
def get_github():
    return render_template("get_github.html")


@app.route("/student") # route() is a decorator that tells Flask what URL should trigger function
def get_student(): # function name
    hackbright_app.connect_to_db()
    student_github = request.args.get("student") #getting key:value from url
    row = hackbright_app.get_student_by_github(student_github)
    html = render_template("student_info.html", first_name = row[0], # render_template(name_template_file, values_to_fill)
                                                last_name = row[1],
                                                github = row[2])
    return html

@app.route("/grade")
def get_grade():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    rows = hackbright_app.get_grades_by_student(student_github)
    projects = []
    for title, grade in rows:
        row_dict = {}
        row_dict['project_title'] = title
        row_dict['grade'] = grade
        projects.append(row_dict)
    print projects
    html = render_template("grade_info.html", projects = projects)
    return html



#     def get_grades_by_student(github):
#     query = """SELECT project_title, grade FROM Grades WHERE student_github = ?"""
#     DB.execute(query, (github,))
#     row = DB.fetchone()
#     return"""\
# Student: %s
# Project Grade: %s: %d""" % (github, row[0], row[1])
    

if __name__ == "__main__":
    app.run(debug=True) # .run() function runs the local server, in debug mode