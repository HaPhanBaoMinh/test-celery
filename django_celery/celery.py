# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Line 3: You import the built-in os module, which you might be familiar with from working with files. You’ll use it in line 6 to set an environment variable.

# Line 4: You import Celery from the celery package. You’ll use it in line 7 to create your Celery application instance.

# Line 6: You use .setdefault() of os.environ to assure that your Django project’s settings.py module is accessible through the "DJANGO_SETTINGS_MODULE" key.

# Line 7: You create the Celery application instance and provide the name of the main module as an argument. In the context of your Django application, the main module is the Django app that contains celery.py, so you pass "django_celery".

# Line 8: You define the Django settings file as the configuration file for Celery and provide a namespace, "CELERY". You’ll need to preprend the namespace value, followed by an underscore (_), to every configuration variable related to Celery. You could define a different settings file, but keeping the Celery configuration in Django’s settings file allows you to stick with a single central place for configurations.

# Line 9: You tell your Celery application instance to automatically find all tasks in each app of your Django project. This works as long as you stick to the structure of reusable apps and define all Celery tasks for an app in a dedicated tasks.py module. You’ll create and populate this file for your django_celery app when you refactor the email sending code later.