from flask import Flask, render_template

app = Flask('')

@app.route('/')
def main():
  return 'hi'

def run():
  app.run(host="0.0.0.0", port=3064)