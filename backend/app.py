from flask import Flask, request, jsonify, send_file
import os
from .generator import generate_art

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.route("/")
def home():
    return jsonify({"message": "AI Art Generator Backend Running"})


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    prompt = data.get("prompt", "abstract art")
    width = int(data.get("width", 512))
    height = int(data.get("height", 512))
    seed = int(data.get("seed", 0))

    output_path = os.path.join(OUTPUT_DIR, "generated.png")

    generate_art(prompt, width, height, seed, output_path)

    return jsonify({
        "status": "success",
        "image_url": "/image"
    })


@app.route("/image", methods=["GET"])
def image():
    output_path = os.path.join(OUTPUT_DIR, "generated.png")
    if not os.path.exists(output_path):
        return jsonify({"error": "No image generated yet"}), 404
    return send_file(output_path, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
