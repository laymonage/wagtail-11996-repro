from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.documents.models import AbstractDocument, Document
from wagtail.blocks import RichTextBlock
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page


class HomePage(Page):
    body = StreamField(
        block_types=[
            ("doc", DocumentChooserBlock()),
            ("text", RichTextBlock()),
        ],
        blank=True,
    )
    rich = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [FieldPanel("body"), FieldPanel("rich")]


class CustomDocument(AbstractDocument):
    my = RichTextField()
    admin_form_fields = ("my",) + Document.admin_form_fields
