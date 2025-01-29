@echo off
python manage.py shell -c "from phishing_app.models import CapturedData; CapturedData.objects.all().delete()"
echo All records deleted.
