"""Publish measured artifacts, with no credentials written to the repository."""
import argparse
import os
from pathlib import Path
from huggingface_hub import HfApi


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--artifact-dir", type=Path, default=Path("outputs/banking77-ptbr"))
    folder = p.parse_args().artifact_dir
    for name in ("model.skops", "metrics.json", "README.md"):
        if not (folder / name).exists():
            raise FileNotFoundError(name)
    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError("Missing HF credential")
    api = HfApi(token=token)
    repo = api.whoami()["name"] + "/banking77-ptbr-intent-v1"
    api.create_repo(repo_id=repo, repo_type="model", private=False, exist_ok=True)
    api.upload_folder(repo_id=repo, repo_type="model", folder_path=str(folder),
                      commit_message="Publish official held-out benchmark experiment")
    print("PUBLIC_MODEL_URL=https://huggingface.co/" + repo)


if __name__ == "__main__":
    main()
