pip install -r requirements.txt
py -m pip install --upgrade build
py -m build
python setup.py install
python setup.py build
pyinstaller mybackupy.py --distpath dist --onefile