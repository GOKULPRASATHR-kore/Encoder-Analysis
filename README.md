```markdown
# Universal Sentence Encoder-5 Embedding Analysis

This repository contains the code and instructions for analyzing the Universal Sentence Encoder-5 (USE-5) model for embedding generation. The primary focus is on analyzing the impact of proper nouns within sentence embeddings.

## Progress
-  Model download and setup
-  Utterance generation
-  Embedding generation
-  Cosine score generation
-  Results Excel Sheet generation

## Prerequisites

Ensure you have the following installed:

- Python 3.9.8
- Numpy 1.26.0
- ONNX
- Openpyxl


## Model Download

Download the USE-5 model from the Huggingface repository:

[Universal Sentence Encoder Large 5 ONNX Model](https://huggingface.co/SamLowe/universal-sentence-encoder-large-5-onnx/blob/main/model.onnx)

**Note:** The model size should be 589 MB. Ensure the downloaded model matches this size. If not, download it again.

## Usage

Here's a sample code snippet to load the ONNX model and generate embeddings:

import onnx
import onnxruntime as ort
from onnxruntime_extensions import get_library_path
from os import cpu_count

sentences = ["hello world"]

def load_onnx_model(model_filepath):
    _options = ort.SessionOptions()
    _options.inter_op_num_threads = cpu_count()
    _options.intra_op_num_threads = cpu_count()
    _options.register_custom_ops_library(get_library_path())
    _providers = ["CPUExecutionProvider"]  # could use ort.get_available_providers()
    return ort.InferenceSession(path_or_bytes=model_filepath, sess_options=_options, providers=_providers)

model = load_onnx_model("<path-to-onnx-model>")

model_outputs = model.run(output_names=["outputs"], input_feed={"inputs": sentences})[0]
print(model_outputs)

## NOTE

Replace `<path-to-onnx-model>` with the actual path to your downloaded ONNX model file.
If the model is loaded and executed correctly, it will produce an embedding array.
