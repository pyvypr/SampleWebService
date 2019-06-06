from app import app
import datetime
import time

def f(l):
  for item in l:
    time.sleep(0.1)

@app.route('/paths_branching_test/<int:n>/', methods=["GET", "POST"])
def paths_branching_test(n):
  if n > 10:
    l = []
    for i in range(n):
      l.append(i**2)
  else:
    l = []
  f(l)
  return "function for experiments"

@app.route("/", methods=["GET"])
def index():
  return "home page"
