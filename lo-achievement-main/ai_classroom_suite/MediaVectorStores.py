# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/media_stores.ipynb.

# %% auto 0
__all__ = ['rawtext_to_doc_split', 'files_to_text', 'youtube_to_text', 'save_text', 'get_youtube_transcript',
           'website_to_text_web', 'website_to_text_unstructured', 'get_document_segments', 'create_local_vector_store']

# %% ../nbs/media_stores.ipynb 3
# import libraries here
import os
import itertools

from langchain.embeddings import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders import WebBaseLoader, UnstructuredURLLoader
from langchain.docstore.document import Document

from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain, ConversationalRetrievalChain

# %% ../nbs/media_stores.ipynb 8
def rawtext_to_doc_split(text, chunk_size=1500, chunk_overlap=150):
  
  # Quick type checking
  if not isinstance(text, list):
    text = [text]

  # Create splitter
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                 chunk_overlap=chunk_overlap,
                                                 add_start_index = True)
  
  #Split into docs segments
  if isinstance(text[0], Document):
    doc_segments = text_splitter.split_documents(text)
  else:
    doc_segments = text_splitter.split_documents(text_splitter.create_documents(text))

  # Make into one big list
  doc_segments = list(itertools.chain(*doc_segments)) if isinstance(doc_segments[0], list) else doc_segments

  return doc_segments

# %% ../nbs/media_stores.ipynb 16
## A single File
def _file_to_text(single_file, chunk_size = 1000, chunk_overlap=150):

  # Create loader and get segments
  loader = UnstructuredFileLoader(single_file)
  doc_segments = loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                                      chunk_overlap=chunk_overlap,
                                                                      add_start_index=True))
  return doc_segments


## Multiple files
def files_to_text(files_list, chunk_size=1000, chunk_overlap=150):
  
  # Quick type checking
  if not isinstance(files_list, list):
    files_list = [files_list]

  # This is currently a fix because the UnstructuredFileLoader expects a list of files yet can't split them correctly yet
  all_segments = [_file_to_text(single_file, chunk_size=chunk_size, chunk_overlap=chunk_overlap) for single_file in files_list]
  all_segments = list(itertools.chain(*all_segments)) if isinstance(all_segments[0], list) else all_segments

  return all_segments

# %% ../nbs/media_stores.ipynb 20
def youtube_to_text(urls, save_dir = "content"):
  # Transcribe the videos to text
  # save_dir: directory to save audio files

  if not isinstance(urls, list):
    urls = [urls]
  
  youtube_loader = GenericLoader(YoutubeAudioLoader(urls, save_dir), OpenAIWhisperParser())
  youtube_docs = youtube_loader.load()
  
  return youtube_docs

# %% ../nbs/media_stores.ipynb 24
def save_text(text, text_name = None):
  if not text_name:
    text_name = text[:20]
  text_path = os.path.join("/content",text_name+".txt")
  
  with open(text_path, "x") as f:
    f.write(text)
  # Return the location at which the transcript is saved
  return text_path

# %% ../nbs/media_stores.ipynb 25
def get_youtube_transcript(yt_url, save_transcript = False, temp_audio_dir = "sample_data"):
  # Transcribe the videos to text and save to file in /content
  # save_dir: directory to save audio files

  youtube_docs = youtube_to_text(yt_url, save_dir = temp_audio_dir)
  
  # Combine doc
  combined_docs = [doc.page_content for doc in youtube_docs]
  combined_text = " ".join(combined_docs)
  
  # Save text to file
  video_path = youtube_docs[0].metadata["source"]
  youtube_name = os.path.splitext(os.path.basename(video_path))[0]

  save_path = None
  if save_transcript:
    save_path = save_text(combined_text, youtube_name)
  
  return youtube_docs, save_path

# %% ../nbs/media_stores.ipynb 27
def website_to_text_web(url, chunk_size = 1500, chunk_overlap=100):
  
    # Url can be a single string or list
    website_loader = WebBaseLoader(url)
    website_raw = website_loader.load()

    website_data = rawtext_to_doc_split(website_raw, chunk_size = chunk_size, chunk_overlap=chunk_overlap)
  
    # Combine doc
    return website_data

# %% ../nbs/media_stores.ipynb 33
def website_to_text_unstructured(web_urls, chunk_size = 1500, chunk_overlap=100):

    # Make sure it's a list
    if not isinstance(web_urls, list):
        web_urls = [web_urls]
  
    # Url can be a single string or list
    website_loader = UnstructuredURLLoader(web_urls)
    website_raw = website_loader.load()

    website_data = rawtext_to_doc_split(website_raw, chunk_size = chunk_size, chunk_overlap=chunk_overlap)
  
    # Return individual docs or list
    return website_data

# %% ../nbs/media_stores.ipynb 45
def get_document_segments(context_info, data_type, chunk_size = 1500, chunk_overlap=100):

    load_fcn = None
    addtnl_params = {'chunk_size': chunk_size, 'chunk_overlap': chunk_overlap}

    # Define function use to do the loading
    if data_type == 'text':
        load_fcn = rawtext_to_doc_split
    elif data_type == 'web_page':
        load_fcn = website_to_text_unstructured
    elif data_type == 'youtube_video':
        load_fcn = youtube_to_text
    else:
        load_fcn = files_to_text
    
    # Get the document segments
    doc_segments = load_fcn(context_info, **addtnl_params)

    return doc_segments

# %% ../nbs/media_stores.ipynb 47
def create_local_vector_store(document_segments, **retriever_kwargs):
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(document_segments, embeddings)
    retriever = db.as_retriever(**retriever_kwargs)
    
    return db, retriever
