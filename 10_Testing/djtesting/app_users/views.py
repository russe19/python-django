from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.formats import date_format
import datetime

def example(request, *args, **kwargs):
    return render(request, 'example.html')

def greatings(request, *args, **kwargs):
    greatings_message = _('Hello there! Today is %(date)s %(time)s') % {
        'date': date_format(datetime.datetime.now().date(), format='SHORT_DATE_FORMAT', use_l10n=True),
        'time': datetime.datetime.now().time(),
    }
    return render(request, 'greatings.html', context={
        'greatings_message': greatings_message
    })
