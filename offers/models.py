from django.db import models
from . import fields
from operator import iand, ior


class Offer(models.Model):
    coupon_code = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    short_description=models.CharField(max_length=50)

    popularity=models.IntegerField()
    description=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_from=models.DateTimeField()
    expire_at=models.DateTimeField()

    class Meta:
        ordering = ('popularity', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('offers:offer_detail', args=[self.id, self.slug])


class Discount(models.Model):
    """
    Abstract model representing one of several types of monetary
    reductions, as well as a date range they're applicable for, and
    the products and products in categories that the reduction is
    applicable for.
    """

    title = models.CharField(max_length=100)
    active = models.BooleanField(_("Active"), default=False)
    popularity=models.IntegerField()

    products = models.ManyToManyField("Product", blank=True,
                                      verbose_name=_("Products"))
    categories = models.ManyToManyField("Category", blank=True,
                                        related_name="%(class)s_related",
                                        verbose_name=_("Categories"))
    discount_deduct = fields.MoneyField(_("Reduce by amount"))
    discount_percent = fields.PercentageField(_("Reduce by percent"),
                                           max_digits=5, decimal_places=2,
                                           blank=True, null=True)
    max_user_usage=models.IntegerField()

    discount_exact = fields.MoneyField(_("Reduce to amount"))
    valid_from = models.DateTimeField(_("Valid from"), blank=True, null=True)
    valid_to = models.DateTimeField(_("Valid to"), blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def all_products(self):
        """
        Return the selected products as well as the products in the
        selected categories.
        """
        filters = [category.filters() for category in self.categories.all()]
        filters = reduce(ior, filters + [Q(id__in=self.products.only("id"))])
        return Product.objects.filter(filters).distinct()