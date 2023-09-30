from flask import Flask

app = Flask(__name__) #if we want to make variables private we use double underscore for protected variable
                      # we use single underscore and for public we dont use any underscore

@app.route("/")
def home():
    return "Hello with flask" 


if __name__ == "__main__":  # it is written virtually mean it is already present in the code
    
    app.run(debug = True)

