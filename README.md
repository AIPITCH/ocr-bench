# OCR Bench

OCR tools and models benchmarking framework in the context of AIL-project.

## Terminology and capabilities to be considered:
- **Text Detection**: localize text regions
- **Text Recognition**: transcribe those regions into machine-readable text
- **Text Spotting**: detection and recognition performed together
- **Key Information Extraction (KIE)**
	- document-understanding task
	- interprets the text and layout, assigns labels
	- link a field label to its corresponding value
- **Scene Text Detection**: localize text regions from natural images
- **Scene Text Recognition (STR)**: transcribe those regions

KIE is not mandatory in our operating context.

## Evaluation metrics and existing framework
### Metrics

| Name          | Description                                                                                                                           | Evaluation target                                  | Paper or repository URL                                                                   | License                                                                                                  |
| -             | -                                                                                                                                     | -                                                  | -                                                                                         | -                                                                                                        |
| CER/WER       | Character Error Rate/Word Error Rate                                                                                                  | Machine translation                                | https://aclanthology.org/W03-2804.pdf https://aclanthology.org/W16-2342.pdf               | N/A                                                                                                      |
| Edit Distance | String similarity measurement                                                                                                         | Machine translation                                | https://en.wikipedia.org/wiki/Edit_distance                                               | N/A                                                                                                      |
| BLEU          | BiLingual Evaluation Understudy                                                                                                       | Machine translation                                | https://aclanthology.org/P02-1040.pdf                                                     | N/A                                                                                                      |
| SacreBLEU     | Computation of shareable, comparable, and reproducible BLEU scores                                                                    | Machine translation                                | https://github.com/mjpost/sacrebleu                                                       | Apache-2.0 license                                                                                       |
| ROUGE         | Recall-Oriented Understudy for Gisting Evaluation                                                                                     | Machine summarization/translation                  | https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/was2004.pdf           | N/A                                                                                                      |
| MAUVE         | Compares distributions of generated and human text in an embedding space, aiming to capture both quality and diversity                | Open-ended text generation                         | https://proceedings.neurips.cc/paper/2021/file/260c2432a0eecc28ce03c10dadc078a4-Paper.pdf | N/A                                                                                                      |
| METEOR        | Metric for Evaluation of Translation with Explicit ORdering                                                                           | Machine translation                                | https://www.cs.cmu.edu/~alavie/METEOR/                                                    | LGPL                                                                                                     |
| LEPOR         | LEngth penalty, Precision, n-gram pOsition difference penalty and Recall                                                              | Machine translation                                | https://pypi.org/project/hLepor/                                                          | Apache Software License                                                                                  |
| NIST          | https://en.wikipedia.org/wiki/NIST_(metric) Automatic Evaluation of Machine Translation Quality Using N-gram Co-Occurrence Statistics | N/A                                                | Machine translation                                                                       | https://web.archive.org/web/20170119114251/http://www.itl.nist.gov/iad/mig//tests/mt/doc/ngram-study.pdf |
| BERTscore     | Evaluating Text Generation with BERT                                                                                                  | Open-ended text generation                         | https://github.com/Tiiiger/bert_score                                                     | MIT                                                                                                      |
| ANLS*         | A Universal Document Processing Metric for Generative Large Language Models                                                           | Document classification and information extraction | https://arxiv.org/html/2402.03848v10                                                      | N/A                                                                                                      |

### Existing benchmarking frameworks/tools

| Name                                     | Project URL                                                                | License                        | Code repository                                                                                                                                                      | Freshness |
| -                                        | -                                                                          | -                              | -                                                                                                                                                                    | -         |
| OmniDocBench                             | https://opendatalab.com/omnidocbench                                       | Apache 2.0                     | https://github.com/opendatalab/OmniDocBench                                                                                                                          | 07/2026   |
| OCRBench v2                              | https://99franklin.github.io/ocrbench_v2/                                  | MIT License                    | https://github.com/Yuliang-Liu/MultimodalOCR                                                                                                                         | 07/2026   |
| DocVQA                                   | https://www.docvqa.org/                                                    | N/A (Multiple projects linked) | https://github.com/VLR-CVC/DocVQA2026 Challenge results: https://rrc.cvc.uab.es/?ch=34&com=evaluation&task=1 https://barisdeniz.is-a.dev/posts/perceive-reason-code/ | 04/2026   |
| socOCRbench                              | https://noahdasanaike.github.io/posts/sococrbench.html                     | Private project                | https://www.dropbox.com/scl/fi/kjstgkkofqjs45jugxpcc/dasanaike_vlms.pdf?rlkey=ewkv46l5ghil61u3l66441k31&e=1&st=q5zd7410&dl=0                                         | 05/2026   |
| Scene Text Recognition Model Comparisons | https://arxiv.org/abs/1904.01906                                           | Apache 2.0                     | https://github.com/clovaai/deep-text-recognition-benchmark                                                                                                           | 07/2023   |
| Scene Text Recognition Benchmarks        | https://paperswithcode.co/tasks/scene-text-recognition                     | N/A                            |                                                                                                                                                                      | ongoing   |
| FiftyOne                                 | https://docs.voxel51.com/                                                  | Apache 2.0                     | https://github.com/voxel51/fiftyone                                                                                                                                  | 08/2026   |
| GlotOCR                                  | https://arxiv.org/pdf/2604.12978v1                                         | MIT                            | https://github.com/cisnlp/glotocr-bench                                                                                                                              | 04/2026   |

