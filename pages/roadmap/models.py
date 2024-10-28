from django.utils.translation import gettext_lazy as _

# Create your models here.
from base.models import AbstractBannerPage
# Create your models here.

class RoadmapPage(AbstractBannerPage):
    template = "roadmap_page.html"

    parent_page_types= [
        'home.Homepage'
    ]

    max_count = 1

    class Meta:
        verbose_name= _("RoadMap Page")