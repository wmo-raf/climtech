from django.utils.translation import gettext_lazy as _
from wagtail import blocks

from config.settings.base import SUMMARY_RICHTEXT_FEATURES, FULL_RICHTEXT_FRATURES
from wagtail.images.blocks import ImageChooserBlock
from wagtailiconchooser.blocks import IconChooserBlock


class TitleTextBlock(blocks.StructBlock):

    ALIGN_TYPE_CHOICES = [
        ('left', 'Left'),
        ('center', 'Center'),
    ]

    title = blocks.CharBlock(max_length=100, verbose_name=_('Section Title'),
                             help_text=_("Section Title"), )
    text = blocks.RichTextBlock(features=FULL_RICHTEXT_FRATURES, verbose_name=_('Section Text'),
                                help_text=_("Section description"))
    action_link_text = blocks.CharBlock(max_length=15, required=False)
    action_link = blocks.PageChooserBlock(required=False, label=_("Action Link Internal"))
    action_link_external = blocks.URLBlock(required=False, max_length=400,
                                           help_text=_("An external link to a detailed resource on the internet."
                                                       "If provided, the internal link will be ignored"))
    dark_mode = blocks.BooleanBlock(bool=False, help_text="Switch Section to dark mode", required=True)
    align = blocks.ChoiceBlock(choices=ALIGN_TYPE_CHOICES, default='left')

    class Meta:
        template = "streams/title_text.html"
        icon = "placeholder"
        label = _("Title and Text")

class TitleTextImageBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=100, verbose_name=_('Section Title'),
                             help_text=_("Section Title"), )
    text = blocks.RichTextBlock(features=SUMMARY_RICHTEXT_FEATURES, verbose_name=_('Section Text'),
                                help_text=_("Section description"))
    image = ImageChooserBlock(required=True)
    action_link_text = blocks.CharBlock(max_length=15, required=False)
    action_link = blocks.PageChooserBlock(required=False, label=_("Action Link Internal"))
    action_link_external = blocks.URLBlock(required=False, max_length=400,
                                           help_text=_("An external link to a detailed resource on the internet."
                                                       "If provided, the internal link will be ignored"))
    dark_mode = blocks.BooleanBlock(bool=False, help_text="Switch Section to dark mode", required=True)
    img_postn = blocks.BooleanBlock(bool=False, help_text="Image before Text", required=True, verbose_name=_("Image Before Text"))

    class Meta:
        template = "streams/title_text_image.html"
        icon = "placeholder"
        label = _("Title, Text and Image")


class QuoteBlock(blocks.StructBlock):
    text = blocks.CharBlock(max_length=100, verbose_name=_('Quote Text'),
                             help_text=_("Quote Text"), )
    dark_mode = blocks.BooleanBlock(bool=False, help_text="Switch Section to dark mode", required=True)

    class Meta:
        template = "streams/quote.html"
        icon = "placeholder"
        label = _("Quote")


class CollapsibleBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    description = blocks.RichTextBlock(features=SUMMARY_RICHTEXT_FEATURES)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "streams/collapsible_block.html"
        icon = "placeholder"
        label = _("Collapsible Block")


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    collapsibles = blocks.StreamBlock([
        ('collapsibles', CollapsibleBlock())
    ])

    class Meta:
        template = "streams/accordion.html"
        icon = "placeholder"
        label = _("Accordion")


class CollapsibleTextBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=255)
    description = blocks.RichTextBlock(features=SUMMARY_RICHTEXT_FEATURES)
    link_text = blocks.CharBlock(max_length=100, required=False)
    link_related_page = blocks.PageChooserBlock(required=False)

    class Meta:
        template = "streams/collapsible_text_block.html"
        icon = "placeholder"
        label = _("Collapsible Text Block")


class FeatureBlock(blocks.StructBlock):

    image = ImageChooserBlock(required=False)
    
    title = blocks.CharBlock()
    text = blocks.RichTextBlock(label=_("Description"), features=SUMMARY_RICHTEXT_FEATURES)
    action_link_text = blocks.CharBlock(max_length=15, required=False)
    action_link = blocks.PageChooserBlock(required=False, label=_("Action Link Internal"))
    action_link_external = blocks.URLBlock(required=False, max_length=400,
                                           help_text=_("An external link to a detailed resource on the internet."
                                                       "If provided, the internal link will be ignored"))
    dark_mode = blocks.BooleanBlock(bool=False, help_text="Switch Section to dark mode", required=True)

    class Meta:
        template = "streams/feature_block.html"
        icon = "placeholder"
        label = _("Feature Block")


class FeatureGroupBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    features = blocks.StreamBlock([
        ('features', FeatureBlock())
    ])

    class Meta:
        template = "streams/feature_group_block.html"
        icon = "placeholder"
        label = _("Feature Block Group")

class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock(label=_("Description"), features=SUMMARY_RICHTEXT_FEATURES)
    action_link = blocks.PageChooserBlock(required=False, label=_("Action Link Internal"))
    action_link_external = blocks.URLBlock(required=False, max_length=400,
                                           help_text=_("An external link to a detailed resource on the internet."
                                                       "If provided, the internal link will be ignored"))
   
    dark_mode = blocks.BooleanBlock(bool=False, help_text="Switch Section to dark mode", required=True)



class TitleTextIconBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock(label=_("Description"), features=SUMMARY_RICHTEXT_FEATURES)
    action_link = blocks.PageChooserBlock(required=False, label=_("Action Link Internal"))
    action_link_external = blocks.URLBlock(required=False, max_length=400,
                                           help_text=_("An external link to a detailed resource on the internet."
                                                       "If provided, the internal link will be ignored"))
    class Meta:
        template = "streams/title_text_icon_include.html"
        icon = "placeholder"
        label = _("Title, Text and Icon Block")

class TitleTextIconGroupBlock(blocks.StructBlock):
    DISPLAY_CHOICES = [
        ('list', 'List'),
        ('grid', 'Grid')
    ]
    title = blocks.CharBlock()
    display = blocks.ChoiceBlock(choices=DISPLAY_CHOICES, default='grid')

    content = blocks.StreamBlock([
        ('content', TitleTextIconBlock())
    ])

    dark_mode = blocks.BooleanBlock(bool=False, help_text=_("Switch Section to dark mode"), required=True)

    class Meta:
        template = "streams/title_text_icon.html"
        icon = "placeholder"
        label = _("Title, Text and Icon Block Group")