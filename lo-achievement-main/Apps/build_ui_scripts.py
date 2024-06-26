#### Makefile rule to convert all ui_nbs to ui_scripts

import glob, re, os
import nbformat

# Pattern we're looking for for cells to export
export_pattern  = r'^#\|\s*to_script(\n|$)'

# Get path of notebooks to read based on our current working directory
# Default behavior will be to call from lo_achievement using the Makefile, but if we're calling
# from the Apps directory, we need to add a path prefix
path_prefix = 'Apps/'
if os.getcwd().split('/')[-1] == 'Apps':
    path_prefix = ''

full_fpath = path_prefix + 'ui_nbs/*.ipynb'

# get list of ipynb in ui_nbs folder
ui_nbs = glob.glob(full_fpath)

# read the notebook
for nbfname in ui_nbs:
    in_nb = nbformat.read(nbfname, as_version=4)

    # pull out the relevant cells matching export_pattern using nbformat
    cells = [c for c in in_nb['cells'] if re.search(export_pattern, c['source'], re.IGNORECASE)]

    # write out file
    outfpath = nbfname.replace('.ipynb', '.py').replace('ui_nbs', 'ui_scripts')
    with open(outfpath, 'w') as f:
        f.write(f'###Autogenerated code from internal Makefile\n### Sourced from file: {nbfname}\n\n')
        for c in cells:
            f.write(c['source'])
            f.write('\n')
    
    # print out information
    print(f'Wrote {len(cells)} cells to {outfpath}')






