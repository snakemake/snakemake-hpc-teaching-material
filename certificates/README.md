# Certificate Generator

This directory contains a script called 'certificate_generator'. Its purpose is to generate a PDF with one page per participant to issue certificates of attendance.

Call `./certificate_generator -h` to obtain help.

Allowed flags are:
- `--exportfile` - mandatory input, csv file of names
- `--date`       - the course date as indicate on the PDF, e.g. `--date="20. Feb. 2026"
- `--sign-date`  - your signature date - e.g. `--sign-date="25. March 2027"` - note that date and signature date may differ
- `--name-index` - the name index in the csv, default=1
- `--surname-index` - the surename index in the csv, default=0
