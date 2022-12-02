from django.core.exceptions import ImproperlyConfigured
from django.forms import Media
from django.utils.functional import cached_property
from wagtail.admin.panels import InlinePanel
from wagtail.admin.staticfiles import versioned_static
from wagtail.telepath import JSContext


class MultipleChooserPanel(InlinePanel):
    def __init__(self, relation_name, chooser_field_name=None, **kwargs):
        if chooser_field_name is None:
            raise ImproperlyConfigured("MultipleChooserPanel must specify a chooser_field_name argument")

        self.chooser_field_name = chooser_field_name
        super().__init__(relation_name, **kwargs)

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs["chooser_field_name"] = self.chooser_field_name
        return kwargs

    class BoundPanel(InlinePanel.BoundPanel):
        template_name = "wagtail_multiple_chooser_panel/multiple_chooser_panel.html"

        @cached_property
        def chooser_widget(self):
            return self.formset.empty_form.fields[self.panel.chooser_field_name].widget

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)

            js_context = JSContext()
            chooser_widget_definition = js_context.pack(self.chooser_widget)

            context["chooser_widget_definition"] = chooser_widget_definition
            return context

        @property
        def media(self):
            return super().media + Media(
                js=[
                    versioned_static("wagtailadmin/js/telepath/telepath.js"),
                ],
            )
