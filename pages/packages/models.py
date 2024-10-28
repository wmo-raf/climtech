# Create your models here.
from django.utils.translation import gettext_lazy as _

from base.models import AbstractBannerPage
# Create your models here.

class PackagesPage(AbstractBannerPage):
    template = "packages_page.html"

    max_count = 1
    
    class Meta:
        verbose_name= _("Packages Page")