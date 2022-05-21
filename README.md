<h1 align="center"> <img alt="Tap Tap Defense" title="Tap Tap Defense" src="game_assets/icon.png" width="50">Tap Tap Defense </h1> <br>

<p align="center">
    <img alt="Tap Tap Defense" title="Tap Tap Defense" src="assets_readme/gambar/Start_Game.png" width="600">
</p>
<p>
<p align="center"> Tap Tap Defense <br>
(Tugas Besar PBO RA-04) <br>
</p>
<p align="center">
    <a href="https://github.com/rajastra/Tap-Tap-Defense/graphs/contributors">
    <img src="https://img.shields.io/badge/contributors-6-red?style=flat-square&logo=appveyor" alt="Contributors">
  </a>
    <a href="https://www.pygame.org/news">
    <img src="https://img.shields.io/pypi/v/pygame?style=flat-square&logo=appveyor" alt="Pygame">
  </a>
</p>

<br>

## Table of Content

- [Description of Project](#description-of-project)
- [How to Run a Game](#how-to-run-a-game)
- [How to Play a Game](#how-to-play-a-game)
- [Features](#features)
- [UML Class Diagram](#uml-class-diagram)
- [Contributors of Project](#contributors-of-project-✨)

## Description of Project

Proyek yang kami buat yaitu Proyek game sederhana bernama <b>Tap Tap Defense</b>, <b>Tap Tap Defense</b> yaitu sebuah game dua dimensi yang konsep bermainnya hampir sama dengan game mobile <b> Smash Ant </b> yaitu pertahankan batas penjagaan kita dengan cara menghabisi musuh yang datang dari arah berlawanan batas penjagaan dengan cara mengarahkan cursor ke musuh dan menekan tombol kiri mouse dan Player akan kalah apabila darah player habis(Musuh yang berhasil melewati perbatasan sebanyak darah player) dan bila player berhasil menahan musuh secara terus-menerus maka musuh juga akan bertambah kuat. Selain itu, didalam game ini juga terdapat skill yang dapat digunakan tetapi menggunakan mana,skill diaktifkan dengan mengklik mouse sebelah kanan.

<br>

## How to Run a Game

- #### Install Dependecies

```bash
git clone https://github.com/rajastra/Tap-Tap-Defense
cd Tap-Tap-Defense

pip install pygame
```

- ### Run a Game

```python
py ./main.py

atau

python main.py

atau

python3 main.py
```

<br>

## How to Play a Game

- ### Start a Game

Berikut ini adalah gambar untuk panduan memulai Game <b> Tap Tap Defense</b>

  <img alt="Tap Tap Defense" title="Tap Tap Defense" src="assets_readme/gambar/start_menu.png" width="600">

- ### Game Play

Berikut ini adalah gambar untuk panduan bermain <b> Tap Tap Defense</b>

  <img alt="Tap Tap Defense" title="Tap Tap Defense" src="assets_readme/gambar/gameplay.png" width="600">

Gameplay :

1. Tembak bombo agar tidak mencapai batas dan mendapatkan poin sebanyak banyaknya
2. Jika bombo melewati batas maka kastel akan hancur sedikit demi sedikit
3. Permainan berakhir jika kastel hancur lebur

- ### End Game

Permainan akan berakhir apabila kastel sudah hancur lebur
<br>
Bisa dilihat di video dibawah ini:
<br>

![end_game](assets_readme/gambar/end_game.gif)

- ### Control in Game

Berikut adalah gambar untuk panduan Control in Game seperti cara shoot klik apa, reload klik apa,dan sebagainya.
<br>
<img alt="Tap Tap Defense" title="Tap Tap Defense" src="assets_readme/gambar/control_game.png" width="600">

<details>

<summary>What if... Player choose Glock Weapon?</summary>
Jika player memilih Senjata Glock di dalam Game ,makaplayer akan mendapat amunisi sebanyak 15, namun untuk hitkepada giant bombo menjadi kurang damagenya dibandingkandengan revolver.
<br>

![glock](assets_readme/gambar/glock.gif)

</details>
<br>
<details>
<summary>What if... Player choose Revolver Weapon?</summary>
Jika player memilih Senjata Revolver di dalam Game ,maka player hanya akan mendapat amunisi sebanyak 6 (lebih sedikit dibandingkan Glock), namun untuk hit kepada giant bombo lebih besar dibandingkan dengan Glock.
<br>

![revolver](assets_readme/gambar/revolver.gif)

</details>
<br>
<details>
<summary>What if... Player choose Skill 1?</summary>
Jika player ingin menggunakan skill1,maka player harus menggunakan mana sesuai ketentuan berikut dan fungsi dari skillnya.
<br>
Skill 1 (100 mana) = Mendorong Normal Bombo sejauh 100 pixel dan menghentikan pergerakan Giant Bombo untuk sementara
<br>

![skill1](assets)

</details>
<br>
<details>
<summary>What if... Player choose Skill 2?</summary>
Jika player ingin menggunakan skill2,maka player harus menggunakan mana sesuai ketentuan berikut dan fungsi dari skillnya.
<br>
Skill 2 (150 mana) = Memberikan 5 damage serta menghentikan sementara pergerakan semua bombo yang ada
<br>

![skill2](assetsf)

</details>
<br>
<details>
<summary>What if... Player choose Skill 3?</summary>
Jika player ingin menggunakan skill2,maka player harus menggunakan mana sesuai ketentuan berikut dan fungsi dari skillnya.
<br>
Skill 3 (300 mana) = Menghapus semua bombo yang ada
<br>

![skill3](assets)

</details>
<br>
<details>
<summary>What if... Player wanna cheat?</summary>
1. Cheat Button
<br>
Berikut ini cara untuk mengaktifkan cheatnya:
<br>
<img alt="Tap Tap Defense" title="Tap Tap Defense" src="assets_readme/gambar/cheat_shortcut.png" width="600">
<br>
2. Cheat Murder (Keyboard P atau p)
<br>
Cheat ini merupakan cheat yang meningkatkan FPS dari 30 menjadi 240 sehingga gameplay menjadi sangat cepat dan musuh akan berjalan sangat cepat dan bermunculan sangat banyak sehingga cheat ini dinamakan bunuh diri.
<br>

![cheat](assets)
<br> 3. Cheat Mana (Keyboard O atau o)
<br>
Cheat ini berfungsi untuk mengisi mana menjadi full sehingga player bisa menggunakan skill sesuka hati.
<br>

![cheat](assets)

</details>

<br>

## UML Class Diagram

Berikut adalah UML Class Diagram Proyek Kelompok kami:

<br>

## Contributors of Project ✨

<br>

Thanks to Contribue this Project 🙏

<br>

<table>
<tr>
    <td align="center"><a href="https://github.com/120140056"><img src="https://avatars.githubusercontent.com/u/103248575?v=4" width="100px;" alt=""/><br /><sub><b>Christian <br>
    (120140056)</br></sub></a><br /></td>
    <td align="center"><a href="https://github.com/irwantoYS"><img src="https://avatars.githubusercontent.com/u/103361592?v=4" width="100px;" alt=""/><br /><sub><b>Irwanto Yezekiel <br>Sihotang <br>(120140227)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/wellaamandaa"><img src="https://avatars.githubusercontent.com/u/103342778?v=4" width="100px;" alt=""/><br /><sub><b>Wella <br>Amanda <br>(120140057)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/rajastra"><img src="https://avatars.githubusercontent.com/u/89762086?v=4" width="100px;" alt=""/><br /><sub><b>Raja  Saputera <br>(120140228)</br></sub></a><br /></td>
    
</tr>
<tr>
    <td align="center"><a href="https://github.com/120140219"><img src="https://avatars.githubusercontent.com/u/104046990?v=4" width="100px;" alt=""/><br /><sub><b>M. Rafi Irfan Lubis <br>(120140219)</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/krisnasaputtra"><img src="https://avatars.githubusercontent.com/u/94743282?v=4" width="100px;" alt=""/><br /><sub><b>Krisna Saputra <br>(120140221)</b></sub></a><br /></td>
</tr>
</table>
