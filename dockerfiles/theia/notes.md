https://theia-ide.org/docs/composing_applications/
https://www.npmjs.com/search?q=keywords:theia-extension


docker rmi $(docker images -q)

docker build -t tearne/theia:latest .  

docker run -it --rm -p 3000:3000 -v "$(pwd):/home/project" tearne/theia:latest

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

https://github.com/rust-lang/rls-vscode/releases/download/v0.7.8/rust.vsix