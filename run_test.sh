export RUN_TEST_STORE=$1

export TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiJhZGJlZDE5MS0xZjNjLTQ2MDktYTM0YS02ODA1ZDk1Yjk4ZjYiLCJleHAiOjE2OTM1NDA4NDh9.zcNu9yR4GbbuSztK6_cPlNAPAa1gm6PYp4CfvcUrMRI'

# coverage run -m pytest -v --disable-pytest-warnings $2
python3 -m pytest