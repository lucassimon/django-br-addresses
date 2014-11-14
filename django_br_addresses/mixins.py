# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible

# Third-party app imports
from django_extensions.db.models import TimeStampedModel
from localflavor.br.br_states import STATE_CHOICES
from uuslug import uuslug

# Imports from your apps


@python_2_unicode_compatible
class CityMixin(TimeStampedModel):
    u"""
    Model to define a info about a city
    """

    state = models.CharField(
        verbose_name=_(u'State'),
        max_length=2,
        choices=STATE_CHOICES
    )

    name = models.CharField(
        verbose_name=_(u'Name'),
        max_length=100
    )

    slug = models.CharField(
        verbose_name=_('Slug'),
        max_length=100
    )

    class Meta:
        abstract = True
        ordering = ('state', 'name')
        verbose_name = _(u'city')
        verbose_name_plural = _(u'cities')
        unique_together = ('name', 'state')

    def __unicode__(self):
        return u'{} - {}'.format(self.state, self.name)

    def __str__(self):
        return u'{} - {}'.format(self.state, self.name)

    def save(self, *args, **kw):
        slug = '{} {}'.format(self.state, self.name)
        self.slug = uuslug(slug, instance=self, start_no=1)
        super(CityMixin, self).save(*args, **kw)


@python_2_unicode_compatible
class AddressMixin(TimeStampedModel):
    """
    Model to define a address
    """

    zip_code = models.CharField(
        verbose_name=_('Zip Code'),
        max_length=9
    )

    neighborhood = models.CharField(
        max_length=200,
        verbose_name=_(u'Neighborhood'),
        default=u'center'
    )

    street = models.CharField(
        max_length=200,
        verbose_name=_(u'Street'),
        help_text=_(u'street or avenue or alley or highway ... plus a name')
    )

    number = models.IntegerField(
        verbose_name=_(u'Number'),
        default=1000
    )

    complement = models.TextField(
        blank=True,
        null=True,
        verbose_name=_(u'Complement')
    )

    class Meta:
        """
        Seta a ordenação da listagem pelo campo `created` ascendente
        Nome da app no singular e plural
        """
        abstract = True
        ordering = ['created']
        verbose_name = _(u'Address')
        verbose_name_plural = _(u'Addresses')

    def __unicode__(self):
        """
        Retorna o endereço
        como unicode.
        """
        return u'{}, {} - {} , {} , {}'.format(
            self.city.state,
            self.city.name,
            self.street,
            self.number,
            self.neighborhood,
        )

    def __str__(self):
        """
        Retorna o endereço
        como unicode.
        """
        return u'{}, {} - {} , {} , {}'.format(
            self.city.state,
            self.city.name,
            self.street,
            self.number,
            self.neighborhood,
        )
