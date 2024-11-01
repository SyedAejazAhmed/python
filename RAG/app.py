import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# API key is stored in Streamlit secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

pdf_mappings = {
    "SEC-2019.pdf": (1, 52),
    "SEC-2020.pdf": (54, 90),
    "SEC-2021.pdf": (91, 136),
    "SEC-2022.pdf": (137, 257),
    "SEC-2023.pdf": (258, 350)
}

def get_source_and_page(merged_page_number):
    for pdf_name, (start_page, end_page) in pdf_mappings.items():
        if start_page <= merged_page_number <= end_page:
            relative_page_number = merged_page_number - start_page + 1
            return pdf_name, relative_page_number
    return None, None

pdf_path = 'SEC-merged.pdf'
pdfreader = PdfReader(pdf_path)

text_with_page_numbers = []
for page_number, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        text_with_page_numbers.append((content, page_number + 1))

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)

texts_with_pages = []
for content, page_number in text_with_page_numbers:
    texts = text_splitter.split_text(content)
    for text in texts:
        texts_with_pages.append((text, page_number))

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
documentsearch = FAISS.from_texts([text for text, _ in texts_with_pages], embeddings)

qa_chain = load_qa_chain(OpenAI(api_key=OPENAI_API_KEY), chain_type="refine")

def answer_query(query):
    doc = documentsearch.similarity_search(query, k=1)[0]
    
    index = [text[0] for text in texts_with_pages].index(doc.page_content)
    merged_page_number = texts_with_pages[index][1]
    
    source_pdf, actual_page_number = get_source_and_page(merged_page_number)
    
    answer = qa_chain.run(input_documents=[doc], question=query)
    
    return answer, source_pdf, actual_page_number

def main():
    st.title("SEC-Saudi Electricity Company")
    
    query = st.text_input("Enter your question about the PDF:")

    if query:
        answer, source_pdf, actual_page_number = answer_query(query)
        st.write("### Answer:")
        st.write(answer)
        st.write("### Source:")
        st.write(f"Source PDF: {source_pdf}")
        st.write(f"Page Number: {actual_page_number}")

if __name__ == "__main__":
    main()

