from django.db import models

from wagtail import blocks, fields
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.search import index

from climtech.services.blocks import SectionBlock


class ServicesPage(Page):
    parent_page_types = ["core.HomePage"]
    subpage_types = []
    intro = models.TextField(null=True, blank=True)
    body = fields.StreamField(
        blocks.StreamBlock(
            [("section", SectionBlock())],
            min_num=4,
            max_num=4,
        ),
        blank=False,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]
