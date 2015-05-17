sudo apt-get update && apt-get install -y xdotool chromium unclutter 
cd
mkdir src
git clone https://github.com/ukscone/set_overscan.git
cd set_overscan
make
cd ..
wget http://steinerdatenbank.de/software/kweb-1.6.4.tar.gz
tar -xzf kweb-1.6.4.tar.gz
cd kweb-1.6.4
./debinstall
cd ..
