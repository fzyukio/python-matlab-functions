rm -rf pymlfunc.egg-info
rm -rf dist/*
python setup.py sdist
twine upload dist/*
