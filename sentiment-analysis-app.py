from transformers import pipeline
classifier = pipeline("sentiment-analysis")
def func(utterance):
  return classifier(utterance)
import gradio as gr
descriptions = "This is an AI sentiment analyser which checks and get the emotions in a particular utterance. Just put in a sentence and you'll get the probable emotions behind that sentence"

app = gr.Interface(fn=func, inputs="text", outputs="text", title="Sentiment Analayser", description=descriptions)
app.launch()