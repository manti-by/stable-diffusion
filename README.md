Stable Diffusion on Intel CPU
====

Installation
----

```bash
$ git clone https://github.com/manti-by/stable-diffusion.git
$ pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

Usage
----

1. To start using Stable Diffusion library you need register on (huggingface.co)[https://huggingface.co/] and 
(generate a new token)[https://huggingface.co/docs/hub/security-tokens].

2. Clone source code and install requirements:

```bash
$ git clone https://github.com/manti-by/stable-diffusion.git
$ pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

3. Put you securoty token into file `token.txt` inside project root directory.

4. Run generation:

```bash
$ python3 main.py 'The serene glide and billowing synths'
```

5. Check a resulting file `output.png`.

