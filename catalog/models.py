from django.db import models
import uuid
from django.utils import timezone


# Create your models here.

class Services(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """

    servis_name = models.CharField(max_length=30, help_text='Название услуги')
    photo_id = models.CharField(max_length=20, unique=True, null=True, help_text='Id фото для отображения в карусели в ВК')

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):

        return '%s' % self.servis_name


class Customer(models.Model):
    First_name = models.CharField(max_length=100, help_text='Имя заказчика')
    Last_name = models.CharField(max_length=100, help_text='Фамилия заказчика')
    Phone_numb = models.CharField(max_length=100, help_text='Номер заказчика')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчик'
        ordering = ['Phone_numb']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s %s | %s' % (self.First_name, self.Last_name, self.Phone_numb)


class Servis_order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="ID заказа")



    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, verbose_name='Время поступления заказа')

    publish_at = models.DateTimeField(null=True, help_text='Время обновления', verbose_name='Время обновления')

    cust = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, help_text='Данные заказчика', verbose_name='Заказчик')

    Services = models.ForeignKey('Services', on_delete=models.SET_NULL, null=True, help_text='Заказаная услуга', verbose_name='Услуга')

    LOAN_STATUS = (
        ('Н', 'Новый'),
        ('Р', 'В работе'),
        ('В', 'Выполнен'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default=False, help_text='Статус заказа', verbose_name='Статус')

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        if self.status and self.publish_at is None:
            self.publish_at = timezone.now()
        elif not self.status and self.publish_at is not None:
            self.publish_at = None
        super(Servis_order, self).save(*args, **kwargs)

    def __str__(self):

        return 'id %s| %s %s | Дата заказа %s | %s | %s | Cтатус заказа %s' % (self.id, self.cust.First_name, self.cust.Last_name, self.publish_at, self.created_at,
                                                                          self.Services.servis_name, self.status)
