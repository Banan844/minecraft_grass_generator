# Minecraft grass texture generator
Generates gray gradient colors from 117 to 192 *(can be easy changed in code)*. After that, generating image, sized 16x16 px *(also can be easy changed)*, where randomly choices pixel from gradient.
## Dependencies
Requires: [**PyPNG**](https://pypi.org/project/pypng/ "See on PyPI"). Install with: `pip install pypng`.
## Usage
Starting without arguments creates image `image.png` in folder, where you writed command, random seed is selecting by python random. If you started program with random seed argument, all at same, but image generating with your random seed.

**Program arguments**: random seed *(not required, type: integer)*.

Start without arguments:
```bash
python main.py
```

Start with random seed argument *(here random seed is **123**)*:
```bash
python main.py 123
```
## Example
Image generated with seed 1 *(scaled)*:

![Example image](example_image.png "Generated image with seed 1")
