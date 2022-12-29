# 疑似バーガー店員体験サービス
バーガー店員体験できるROSパッケージです。
## 詳細
プログラムが動くと注文が行われます。声を出してしっかりと確認しよう。

## 必要なソフトウェア
  * Python

  * テスト環境
	* Ubuntu20.04
  * ROS2
	* インストールに使用したスクリプト(https://github.com/ryuichiueda/ros2_setup_scripts/blob/master/setup.bash)

## インストール方法
### 本パッケージをクローンし、依存関係をインストールする
cd ~ros2_ws/src
git clone https://github.com/TarouSatou/Moc.git

### パッケージをビルドする
cd ~/ros2_ws
colcon build
source ~/.bashrc

## 使用方法
ビルドが出来たら下記のコマンドを実行する
ros2 launch moc talk_listen.launch.py

## 権利関係・謝辞
  * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  * このパッケージは，https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/ 由来のコード（© 2022 Ryuichi Ueda）を利用しています．
  * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作とし>たものです．
      * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  * © 2022 Tarou Satou

