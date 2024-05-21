# python scripts/download.py --repo_id $1 && python scripts/convert_hf_checkpoint.py --checkpoint_dir checkpoints/$1 && python quantize.py --checkpoint_path checkpoints/$1/model.pth --mode int8


from YoloGemma.utils.hf_download import hf_download
from YoloGemma.utils.convert import convert_hf_checkpoint
from YoloGemma.utils.quantize import quantize

def download_and_quantize_model(repo_id, hf_token):
    # print(repo_id)
    hf_download(repo_id , hf_token)
    convert_hf_checkpoint(checkpoint_dir=f"checkpoints/{repo_id}")
    quantize(checkpoint_path=f"checkpoints/{repo_id}/model.pth", mode="int8")