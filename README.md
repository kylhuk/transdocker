# transdocker

Using the en-de ml model (`opus-mt-en-de`) of the University of Helsinki inside a docker container with a small frontend.

*Disclaimer:* This thing is probably super unstable and absolutely not optimized. Feel free to open PR if you think you can do it better.

## How-to
1) Clone this repo `git clone https://github.com/kylhuk/transdocker.git`
2) Change into the directory `cd transdocker`
3) Build the docker container `docker build -t transdocker:v1 .`
4) Run the docker container `docker run -it -p5000:5000 transdocker:v1`
5) Open the `index.html`

## Citation Information
```
@InProceedings{TiedemannThottingal:EAMT2020,
  author = {J{\"o}rg Tiedemann and Santhosh Thottingal},
  title = {{OPUS-MT} — {B}uilding open translation services for the {W}orld},
  booktitle = {Proceedings of the 22nd Annual Conferenec of the European Association for Machine Translation (EAMT)},
  year = {2020},
  address = {Lisbon, Portugal}
 }
```
