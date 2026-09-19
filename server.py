"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the requested text and return a formatted string.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    # Task 7: Handling blank or invalid input
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': "
        f"{response['fear']}, 'joy': {response['joy']} and 'sadness': "
        f"{response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)