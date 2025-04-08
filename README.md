# For Unix/macOS

python3 -m venv venv
source venv/bin/activate

# For Windows

python -m venv venv
venv\Scripts\activate

## Installing dependencies:

```python
pip install -r requirements.txt
```

you need to install tectonic
on unix/mac:

```sh
brew install tectonic
```

# TODO:

- [ ] Add scraping to get job descriptions
- [ ] Add "similarity" meter to check how qualified / good of a fit you are for a job
- [ ] Find resumes to test how resistant it is and figure out good ways to test tone and other things
