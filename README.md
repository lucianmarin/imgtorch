# imgtorch

Experiments with PyTorch and images.

- `diff_map.py` — computes an absolute per-pixel difference map between two
  images and saves it as a new image.
- `comp.ipynb` — compares a pair of images with PSNR and SSIM (using `piqa`)
  and calls the difference map helper.

## Usage

```shell
pip install torch torchvision pillow piqa
python diff_map.py bw.jpg enhanced.jpg --output diff.png
```

Sample images included: `flowers.jpg`, `grayscale.jpg`, `bw.jpg`,
`enhanced.jpg`.
