 OCR Bench

OCR tools and models benchmarking framework in the context of AIL-project.

## Terminology and capabilities to be considered:
- Text detection: localizes text regions
- Text recognition: transcribes those regions into machine-readable text
- Text spotting: detection and recognition performed together
- Key Information Extraction (KIE)
	- document-understanding task
	- interprets the text and layout, assigns labels
	- link a field label to its corresponding value

KIE is not mandatory in our operating context.

## Evaluation metrics and existing framework
### Metrics

| Name    | Description                                                                                                            | Usage                             | URL                                                                                       |
| -       | -                                                                                                                      | -                                 | -                                                                                         |
| CER/WER | Character Error Rate/Word Error Rate                                                                                   | Machine translation               | https://aclanthology.org/W03-2804.pdf https://aclanthology.org/W16-2342.pdf               |
| BLEU    | BiLingual Evaluation Understudy                                                                                        | Machine translation               | https://aclanthology.org/P02-1040.pdf                                                     |
| ROUGE   | Recall-Oriented Understudy for Gisting Evaluation                                                                      | Machine summarization/translation | https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/was2004.pdf           |
| MAUVE   | Compares distributions of generated and human text in an embedding space, aiming to capture both quality and diversity | Open-ended text generation        | https://proceedings.neurips.cc/paper/2021/file/260c2432a0eecc28ce03c10dadc078a4-Paper.pdf |
| ...     | ...                                                                                                                    | ...                               | ...                                                                                       |

### Existing frameworks

| Name         | Project URL                               | License                        | Code repository                                                                                                                                                      | Freshness |
| -            | -                                         | -                              | -                                                                                                                                                                    | -         |
| OmniDocBench | https://opendatalab.com/omnidocbench      | Apache 2.0                     | https://github.com/opendatalab/OmniDocBench                                                                                                                          | 07/2026   |
| OCRBench v2  | https://99franklin.github.io/ocrbench_v2/ | MIT License                    | https://github.com/Yuliang-Liu/MultimodalOCR                                                                                                                         | 07/2026   |
| DocVQA       | https://www.docvqa.org/                   | N/A (Multiple projects linked) | https://github.com/VLR-CVC/DocVQA2026 Challenge results: https://rrc.cvc.uab.es/?ch=34&com=evaluation&task=1 https://barisdeniz.is-a.dev/posts/perceive-reason-code/ | 04/2026   |
| ...          | ...                                       | ...                            | ...                                                                                                                                                                  |           |

## Existing Tools and models
[...]

### Non-LLM based
[...]

### LLM based
[...]

### Legacy tools
[...]

