from flask import Flask, jsonify, request
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route("/add-name", methods=["POST"])
def add_name():
    data = request.get_json()
    name = data.get("name")

    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO names (name) VALUES (%s) RETURNING id, created_at;",
            (name,)
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return jsonify(
            message=f"Name \'{name}\' inserted successfully",
            id=row[0],
            created_at=row[1].isoformat()
        ), 201
    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route("/delete-name/<string:name>", methods=["DELETE"])
def delete_name(name):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("DELETE FROM names WHERE name = %s RETURNING id;", (name,))
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if deleted:
            return jsonify(message=f'Name "{name}" deleted'), 200
        else:
            return jsonify(error=f'No entry found with name "{name}"'), 404
    except Exception as e:
        return jsonify(error=str(e)), 500

    
@app.route("/names", methods=["GET"])
def get_names():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT * FROM names;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        names = [{"id": r[0], "name": r[1], "created_at": r[2].isoformat()} for r in rows]
        return jsonify(names=names)
    except Exception as e:
        return jsonify(error=str(e)), 500


