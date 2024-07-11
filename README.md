# HiBlu: LLM Chatbot for Blu (Digital Banking)

---

## Background

In today's competitive digital era, user satisfaction is crucial, especially in the banking services sector. Quick and accurate responses to user inquiries are essential for retaining customers. Generative AI, particularly Large Language Models (LLM), has revolutionized user interactions through intelligent chatbots that can provide information quickly and accurately, thereby enhancing operational cost efficiency.

---

## Introduction

HiBlu is a tailored LLM chatbot model created specifically for Blu (a digital banking service). HiBlu is designed to provide quick and accurate responses to customer/prospective customer inquiries related to Blu services, aiming to improve response times, efficiency, and user experience.

This LLM chatbot model is the first prototype, with the hope of future implementation across all Blu services. In the documentation of this prototype, a comparison will also be made between the modeling results of the LLM RAG model, fine-tuned LLM model, and RAFT LLM model.

---

## Team Members

   - [Ahmad Naufal Budianto](https://naufalbudianto.framer.website/)
   - [Gieorgie Kharismatik Kosasih](https://github.com/GieorgieK)
   - [Darly Guntur Darris Purba](https://github.com/DarlyP)
   - [Dito Wicaksana Prasetya](https://github.com/ditoowp)

---

## Data Source

Data reference for this LLM is from Web Scrapping on [FAQ Blu page](https://blubybcadigital.id/info/faq).

---

## RAG LLM Workflow

<center><img src="https://imgtr.ee/images/2024/07/11/ced345b5d0bf4ca7b4bfec39aa11cae9.png" alt="ced345b5d0bf4ca7b4bfec39aa11cae9.png" border="0" /></center>

---

## Fine Tuning LLM Workflow

<center><img src="https://imgtr.ee/images/2024/07/11/da26d77b15aa64e787c98038c1e6da32.png" alt="da26d77b15aa64e787c98038c1e6da32.png" border="0" /></center>

---

## RAFT LLM Workflow

<center><img src="https://imgtr.ee/images/2024/07/11/09d57cc273fa81e677dd021793c45758.png" alt="09d57cc273fa81e677dd021793c45758.png" border="0" /></center>

---

## File Explanation

| File | Explanation |
| --- | --- |
| `scraping.ipynb` | FAQ Web Scrapping Documentation |
| `DAG.py` | DAG Documentation |
| `eda.ipynb` | EDA Documentation |
| `FAQ_GX.ipynb` | Great Expectation Validation Documentation |
| `rag_maverick_vecdb.ipynb` | Vector To MongoDB Documentation |
| `rag_maverick_query.ipynb` | RAG Model Documentation |
| `fine_tuning_maverick_query.ipynb` | Fine Tuning Model Documentation |
| `raft_maverick_query.ipynb` | RAFT Model Documentation |
| `rag.py` | RAG Deployment Documentation |
| `finetuning.py` | Fine Tuning Documentation |
| `raft.py` | RAFT Documentation |

---

## Link

* [Recording Deployment Video](https://drive.google.com/file/d/1AUtG-WBEMWUht799C6bXHG-T645zUv1c/view?usp=sharing)
* [Sample of Model Comparison**](https://docs.google.com/spreadsheets/d/1C6bjPlXn09hHPvgiO1LU5f2JuIc1eKDk/edit?usp=sharing&ouid=108097674241546601906&rtpof=true&sd=true)
* [Presentation Deck]()

**We compare 3 LLM Model using same temperature, prompt and questions.