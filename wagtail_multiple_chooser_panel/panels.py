from django.core.exceptions import ImproperlyConfigured
from django.forms import Media
from wagtail.admin.panels import InlinePanel
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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.chooser_widget = self.formset.empty_form.fields[self.panel.chooser_field_name].widget
            self.js_context = JSContext()
            self.chooser_widget_telepath_definition = self.js_context.pack(self.chooser_widget)

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)
            context["chooser_field_name"] = self.panel.chooser_field_name
            context["chooser_widget_definition"] = self.chooser_widget_telepath_definition
            return context

        @property
        def media(self):
            return super().media + self.js_context.media + Media(js=[
                'wagtail_multiple_chooser_panel/js/wagtail-multiple-chooser-panel.js',
            ])
