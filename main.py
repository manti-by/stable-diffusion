#!/usr/bin/env python
from diffusers import StableDiffusionPipeline


def main():
    with open("token.txt") as f:
        token = f.read().replace("\n", "")

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", use_auth_token=token
    ).to("cpu")

    prompt = """
        Allnite Music boss APOENA returns with the label's second essential release in a mere matter of weeks.
        Four slices of exceptionally cool house music, from 'Soul People' with its chuntering organs and inspirational
         rabble rousing sampled from Martin Luther King to 'Meditation' with its cowbell-enhanced groove and oozing, 
         soulful vocals. The serene glide and billowing synths of 'Jus Dance' and the meditational hypnotism of 
         'Shapeshifters' complete the package, all going to make one neat selection of tasteful, addictive cuts.
    """
    image = pipe(prompt)["sample"][0]
    image.save("output/out.png")


if __name__ == "__main__":
    main()
