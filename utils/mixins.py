from django.shortcuts import get_object_or_404

class OwnerMixin:
    """ expects standard url <[model name]_unid> to work with"""
    model = None

    def get_object(self,queryset=None):
        print("looking for get_object")
        model_name = self.model.__name__.lower()
        url_unid = "{}_unid".format(model_name)
        unid_ = self.kwargs.get(url_unid)
        obj = get_object_or_404(self.model,unid=unid_,user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj