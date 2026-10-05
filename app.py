from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import get_connection

app = Flask(__name__)


def get_all_jobs():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM applications ORDER BY id DESC")
    jobs = cur.fetchall()
    cur.close()
    conn.close()
    return jobs


def add_job_to_db(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO applications
        (company, role, location, salary, applied_date, status)
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (data["company"], data["role"], data["location"], data["salary"],
         data["applied_date"], data["status"]))
    conn.commit()
    cur.close()
    conn.close()


def get_job(job_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM applications WHERE id=%s", (job_id,))
    job = cur.fetchone()
    cur.close()
    conn.close()
    return job


def update_job_in_db(job_id, data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""UPDATE applications SET company=%s, role=%s, location=%s,
        salary=%s, applied_date=%s, status=%s WHERE id=%s""",
        (data["company"], data["role"], data["location"], data["salary"],
         data["applied_date"], data["status"], job_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_job_from_db(job_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM applications WHERE id=%s", (job_id,))
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def index():
    jobs = get_all_jobs()
    return render_template("index.html", jobs=jobs)


@app.route("/add", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        add_job_to_db(request.form)
        return redirect(url_for("index"))
    return render_template("add_job.html")


@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    if request.method == "POST":
        update_job_in_db(job_id, request.form)
        return redirect(url_for("index"))
    job = get_job(job_id)
    return render_template("edit_job.html", job=job)


@app.route("/delete/<int:job_id>")
def delete_job(job_id):
    delete_job_from_db(job_id)
    return redirect(url_for("index"))


@app.route("/api/jobs", methods=["GET"])
def api_get_jobs():
    return jsonify(get_all_jobs())


@app.route("/api/jobs", methods=["POST"])
def api_add_job():
    data = request.get_json()
    add_job_to_db(data)
    return jsonify({"message": "Application added"}), 201


@app.route("/api/jobs/<int:job_id>", methods=["PUT"])
def api_update_job(job_id):
    data = request.get_json()
    update_job_in_db(job_id, data)
    return jsonify({"message": "Application updated"})


@app.route("/api/jobs/<int:job_id>", methods=["DELETE"])
def api_delete_job(job_id):
    delete_job_from_db(job_id)
    return jsonify({"message": "Application deleted"})


if __name__ == "__main__":
    app.run(debug=True)
