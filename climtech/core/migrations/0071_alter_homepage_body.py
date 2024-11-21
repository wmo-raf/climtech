# Generated by Django 5.0.9 on 2024-11-15 12:01

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0070_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("get_started_block", 0),
                    ("headline", 9),
                    ("highlight", 13),
                    ("icon_bullets", 18),
                    ("logos", 21),
                    ("multiple_quotes", 27),
                    ("standalone_cta", 29),
                    ("teaser", 33),
                    ("video", 36),
                    ("map_block", 45),
                ],
                block_lookup={
                    0: (
                        "wagtail.snippets.blocks.SnippetChooserBlock",
                        ("core.GetStartedSnippet",),
                        {"icon": "th-list"},
                    ),
                    1: ("wagtail.blocks.CharBlock", (), {"max_length": 255}),
                    2: ("wagtail.blocks.TextBlock", (), {"required": False}),
                    3: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"label": "CTA text", "max_length": 255, "required": False},
                    ),
                    4: (
                        "wagtail.blocks.PageChooserBlock",
                        (),
                        {"label": "CTA page", "required": False},
                    ),
                    5: (
                        "wagtail.blocks.URLBlock",
                        (),
                        {"label": "CTA URL", "required": False},
                    ),
                    6: (
                        "wagtail.blocks.StructBlock",
                        [[("text", 3), ("cta_page", 4), ("cta_url", 5)]],
                        {},
                    ),
                    7: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                ("arrow-alt", "Arrow alt"),
                                ("arrow-in-circle", "Arrow in circle"),
                                ("arrow-in-square", "Arrow in square"),
                                ("arrows", "Arrows"),
                                ("blog", "Blog"),
                                ("bread", "Bread"),
                                ("briefcase", "Briefcase"),
                                ("building", "Building"),
                                ("calendar", "Calendar"),
                                ("code-file", "Code File"),
                                ("document", "Document"),
                                ("envelope", "Envelope"),
                                ("explanation", "Explanation"),
                                ("eye", "Eye"),
                                ("flame", "Flame"),
                                ("friends", "Friends"),
                                ("github", "Github"),
                                ("handshake", "Handshake"),
                                ("heart", "Heart"),
                                ("history", "History"),
                                ("id-card", "ID Card"),
                                ("image", "Image"),
                                ("knife-fork", "Knife Fork"),
                                ("leaf", "Leaf"),
                                ("location-pin", "Location Pin"),
                                ("map", "Map"),
                                ("magnifying-glass", "Magnifying Glass"),
                                ("money", "Money"),
                                ("moon", "Moon"),
                                ("one-two-steps", "One Two Steps"),
                                ("padlock", "Padlock"),
                                ("paper-plane", "Paper Plane"),
                                ("paper-stack", "Paper Stack"),
                                ("pen-checkbox", "Pen Checkbox"),
                                ("person-in-tie", "Person in Tie"),
                                ("python", "Python"),
                                ("question-mark-circle", "Question Mark Circle"),
                                ("quotes", "Quotes"),
                                ("release-cycle", "Release Cycle"),
                                ("roadmap", "Roadmap"),
                                ("rocket", "Rocket"),
                                ("rollback", "Rollback"),
                                ("slack", "Slack"),
                                ("speech-bubble", "Speech Bubble"),
                                ("sun-cloud", "Sun Cloud"),
                                ("table-tennis", "Table Tennis"),
                                ("tree", "Tree"),
                                ("wordpress", "Wordpress"),
                                ("world", "World"),
                            ],
                            "required": False,
                        },
                    ),
                    8: (
                        "wagtail.blocks.BooleanBlock",
                        (),
                        {"default": False, "required": False},
                    ),
                    9: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 1),
                                ("sub_heading", 2),
                                ("intro", 2),
                                ("cta", 6),
                                ("icon", 7),
                                ("dark_background", 8),
                            ]
                        ],
                        {},
                    ),
                    10: ("wagtail.blocks.CharBlock", (), {"max_length": 100}),
                    11: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                    12: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"max_length": 50, "required": False},
                    ),
                    13: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 10),
                                ("description", 2),
                                ("image", 11),
                                ("image_on_right", 8),
                                ("meta_text", 12),
                                ("meta_icon", 7),
                                ("cta", 6),
                            ]
                        ],
                        {},
                    ),
                    14: (
                        "wagtail.blocks.ChoiceBlock",
                        [],
                        {
                            "choices": [
                                ("arrow-alt", "Arrow alt"),
                                ("arrow-in-circle", "Arrow in circle"),
                                ("arrow-in-square", "Arrow in square"),
                                ("arrows", "Arrows"),
                                ("blog", "Blog"),
                                ("bread", "Bread"),
                                ("briefcase", "Briefcase"),
                                ("building", "Building"),
                                ("calendar", "Calendar"),
                                ("code-file", "Code File"),
                                ("document", "Document"),
                                ("envelope", "Envelope"),
                                ("explanation", "Explanation"),
                                ("eye", "Eye"),
                                ("flame", "Flame"),
                                ("friends", "Friends"),
                                ("github", "Github"),
                                ("handshake", "Handshake"),
                                ("heart", "Heart"),
                                ("history", "History"),
                                ("id-card", "ID Card"),
                                ("image", "Image"),
                                ("knife-fork", "Knife Fork"),
                                ("leaf", "Leaf"),
                                ("location-pin", "Location Pin"),
                                ("map", "Map"),
                                ("magnifying-glass", "Magnifying Glass"),
                                ("money", "Money"),
                                ("moon", "Moon"),
                                ("one-two-steps", "One Two Steps"),
                                ("padlock", "Padlock"),
                                ("paper-plane", "Paper Plane"),
                                ("paper-stack", "Paper Stack"),
                                ("pen-checkbox", "Pen Checkbox"),
                                ("person-in-tie", "Person in Tie"),
                                ("python", "Python"),
                                ("question-mark-circle", "Question Mark Circle"),
                                ("quotes", "Quotes"),
                                ("release-cycle", "Release Cycle"),
                                ("roadmap", "Roadmap"),
                                ("rocket", "Rocket"),
                                ("rollback", "Rollback"),
                                ("slack", "Slack"),
                                ("speech-bubble", "Speech Bubble"),
                                ("sun-cloud", "Sun Cloud"),
                                ("table-tennis", "Table Tennis"),
                                ("tree", "Tree"),
                                ("wordpress", "Wordpress"),
                                ("world", "World"),
                            ]
                        },
                    ),
                    15: (
                        "wagtail.blocks.RichTextBlock",
                        (),
                        {"features": ["bold", "italic", "link"], "required": False},
                    ),
                    16: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("icon", 14),
                                ("heading", 1),
                                ("description", 15),
                                ("cta", 6),
                            ]
                        ],
                        {},
                    ),
                    17: ("wagtail.blocks.ListBlock", (16,), {}),
                    18: (
                        "wagtail.blocks.StructBlock",
                        [[("icon_bullets", 17)]],
                        {"icon": "rectangle-list"},
                    ),
                    19: ("wagtail.blocks.CharBlock", (), {"required": False}),
                    20: ("wagtail.blocks.ListBlock", (11,), {}),
                    21: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 19), ("logos", 20)]],
                        {},
                    ),
                    22: ("wagtail.blocks.TextBlock", (), {"required": True}),
                    23: (
                        "wagtail.blocks.RichTextBlock",
                        (),
                        {"features": ["link"], "required": True},
                    ),
                    24: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"required": False},
                    ),
                    25: (
                        "wagtail.blocks.StructBlock",
                        [[("quote", 22), ("author", 23), ("author_image", 24)]],
                        {},
                    ),
                    26: ("wagtail.blocks.ListBlock", (25,), {"min_num": 2}),
                    27: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 22), ("quotes", 26)]],
                        {},
                    ),
                    28: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "label": "Short description",
                            "max_length": 100,
                            "required": False,
                        },
                    ),
                    29: (
                        "wagtail.blocks.StructBlock",
                        [[("cta", 6), ("description", 28)]],
                        {},
                    ),
                    30: (
                        "wagtail.blocks.PageChooserBlock",
                        (),
                        {"page_type": ["blog.BlogPage"], "required": False},
                    ),
                    31: ("wagtail.blocks.URLBlock", (), {"required": False}),
                    32: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {"label": "Subheading for external link", "required": False},
                    ),
                    33: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("page", 30),
                                ("url_chooser", 31),
                                ("image_for_external_link", 24),
                                ("heading_for_external_link", 2),
                                ("subheading_for_ext_link", 32),
                            ]
                        ],
                        {},
                    ),
                    34: (
                        "wagtailmedia.blocks.VideoChooserBlock",
                        (),
                        {"required": False},
                    ),
                    35: ("wagtail.embeds.blocks.EmbedBlock", (), {"required": False}),
                    36: (
                        "wagtail.blocks.StructBlock",
                        [[("heading", 19), ("video", 34), ("embed", 35)]],
                        {},
                    ),
                    37: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"max_length": 255, "required": True},
                    ),
                    38: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"max_length": 255, "required": False},
                    ),
                    39: (
                        "wagtail.blocks.RichTextBlock",
                        (),
                        {
                            "features": [
                                "bold",
                                "italic",
                                "h2",
                                "h3",
                                "ol",
                                "ul",
                                "link",
                                "document",
                            ],
                            "required": True,
                        },
                    ),
                    40: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"label": "Category Name", "max_length": 255, "required": True},
                    ),
                    41: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"help_text": "Hex code for category color", "required": True},
                    ),
                    42: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {
                            "choices": [
                                ("DZ", "Algeria"),
                                ("AO", "Angola"),
                                ("BJ", "Benin"),
                                ("BW", "Botswana"),
                                ("BF", "Burkina Faso"),
                                ("BI", "Burundi"),
                                ("CM", "Cameroon"),
                                ("CV", "Cape Verde"),
                                ("CF", "Central African Republic"),
                                ("TD", "Chad"),
                                ("KM", "Comoros"),
                                ("CG", "Congo - Brazzaville"),
                                ("CD", "Congo - Kinshasa"),
                                ("CI", "Côte d'Ivoire"),
                                ("DJ", "Djibouti"),
                                ("EG", "Egypt"),
                                ("GQ", "Equatorial Guinea"),
                                ("ER", "Eritrea"),
                                ("SZ", "Eswatini"),
                                ("ET", "Ethiopia"),
                                ("GA", "Gabon"),
                                ("GM", "Gambia"),
                                ("GH", "Ghana"),
                                ("GN", "Guinea"),
                                ("GW", "Guinea-Bissau"),
                                ("KE", "Kenya"),
                                ("LS", "Lesotho"),
                                ("LR", "Liberia"),
                                ("LY", "Libya"),
                                ("MG", "Madagascar"),
                                ("MW", "Malawi"),
                                ("ML", "Mali"),
                                ("MR", "Mauritania"),
                                ("MU", "Mauritius"),
                                ("MA", "Morocco"),
                                ("MZ", "Mozambique"),
                                ("NA", "Namibia"),
                                ("NE", "Niger"),
                                ("NG", "Nigeria"),
                                ("RW", "Rwanda"),
                                ("ST", "São Tomé and Príncipe"),
                                ("SN", "Senegal"),
                                ("SC", "Seychelles"),
                                ("SL", "Sierra Leone"),
                                ("SO", "Somalia"),
                                ("ZA", "South Africa"),
                                ("SS", "South Sudan"),
                                ("SD", "Sudan"),
                                ("TZ", "Tanzania"),
                                ("TG", "Togo"),
                                ("TN", "Tunisia"),
                                ("UG", "Uganda"),
                                ("ZM", "Zambia"),
                                ("ZW", "Zimbabwe"),
                            ],
                            "help_text": "Select one or multiple countries in Africa",
                        },
                    ),
                    43: (
                        "wagtail.blocks.StructBlock",
                        [[("category_name", 40), ("color", 41), ("countries", 42)]],
                        {},
                    ),
                    44: (
                        "wagtail.blocks.ListBlock",
                        (43,),
                        {"help_text": "Add one or more categories"},
                    ),
                    45: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("heading", 37),
                                ("subheading", 38),
                                ("description", 39),
                                ("categories", 44),
                            ]
                        ],
                        {},
                    ),
                },
            ),
        ),
    ]
