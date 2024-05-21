from pathlib import Path
from YoloGemma.inference import main

TOKENIZERS_PARALLELISM=True

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Your CLI description.')

    ### NEW PARAMS

    parser.add_argument('--prompt', type=str, default="detect cat", help='Input prompt.')
    parser.add_argument('--vid_path', type=str, default="", help='path to mp4 video.')
    parser.add_argument('--vid_start', type=int, default=0, help='Where in video to start detecting (seconds).')
    parser.add_argument('--vid_end', type=int, default=10, help='Where in video to end detecting (seconds).')

    ### OLD PARAMS
    
    parser.add_argument('--interactive', action='store_true', help='Whether to launch in interactive mode')
    parser.add_argument('--max_new_tokens', type=int, default=15, help='Maximum number of new tokens.')
    parser.add_argument('--top_k', type=int, default=200, help='Top-k for sampling.')
    parser.add_argument('--temperature', type=float, default=0.8, help='Temperature for sampling.')
    parser.add_argument('--checkpoint_path', type=Path, default=Path("checkpoints/google/paligemma-3b-mix-224/modelint8.pth"), help='Model checkpoint path.')
    parser.add_argument('--compile', action='store_true', help='Whether to compile the model.', default=True)
    parser.add_argument('--compile_prefill', action='store_true', help='Whether to compile the prefill (improves prefill perf, but higher compile times)')
    parser.add_argument('--profile', type=Path, default=None, help='Profile path.')
    parser.add_argument('--speculate_k', type=int, default=5, help='Speculative execution depth.')
    parser.add_argument('--draft_checkpoint_path', type=Path, default=None, help='Draft checkpoint path.')
    parser.add_argument('--device', type=str, default="cuda", help='device to use')


    args = parser.parse_args()

    main(
        args.prompt, args.vid_path, args.vid_start, args.vid_end, args.interactive, args.max_new_tokens, args.top_k,
        args.temperature, args.checkpoint_path, args.compile, args.compile_prefill, args.profile, args.draft_checkpoint_path,
        args.speculate_k, args.device
    )