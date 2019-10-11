from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Presentation
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  # register the plugin
class PresentationPluginPublisher(CMSPluginBase):
    model = Presentation  # model where plugin data are saved
    module = _("Presentation")
    name = _("Presentation Plugin")  # name of the plugin in the interface
    # render_template = "revealjs/index.html"
    render_template = "presentations/index.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context