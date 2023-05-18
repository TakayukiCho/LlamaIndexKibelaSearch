# create-index.py
import csv
from llama_index import GPTSimpleVectorIndex, SimpleWebPageReader
from llama_index.langchain_helpers.chatgpt import ChatGPTLLMPredictor

article_urls = []
with open('tmp/article-urls.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        article_urls.append(row[0])

documents = SimpleWebPageReader().load_data(article_urls)
index = GPTSimpleVectorIndex(documents=documents, llm_predictor=ChatGPTLLMPredictor()
)
index.save_to_disk('tmp/index.json')
