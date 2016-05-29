call plug#begin('~/.vim/plugged')

Plug 'pangloss/vim-javascript'
Plug 'ctrlpvim/ctrlp.vim'

call plug#end()

autocmd Filetype javascript setlocal ts=2 sts=2 sw=2 expandtab
autocmd Filetype html setlocal ts=2 sts=2 sw=2 expandtab
