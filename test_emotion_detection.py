import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        # Statement 1: Joy
        res1 = emotion_detector("I am glad this happened")
        self.assertEqual(res1["dominant_emotion"], "joy")

        # Statement 2: Anger
        res2 = emotion_detector("I am really angry about this")
        self.assertEqual(res2["dominant_emotion"], "anger")

        # Statement 3: Disgust
        res3 = emotion_detector("I feel disgusted just thinking about this")
        self.assertEqual(res3["dominant_emotion"], "disgust")

        # Statement 4: Sadness
        res4 = emotion_detector("I am so sad about this")
        self.assertEqual(res4["dominant_emotion"], "sadness")

        # Statement 5: Fear
        res5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res5["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()