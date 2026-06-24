#!/bin/bash
# Deploy nirfsa wheel and test file to Windows testing location

# Activate venv
source /mnt/c/PythonRFSATesting/.venv/bin/activate

# Copy the wheel
cp /home/msaini/nimi-python/generated/nirfsa/dist/nirfsa-1.0.2.dev0-py3-none-any.whl /mnt/c/PythonRFSATesting/generated_nirfsa/dist/

# Copy the test file
cp /home/msaini/nimi-python/src/nirfsa/system_tests/test_system_nirfsa.py /mnt/c/PythonRFSATesting/src/nirfsa/system_tests/

# Copy samples2pfile.s2p if needed
cp /home/msaini/nimi-python/src/nirfsa/system_tests/samples2pfile.s2p /mnt/c/PythonRFSATesting/src/nirfsa/system_tests/

echo "Files copied to C:\PythonRFSATesting"
echo "Now run on Windows: C:\PythonRFSATesting\run_nirfsa_tests.bat"