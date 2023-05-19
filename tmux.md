```
eval `ssh-agent -s`
eval $(tmux show-env -s |grep '^SSH_')
```
https://blog.mcpolemic.com/2016/10/01/reconciling-tmux-and-ssh-agent-forwarding.html
