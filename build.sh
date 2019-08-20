conda activate mlenv
pip uninstall scratchml
cd module
python3 setup.py sdist bdist_wheel
cd dist
pip install scratchml-0.0.1-py3-none-any.whl
cd ..
cd ..
