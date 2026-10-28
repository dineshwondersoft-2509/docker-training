from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from the Docker API",
        "status": "running"
    })

@app.route("/db")
def database_test():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "trainingdb"),
            user=os.getenv("DB_USER", "traininguser"),
            password=os.getenv("DB_PASSWORD", "trainingpass")
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]

        cur.close()
        conn.close()

        return jsonify({
            "database": "connected",
            "version": version
        })

    except Exception as e:
        return jsonify({
            "database": "failed",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)