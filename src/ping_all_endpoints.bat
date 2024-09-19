REM - a utility file to actually hit the api endpoints - assumes that
REM the dev server is running on 127.0.0.1:8000 - and that the test
REM database exist with elements referenced in the ping files.

python tests/ping_FN022_endpoints.py AA
python tests/ping_FN026_endpoints.py AA
python tests/ping_FN026Subspace_endpoints.py AB
python tests/ping_FN028_endpoints.py AA
python tests/ping_FN121_endpoints.py 6565
python tests/ping_FN121GpsTrack_endpoints.py 55
python tests/ping_FN122_endpoints.py 55
python tests/ping_FN123_endpoints.py 161
python tests/ping_FN123Nonfish_endpoints.py 12345
python tests/ping_FN124_endpoints.py 55
python tests/ping_FN125_endpoints.py 6565
python tests/ping_FN125Lamprey_endpoint.py 12
python tests/ping_FN125Tag_endpoints.py 12
python tests/ping_FN126_endpoints.py 65
python tests/ping_FN127_endpoints.py 65
python tests/ping_GrEffProcType_endpoints.py  GL01
python tests/ping_StreamDimension_endpoints.py 0.5
