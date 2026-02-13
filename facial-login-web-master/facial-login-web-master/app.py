from keras_server import app, load_FRmodel, ini_user_database

if __name__ == "__main__":
    print("Initializing model and user database...")
    try:
        load_FRmodel()
    except Exception as e:
        print(f"Model load failed: {e}")
    try:
        ini_user_database()
    except Exception as e:
        print(f"User DB init failed: {e}")
    app.run(debug=True)
