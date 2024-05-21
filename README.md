# YoloGemma

**YoloGemma** is an project showcasing the capabilities of Vision-Language models in performing computer vision tasks such as object detection and segmentation tasks. At the heart of this experiment lies [**PaliGemma**](https://huggingface.co/google/paligemma-3b-mix-224), a state-of-the-art model that bridges the gap between Language and Vision. Through YoloGemma, we aim to explore whether Vision-Language models can match but conventional methods of computer vision.

## Outputs

YoloGemma generates outputs by processing images and videos to identify and segment objects within them. The results are visualized as annotated images or videos, highlighting detected objects with bounding boxes or segmentation masks.

## Installation

To get started with YoloGemma, follow these simple installation steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/YoloGemma.git
    cd YoloGemma
    ```

2. Install the required dependencies:
    ```bash
    conda create -n YoloGemma-venv python=3.10
    conda activate YoloGemma-venv
    pip install -e .
    ```
## How to Run

- **Model Download:** You can download the model by running the following command:
    ```bash
    python download.py
    ```
    This command will download and quantize the model.

YoloGemma provides three main scripts to facilitate various tasks. Below are instructions on how to run each script:

1. **Main Script for Object Detection and Segmentation:**
    ```bash
    python main.py --task "detect" --object "Cat" --input_path path/to/input --output_path path/to/output
    ```
    Parameters:
    - `--task`: Specify whether to `detect` or `segment`.
    - `--object`: Define the object or objects you want to perform the task on.
    - `--input_path`: Path to the input image or video.
    - `--output_path`: Path to where the output will be saved.

    Replace `path/to/input` with the path to your input image or video, and `path/to/output` with the desired output path.

2. **Server Script to Run a Server:**
    ```bash
    python server.py --port 8080
    ```
    This command will start a server on port 8080, allowing you to send requests for object detection and segmentation.

    
3. **Gradio Interface:**
    (Note: Yet to be implemented)
    ```bash
    python gradio.py
    ```
    This command will launch a Gradio interface, providing an interactive web application to perform object detection and segmentation.


## Acknowledgements

Special thanks to [PaliGemma](https://huggingface.co/blog/paligemma) for their groundbreaking work in Vision-Language models, which serves as the foundation for this project.
The project was inspired by this repository - [loopvlm](https://github.com/sumo43/loopvlm)

---

YoloGemma is an exciting experimental step towards the future of visison langauge model based computer vision, blending the strengths of language models with visual understanding.
