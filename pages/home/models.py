from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from base import blocks
from base.models import AbstractBannerPage
# Create your models here.

class HomePage(AbstractBannerPage):
    template = "home/home_page.html"


    content = StreamField(
        [
            ("title_text", blocks.TitleTextBlock()),
            ("title_text_image", blocks.TitleTextImageBlock()),
            ("accordion", blocks.AccordionBlock()),
            ('feature_item', blocks.FeatureGroupBlock()),
            ('cta', blocks.CTABlock()),
            ('quote', blocks.QuoteBlock()),
            ('title_text_icons', blocks.TitleTextIconGroupBlock())
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    parent_page_type = [
        'wagtailcore.Page'
    ]
    max_count = 1

    content_panels = Page.content_panels + [
        *AbstractBannerPage.content_panels,
        FieldPanel("content")

    ]

    class Meta:
        verbose_name=_("Home Page")