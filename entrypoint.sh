@'
#!/bin/bash
set -e
python manage.py migrate
exec "$@"
'@ | Out-File -Encoding ASCII -NoNewline entrypoint.sh
