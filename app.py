from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Frontend Engineer',
  'location': 'Lagos, Nigeria',
  'salary': '#250,000'
}, {
  'id': 2,
  'title': 'Backend Engineer',
  'location': 'Abuja, Nigeria',
  'salary': '#600,000'
}, {
  'id': 3,
  'title': 'Data Scientist',
  'location': 'Portharcut, Nigeria',
  'salary': '#300,000'
}, {
  'id': 4,
  'title': 'Data Analyst',
  'location': 'Benue, Nigeria',
  'salary': '#320,000'
}]


@app.route("/")
def Hello_World():
  return render_template('home.html', jobs=JOBS, company_name='V')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
