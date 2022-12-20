from posy.models.product import Product
from posy.models.categories import Categories
from django.views.generic import ListView


class HomeView(ListView):
    model = Product
    paginate_by = 9
    context_object_name = "goods"
    template_name = "store.html"

    def get_queryset(self):
        if "choice" in self.request.GET:
            choice = self.request.GET["choice"]
            return Product.objects.filter(category_id=choice)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        return context
