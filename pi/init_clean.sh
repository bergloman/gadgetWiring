sudo apt update
sudo apt upgrade -y
sudo apt-get install gcc g++ make tmux mc git logrotate nano -y

# docker
# curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

# nodejs
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt install -y nodejs
