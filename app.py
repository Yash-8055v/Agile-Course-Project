from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory store (kept simple for the mini project)
tasks = []
_next_id = 1


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def add_task():
    global _next_id
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify(error="title is required"), 400
    task = {"id": _next_id, "title": title, "done": False}
    _next_id += 1
    tasks.append(task)
    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def toggle_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            return jsonify(t)
    return jsonify(error="not found"), 404


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return "", 204
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
