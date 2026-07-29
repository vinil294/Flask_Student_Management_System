from flask import Flask,render_template,request,flash,get_flashed_messages,redirect,url_for
import database as dt
app = Flask(__name__)
dt.create_database()
app.secret_key="Register_key"
#-----Dashboard-----
@app.route('/')
@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    total=dt.total_students()
    return render_template('dashboard.html')
#---Register---
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=="POST":
        name=request.form.get('name').strip().upper()
        roll_no=request.form.get('roll_no').strip().upper()
        branch=request.form.get('branch').strip().upper()
        try:
          cgpa=float(request.form.get('cgpa'))
        except ValueError:
            flash('Invalid CGPA Format')
            return render_template('register.html',name=name,roll_no=roll_no,branch=branch)
        if cgpa < 0 and cgpa >10:
            flash("CGPA must be between 0 and 10")
            return render_template("register.html")
        try:
            dt.insert_student(name,roll_no,branch,cgpa)
            flash('Successfully registered')
            return redirect(url_for('view'))
        except sqlite3.IntegrityError:
            flash('Student Already Exists')
    return render_template('register.html')
#---view----
@app.route('/view',methods=['GET','POST'])
def view():
    students=dt.view_student()
    return render_template('view.html',result=students)
#---search----
@app.route('/search',methods=['GET','POST'])
def search():
    student=None
    if request.method=="POST":
        roll_no=request.form.get('roll_no').strip().upper()
        student=dt.search_student(roll_no)
        if  not student:
            flash('No student found')
    return render_template('search.html',student=student)
#--Delete----
@app.route("/delete",methods=['GET','POST'])
def delete():
    if request.method=="POST":
        student_roll=request.form.get('student_roll').strip().upper()
        student=dt.delete_student(student_roll)
        if student:
            dt.delete_student(student_roll)
            flash(' Student Deleted Successfully ')
        else:
            flash('Student Not Found')
    return redirect(url_for('view'))
# ---------------- Update ---------------- #
@app.route("/update/<int:student_id>", methods=["GET", "POST"])
def update(student_id):
    student = dt.get_student_by_id(student_id)
    if student is None:
        flash("Student Not Found")
        return redirect(url_for("view"))
    if request.method == "POST":
        name = request.form.get("name").strip().upper()
        roll_no = request.form.get("roll_no").strip().upper()
        branch = request.form.get("branch").strip().upper()
        try:
            cgpa = float(request.form.get("cgpa"))
        except ValueError:
            flash("Invalid CGPA")
            return render_template(
                "update.html",student=student)
        if cgpa < 0 or cgpa > 10:
            flash("CGPA must be between 0 and 10")
            return render_template(
                "update.html",student=student)
        try:
            dt.update_student(student_id,name,roll_no,cgpa)
            flash("Student Updated Successfully")
            return redirect(url_for("view"))
        except sqlite3.IntegrityError:
            flash("Roll Number Already Exists")
            return render_template("update.html",student=student)
    return render_template("update.html",student=student)
if __name__=='__main__':
    app.run(debug=True)