## Existing OCR Tools and models

### Current

| Name                              | Project URL                                                                                  | License                       | Freshness |
| -                                 | -                                                                                            | -                             | -         |
| EasyOCR                           | https://github.com/jaidedai/easyocr                                                          | Apache 2.0                    | 09/2024   |
| PaddleOCR                         | https://github.com/PADDLEPADDLE/PADDLEOCR                                                    | Apache 2.0                    | 06/2026   |
| Tesseract OCR                     | https://github.com/tesseract-ocr/tesseract                                                   | Apache 2.0                    | 07/2026   |
| docTR                             | https://github.com/mindee/doctr                                                              | Apache 2.0                    | 02/2026   |
| kraken                            | https://github.com/mittagessen/kraken                                                        | Apache 2.0                    | 08/2026   |
| calamari OCR                      | https://github.com/Calamari-OCR/calamari                                                     | GPL 3.0                       | 11/2024   |
| PyLaia                            | https://github.com/Transkribus/PyLaia                                                        | MIT                           | 02/2020   |
| TrOCR                             | https://huggingface.co/docs/transformers/en/model_doc/trocr                                  | MIT                           | ongoing   |
| LiteParse                         | https://github.com/run-llama/liteparse                                                       | Apache 2.0                    | 08/2026   |
| macOCR                            | https://github.com/schappim/macOCR                                                           | MIT                           | 07/2026   |
| Marker                            | https://github.com/datalab-to/marker                                                         | Apache 2.0                    | 07/2026   |
| DeepSeek-OCR                      | https://github.com/deepseek-ai/DeepSeek-OCR                                                  | MIT                           | 01/2026   |
| DeepSeek-OCR 2                    | https://github.com/deepseek-ai/DeepSeek-OCR-2                                                | Apache 2.0                    | 01/2026   |
| Qwen3-VL                          | https://github.com/QwenLM/Qwen3-VL                                                           | Apache 2.0                    | 01/2026   |
| InternVL                          | https://github.com/OpenGVLab/InternVL                                                        | MIT                           | 09/2025   |
| RolmOCR                           | https://huggingface.co/reducto/RolmOCR                                                       | Apache 2.0                    | 04/2025   |
| GOT-OCR2.0                        | https://github.com/Ucas-HaoranWei/GOT-OCR2.0                                                 | Apache 2.0                    | 11/2024   |
| Surya                             | https://github.com/datalab-to/surya                                                          | Apache 2.0                    | 07/2026   |
| Docling                           | https://github.com/docling-project/docling                                                   | MIT                           | 08/2026   |
| MinerU                            | https://github.com/opendatalab/MinerU                                                        | Apache 2.0 + additional terms | 08/2026   |
| Unlimited-OCR                     | https://huggingface.co/baidu/Unlimited-OCR                                                   | MIT                           | 06/2026   |
| MMOCR                             | https://github.com/open-mmlab/mmocr                                                          | Apache 2.0                    | 07/2023   |
| UniParser                         | https://github.com/dptech-corp/UniParser-Tools                                               | Proprietary (?)               | 08/2026   |
| DocVQA 2026: Perceive-Reason-Code | https://github.com/bdsaglam/docvqa / https://barisdeniz.is-a.dev/posts/perceive-reason-code/ | (?)                           | 07/2026   |
| OCR4all                           | https://www.ocr4all.org/                                                                     | MIT                           | 01/2022   |
| GLM-OCR                           | https://github.com/zai-org/GLM-OCR                                                           | Apache 2.0                    | 05/2026   |
| Umi-OCR                           | https://github.com/hiroi-sora/Umi-OCR                                                        | MIT                           | 03/2025   |
| EfficientOCR                      | https://github.com/dell-research-harvard/efficient_ocr                                       | Apache 2.0                    | 04/2025   |

### Legacy
- https://gitlab.com/readcoop/transkribus
- https://github.com/ocropus-archive/DUP-ocropy
- https://github.com/ocropus-archive/ocropus4-old
- https://github.com/antimatter15/ocrad.js
- https://github.com/cdli-gh/Cuneiform-OCR
- https://github.com/NMAC427/SwiftOCR

## References
- Accelerating Document AI: https://huggingface.co/blog/document-ai
- Scene Understanding: https://arxiv.org/abs/1405.0312
- Microsoft COCO: Common Objects in Context: https://arxiv.org/pdf/1405.0312
