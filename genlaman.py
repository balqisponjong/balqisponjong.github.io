#!/usr/bin/env python3
'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Monitoring KBM - Baitul Quran Ponjong</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>

<style>
html, body {
    height: 100%;
    margin: 0;
}
</style>

<body>
    <iframe src="https://script.google.com/macros/s/AKfycbz3F5ELoR-Du5gZRU_LklwGXDS41DGxLj8YoZNTqR08EpM_IV-i/exec?k=EDITAKUMAS" frameborder="0" scrolling="yes" seamless="seamless" style="display:block; width:100%; height:100vh;"></iframe>
</body>

</html>
'''

togen = ["7A", "7B", "7C", "8A", "8B", "9A", "9B", "10MIPA1", "10MIPA2"]

for i in togen:
    with open(f"pjj{i}.html", "w+") as f:
        f.write(__doc__.replace("EDITAKUMAS", i))
