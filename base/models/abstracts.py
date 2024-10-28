from django.db import models
from base.mixins import MetadataPageMixin
from wagtail.models import Page
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, PageChooserPanel
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import truncatechars

class AbstractBannerPage(MetadataPageMixin, Page):
    ALIGN_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right')
    ]

    class Meta:
        abstract = True

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Banner Image"),
        help_text=_("A high quality banner image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    banner_title = models.CharField(max_length=255, verbose_name=_('Banner Title'), null=True)
    banner_subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Banner Subtitle'))
    banner_text = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Introduction Text'))
    call_to_action_button_text = models.CharField(max_length=100, blank=True, null=True,
                                                  verbose_name=_('Call to action button text'))
    call_to_action_related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Call to action related page')
    )

    align = models.CharField(max_length=50, choices=ALIGN_CHOICES, verbose_name=_("Align Content"), default="left")

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('banner_image'),
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
                FieldPanel('banner_text'),
                FieldPanel('call_to_action_button_text'),
                PageChooserPanel('call_to_action_related_page'),
                FieldPanel('align')
            ],
            heading=_("Banner Section"),
        )
    ]


    def save(self, *args, **kwargs):
        if not self.search_image and self.banner_image:
            self.search_image = self.banner_image

        if not self.search_description and self.banner_title:
            # Limit the search meta desc to Google's 160 recommended chars
            self.search_description = truncatechars(self.banner_title, 160)
        return super().save(*args, **kwargs)

