#!/usr/bin/env python
import argparse

from diffusers import StableDiffusionPipeline

parser = argparse.ArgumentParser(description="Generate an image from text usin Stable Diffusion library.")
parser.add_argument("text", action="store", type=str, help="Text for generation.")


def main(text: str) -> None:
    with open("token.txt") as f:
        token = f.read().replace("\n", "")

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", use_auth_token=token
    ).to("cpu")

    image = pipe(text)["sample"][0]
    image.save("output.png")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.text)

