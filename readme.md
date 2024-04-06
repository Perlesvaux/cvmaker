# Turn a JSON file into a cv! 

##### Quick start!
```bash
# Initialize JSON representation of your CV 
cvmaker -w

# Redirect the ouput to a file!
cvmaker your_cv.json > index.html

# Customize its looks!
# i.e.: Image-size=2, Text-color=success, background-color=bg-success, flavor=quartz
cvmaker your_cv.json -i 2 -t warning -b border-dark -f quartz > index.html
```

Open the resulting HTML file. Now do CTRL+P to generate a PDF out of it! (i.e.: Destination -> **Save to PDF**) 
Use these settings for the best results.
- Orientation : Portrait
- Margins : None
- Scale : Default (or 'Fit to page width')


# CLI usage
##### 1) Initialize a JSON representation of your cv.
```bash
# Whole JSON (recommended)
cvmaker -w 
```

```bash
# Minimal JSON
cvmaker -n  
```

##### 2) Interactively add a new skill, experience, link or certificate:
```bash
cvmaker -a experience
```
##### 3) Update an existing entry with flags (Create, Entry, Property, Value):
```bash
cvmaker -c links -e 0 -p description -v "Updated description of 1st entry at links section"
```

```bash
cvmaker -c skills -e 1 -v "Updated skill!"
```

```bash
cvmaker -c name -v "John Doe"
```

# Installation
```bash
mkdir ~/bin
echo "export PATH=$PATH:$HOME/bin/" >> ~/.bashrc
git clone https://github.com/Perlesvaux/cvmaker
cd cvmaker
chmod +x cvmaker
ln -s $(realpath cvmaker) ~/bin/cvmaker

```

