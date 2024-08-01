import torch
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)

def generate_image(prompt, output_path):
    image = pipe(prompt).images[0]
    image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    # Example prompts
    prompts = [
        "A large office building representing a company with 1000 employees",
        "A stack of cash representing 1 million dollars",
        "Comparison of company offices based on employee count"
    ]

    for i, prompt in enumerate(prompts):
        generate_image(prompt, f"output_{i}.png")

if __name__ == "__main__":
    main()
