from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.snippets.models import register_snippet

from climtech.core.blocks import GetStartedBlock, MapBlock


@register_snippet
class GetStartedSnippet(models.Model):
    name = models.CharField(max_length=255)
    body = StreamField(
        [
            (
                "get_started_block",
                GetStartedBlock(),
            ),
        ],
        max_num=1,
        use_json_field=True,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("body"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Get started block"


@register_snippet
class SignupFormSnippet(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="For internal identification e.g 'This Week in ClimHub', 'TWIC'.",
    )
    heading = models.CharField(max_length=255)
    sub_heading = models.TextField(blank=True)
    mailchimp_account_id = models.CharField(
        verbose_name="Mailchimp Account ID", max_length=255, blank=True
    )
    mailchimp_newsletter_id = models.CharField(
        verbose_name="Mailchimp Audience ID", max_length=255, blank=True
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("heading"),
                FieldPanel("sub_heading"),
            ],
            "Title",
        ),
        MultiFieldPanel(
            [
                FieldPanel("mailchimp_account_id"),
                FieldPanel("mailchimp_newsletter_id"),
            ],
            "Mailchimp",
            classname="collapsible",
        ),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Signup form"




@register_snippet
class MapSnippet(models.Model):
    """Snippet to define a map block with heading, subheading, description, and categories."""
    name = models.CharField(max_length=255, null=True, blank=False)

    body = StreamField(
        [
            (
                "map_block",
                MapBlock(),
            ),
        ],
        use_json_field=True,
        max_num=1,
        null=True
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Map Block Snippet"
        verbose_name_plural = "Map Block Snippets"
