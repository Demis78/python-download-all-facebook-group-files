python-download-all-facebook-group-files
==============================

Downloads all files from specified Facebook group

1. Install the FacePy module:

    $ pip install --user facepy

2. Generate your Facebook access token from here and make sure to tick all the boxes. Some of the boxes might not be necessary, but I am too lazy to find out which ones.

    https://developers.facebook.com/tools/explorer/

3. Run the program and provide the group ID and the access token:

    $ ./dl\_fb\_files.py _GROUPID_ _ACCESSTOKEN_

For example:

    $ ./dl\_fb\_files.py 666666666666666 CaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCCaaCC
4. The program will create a directory with the name of group id and place all the files from group there
