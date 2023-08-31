# LibreMemChess




## Setup 
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

An anki plugin based on this project:
https://github.com/TowelSniffer/Anki-Chess-2.0

# developer notes:

Plan is to import now the ches.apkg programmatically, 
then we will edit the collection with the anki api, and clone as many notes as we want. 


Installation might be a bit tricky, because we have to copy the
collection.media contents to the appropriate directory. 
This will need to be a runtime check, and we will need to bundle the files with the plugin.

more ideas:
- change the size of the anki window to fit the board
- create seperate menu bar entry
- 
##  Resources
https://github.com/SergioFacchini/anki-cards-web-browser/blob/master/documentation/Processing%20Anki%27s%20.apkg%20files.md

https://addon-docs.ankiweb.net/a-basic-addon.html
https://forums.ankiweb.net/t/pycharm-setup-for-add-on-debugging/17733

We will need to put any files in `user_files`: https://addon-docs.ankiweb.net/addon-config.html#user-files
