# Turn a JSON file into a cv! 

### Redirect the ouput to a file!
```bash
cvmaker your_cv.json > index.html
```

### Customize its looks! i.e.:
Image-size=2, Text-color=success, background-color=bg-success, flavor=quartz 
```bash
cvmaker your_cv.json -i 2 -t warning -b border-dark -f quartz > index.html
```

1) Initialize a JSON representation of your cv.
Whole JSON (recommended)
```bash
cvmaker -w 
```

Minimal JSON
```bash
cvmaker -n  
```

2) Add a new skill, experience, link or certificate:
```bash
cvmaker -a experience
```
3) Update an existing entry with flags {Create, Entry, Property, Value}:
```bash
cvmaker -c links -e 0 -p description -v "New value for description property on first entry under links section "
```

```bash
cvmaker -c skills -e 1 -v "Updated skill!"
```

```bash
cvmaker -c name -v "John Doe"
```


Open the resulting HTML file. Now do CTRL+P to generate a PDF out of it! (i.e.: Destination -> Save to PDF) 
Use these settings for the best results:
- Orientation -> Portrait
- Margins -> None
- Scale -> Default (or 'Fit to page width')
