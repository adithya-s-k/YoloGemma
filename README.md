# YoloGemma

**YoloGemma** is a project showcasing the capabilities of Vision-Language models in performing computer vision tasks such as object detection and segmentation. At the heart of this experiment lies [**PaliGemma**](https://huggingface.co/google/paligemma-3b-mix-224), a state-of-the-art model that bridges the gap between Language and Vision. Through YoloGemma, we aim to explore whether Vision-Language models can match conventional methods of computer vision.

## Outputs

YoloGemma generates outputs by processing images and videos to identify and segment objects within them. The results are visualized as annotated images or videos, highlighting detected objects with bounding boxes or segmentation masks.

<table>
    <tr>
        <td>
            Detect Big Cat:
            <video width="100%" src="https://github.com/adithya-s-k/YoloGemma/assets/27956426/7647388d-4dff-4c15-b1a1-12c2be546c08">
            </td>
        <td>
            Detect Small Cat:
            <video width="100%" src="https://github.com/adithya-s-k/YoloGemma/assets/27956426/3c912f39-4a14-407b-a0d3-59f917ddf413">
        </td>
    </tr>
    <tr>
        <td>
            Detect Gojo:
            <video width="100%" src="https://github.com/adithya-s-k/YoloGemma/assets/27956426/1fe68517-0705-47b2-a32b-c574a5c6756f">
        </td>
        <td>
            Detect Short Person:
            <video width="100%" src="https://github.com/adithya-s-k/YoloGemma/assets/27956426/5766b75d-4b9a-4a0b-8228-57d2b866b550">
        </td>
    </tr>
</table>

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

### Model Download
You can download the model by running the following command:
```bash
python download.py
```
This command will download and quantize the model.

YoloGemma provides three main scripts to facilitate various tasks. Below are instructions on how to run each script:

### Main Script for Object Detection
```bash
python main.py --prompt "Detect 4 people" --vid_path ./people.mp4 --vid_start 1 --vid_end 12 --max_new_tokens 10
```

#### Command Line Arguments

- **`--prompt`** (type: `str`, default: `"detect cat"`): The prompt specifying what to detect in the video.
- **`--vid_path`** (type: `str`, default: `""`): The path to the input MP4 video file.
- **`--vid_start`** (type: `int`, default: `0`): The start time in seconds where the detection should begin.
- **`--vid_end`** (type: `int`, default: `10`): The end time in seconds where the detection should stop.
- **`--max_new_tokens`** (type: `int`, default: `15`): Maximum number of new tokens.

#### Additional Parameters

- **`--interactive`** (action: `store_true`): Launch the application in interactive mode.
- **`--top_k`** (type: `int`, default: `200`): Top-k sampling for generating new tokens.
- **`--temperature`** (type: `float`, default: `0.8`): Sampling temperature.
- **`--checkpoint_path`** (type: `Path`, default: `Path("checkpoints/google/paligemma-3b-mix-224/modelint8.pth")`): Path to the model checkpoint file.
- **`--compile`** (action: `store_true`, default: `True`): Whether to compile the model.
- **`--compile_prefill`** (action: `store_true`): Whether to compile the prefill for improved performance.
- **`--profile`** (type: `Path`, default: `None`): Path to the profile.
- **`--speculate_k`** (type: `int`, default: `5`): Speculative execution depth.
- **`--draft_checkpoint_path`** (type: `Path`, default: `None`): Path to the draft checkpoint.
- **`--device`** (type: `str`, default: `"cuda"`): Device to use for running the model (e.g., `"cuda"` for GPU).

## Example

```bash
python main.py --prompt "Detect 4 people" --vid_path ./people.mp4 --vid_start 1 --vid_end 12 --max_new_tokens 10
```

This command will start the detection process for the prompt "Detect 4 people" on the video located at `./people.mp4`, beginning at 1 second and ending at 12 seconds into the video. It will use a maximum of 10 new tokens during processing.

### Gradio Interface (Coming Soon)

```bash
python demo.py
```
This command will launch a Gradio interface, providing an interactive web application to perform object detection and segmentation.

## Troubleshooting

If you encounter any issues, please ensure that:
- The video file path is correct and the file is accessible.
- The required dependencies are installed.
- Your system has the necessary hardware (e.g., a compatible GPU if using CUDA).

For further assistance, please refer to the project's [issues page](https://github.com/adithyas-s-k/YoloGemma/issues) or contact the maintainers.

## Acknowledgements

Special thanks to [PaliGemma](https://huggingface.co/blog/paligemma) for their groundbreaking work in Vision-Language models, which serves as the foundation for this project. The project was inspired by this repository - [loopvlm](https://github.com/sumo43/loopvlm).

---

YoloGemma is an exciting experimental step towards the future of vision-language model-based computer vision, blending the strengths of language models with visual understanding.
