# OCR Bench

OCR tools and models benchmarking framework in the context of AIL-project.

## Terminology and capabilities to be considered:
- **Text detection**: localizes text regions
- **Text recognition**: transcribes those regions into machine-readable text
- **Text spotting**: detection and recognition performed together
- **Key Information Extraction (KIE)**
	- document-understanding task
	- interprets the text and layout, assigns labels
	- link a field label to its corresponding value

KIE is not mandatory in our operating context.

## Open questions/comments
- Most translation and text generation related metrics compare tools/models output to human produced output
- Can machine translation and text generation related metrics be used to evaluate the quality of an OCR process ?

## Evaluation metrics and existing framework
### Metrics

| Name      | Description                                                                                                                           | Evaluation target                                  | Paper or repository URL                                                                   | License                                                                                                  |
| -         | -                                                                                                                                     | -                                                  | -                                                                                         | N/A                                                                                                      |
| CER/WER   | Character Error Rate/Word Error Rate                                                                                                  | Machine translation                                | https://aclanthology.org/W03-2804.pdf https://aclanthology.org/W16-2342.pdf               | N/A                                                                                                      |
| BLEU      | BiLingual Evaluation Understudy                                                                                                       | Machine translation                                | https://aclanthology.org/P02-1040.pdf                                                     | N/A                                                                                                      |
| SacreBLEU | Computation of shareable, comparable, and reproducible BLEU scores                                                                    | Machine translation                                | https://github.com/mjpost/sacrebleu                                                       | Apache-2.0 license                                                                                       |
| ROUGE     | Recall-Oriented Understudy for Gisting Evaluation                                                                                     | Machine summarization/translation                  | https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/was2004.pdf           | N/A                                                                                                      |
| MAUVE     | Compares distributions of generated and human text in an embedding space, aiming to capture both quality and diversity                | Open-ended text generation                         | https://proceedings.neurips.cc/paper/2021/file/260c2432a0eecc28ce03c10dadc078a4-Paper.pdf | N/A                                                                                                      |
| METEOR    | Metric for Evaluation of Translation with Explicit ORdering                                                                           | Machine translation                                | https://www.cs.cmu.edu/~alavie/METEOR/                                                    | LGPL                                                                                                     |
| LEPOR     | LEngth penalty, Precision, n-gram pOsition difference penalty and Recall                                                              | Machine translation                                | https://pypi.org/project/hLepor/                                                          | Apache Software License                                                                                  |
| NIST      | https://en.wikipedia.org/wiki/NIST_(metric) Automatic Evaluation of Machine Translation Quality Using N-gram Co-Occurrence Statistics | N/A                                                | Machine translation                                                                       | https://web.archive.org/web/20170119114251/http://www.itl.nist.gov/iad/mig//tests/mt/doc/ngram-study.pdf |
| BERTscore | Evaluating Text Generation with BERT                                                                                                  | Open-ended text generation                         | https://github.com/Tiiiger/bert_score                                                     | MIT                                                                                                      |
| ANLS*     | A Universal Document Processing Metric for Generative Large Language Models                                                           | Document classification and information extraction | https://arxiv.org/html/2402.03848v10                                                      | N/A                                                                                                      |

### Existing frameworks

| Name         | Project URL                                               | License                        | Code repository                                                                                                                                                      | Freshness |
| -            | -                                                         | -                              | -                                                                                                                                                                    | -         |
| OmniDocBench | https://opendatalab.com/omnidocbench                      | Apache 2.0                     | https://github.com/opendatalab/OmniDocBench                                                                                                                          | 07/2026   |
| OCRBench v2  | https://99franklin.github.io/ocrbench_v2/                 | MIT License                    | https://github.com/Yuliang-Liu/MultimodalOCR                                                                                                                         | 07/2026   |
| DocVQA       | https://www.docvqa.org/                                   | N/A (Multiple projects linked) | https://github.com/VLR-CVC/DocVQA2026 Challenge results: https://rrc.cvc.uab.es/?ch=34&com=evaluation&task=1 https://barisdeniz.is-a.dev/posts/perceive-reason-code/ | 04/2026   |
| socOCRbench  | https://noahdasanaike.github.io/posts/sococrbench.html    | Private project                | https://www.dropbox.com/scl/fi/kjstgkkofqjs45jugxpcc/dasanaike_vlms.pdf?rlkey=ewkv46l5ghil61u3l66441k31&e=1&st=q5zd7410&dl=0                                         | 05/2026   |

## Existing OCR Tools and models
[...]

### Non-LLM based
[...]

### LLM based
[...]

### Legacy tools
[...]

