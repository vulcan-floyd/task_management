export RUN_TEST_STORE=$1

export TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI1NWU5ZDFmNy1jMmE2LTRkNjAtOTMxZS1hOTEzMDg0MDJiOTgiLCJleHAiOjE2OTM1NjQ2ODF9.rJ9zmCS2s40asJ8nXXmpSdA4664Nh-dt-kglV5R956g'

# coverage run -m pytest -v --disable-pytest-warnings $2
python3 -m pytest