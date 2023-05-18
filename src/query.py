# query.py
import readline
from llama_index import LLMPredictor, ServiceContext, StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI

...

# define LLM
llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

# rebuild storage context
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
storage_context = StorageContext.from_defaults(persist_dir="./tmp")
# load index
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine(service_context=service_context)
name = input('質問の内容をいかに記載してください。\n > ')
answer = query_engine.query(name)
print(answer)
