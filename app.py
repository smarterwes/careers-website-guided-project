from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York City, USA',
    'salary': '$200,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Moscow, ID',
    'salary': '$220,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'San Francisco, CA',
  },
  {
    'id': 4,
    'title': 'Fullstack Westimator',
    'location': 'Austin, TX',
    'salary': '$245,000'
  }  
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                         company_name='@SmarterWes')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
  