"""Publish an actual measured estimator, model card and calibration metadata."""
import os
from pathlib import Path
from huggingface_hub import HfApi

ROOT = Path("outputs/confidence-evaluation")


def main():
    for name in ("model.skops", "metrics.json", "calibration.json", "README.md"):
        if not (ROOT / name).is_file():
            raise FileNotFoundError(ROOT / name)
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise ValueError("Missing private Hugging Face publishing credential")
    api = HfApi(token=token)
    owner = api.whoami()["name"]
    if owner.lower() != "joaooalbernaz":
        raise PermissionError("Unexpected Hugging Face owner")
    repo = owner + "/banking77-ptbr-confidence-v1"
    api.create_repo(repo_id=repo, repo_type="model", private=False, exist_ok=True)
    api.upload_folder(
        repo_id=repo, repo_type="model", folder_path=str(ROOT),
        commit_message="Publish separately trained confidence model and measured calibration study",
    )
    print("PUBLIC_MODEL_URL=https://huggingface.co/" + repo)


if __name__ == "__main__":
    main()
