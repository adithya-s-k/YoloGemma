import argparse

from YoloGemma.download import download_and_quantize_model
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and quantize a model.")
    parser.add_argument("--repo_id", type=str, required=False, default="google/paligemma-3b-mix-224" , help="The repository ID to download the model from.")
    parser.add_argument("--hf_token", type=str, required=False, help="The Hugging Face token for authentication.")
    
    args = parser.parse_args()
    download_and_quantize_model(args.repo_id, args.hf_token)