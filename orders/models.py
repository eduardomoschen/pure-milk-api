from django.db import models
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
import os
from os.path import join
from datetime import datetime
from products.models import Product
from sellers.models import Seller
from supermarkets.models import Supermarket


class Order(models.Model):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    supermarket = models.ForeignKey(Supermarket, on_delete=models.PROTECT)
    date_of_order = models.DateField(auto_now_add=True)
    invoicing = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"""{self.id} - {self.seller} - {self.supermarket}:
{self.date_of_order}"""

    def calculate_invoicing(self):
        total_invoicing = sum(
            item.calculate_item_invoicing() for item in self.order_items.all()
        )
        self.invoicing = total_invoicing

    def generate_pdf(self):
        date_of_order_formatted = self.date_of_order.strftime(
            '%d/%m/%Y'
        ) if self.date_of_order else ''

        save_directory = 'orders/orders_made'
        os.makedirs(save_directory, exist_ok=True)
        save_path = join(
            save_directory,
            f"""order_{self.seller.first_name}_{self.seller.last_name}_
{self.supermarket.name}_{self.date_of_order}.pdf"""
        )

        pdf = SimpleDocTemplate(
            save_path,
            pagesize=A4,
            rightMargin=8,
            leftMargin=8,
            topMargin=6,
            bottomMargin=6
        )

        story = []
        styles = getSampleStyleSheet()
        story.append(Spacer(1, 12))

        heading_style = ParagraphStyle(
            'Heading2',
            parent=styles['Heading2'],
            alignment=1,
        )

        story.append(
            Paragraph(
                f"""<b>PEDIDO {self.supermarket.name.upper()} -
{date_of_order_formatted}</b>""",
                heading_style
            )
        )
        story.append(Spacer(1, 12))

        now = datetime.now()
        current_datetime = now.strftime("%d/%m/%Y às %H:%M:%S")

        header_content_seller = [
            Paragraph(
                f"""<b>Vendedor:</b> {self.seller.first_name}
{self.seller.last_name}<br/>
<b>Telefone:</b> ({self.seller.phone_number[:2]})
{self.seller.phone_number[2:7]}-{self.seller.phone_number[7:]}<br/>
<b>E-mail:</b> {self.seller.email}<br/>""",
                styles['Normal']
            ),
        ]

        header_table_seller = Table(
            [header_content_seller],
            style=[('GRID', (0, 0), (-1, -1), 1, colors.white)]
        )
        story.append(header_table_seller)
        story.append(Spacer(1, 6))

        header_content = [
            Paragraph(
                f"""<b>Estabelecimento:</b> {self.supermarket.name}<br/>
<b>Telefone:</b> ({self.supermarket.phone_number[:2]})
{self.supermarket.phone_number[2:6]}-{self.supermarket.phone_number[6:]}<br/>
<b>Email:</b> {self.supermarket.email}<br/>
<b>Endereço:</b> {self.supermarket.adress}""",
                styles['Normal']
            ),
        ]

        header_table = Table(
            [header_content],
            style=[('GRID', (0, 0), (-1, -1), 1, colors.white)]
        )
        story.append(header_table)
        story.append(Spacer(1, 12))


        order_information = [
            [Paragraph(
                f"<b>Data do Pedido:</b> {date_of_order_formatted}",
                styles['Normal']
            )],
            [Paragraph(
                f"<b>Gerado em:</b> {str(current_datetime)}", styles['Normal']
            )],
            [Spacer(1, 12)],
        ]
        order_information_table = Table(
            order_information,
            style=[('GRID', (0, 0), (-1, -1), 1, colors.white)]
        )
        story.append(order_information_table)

        order_item_content_list = []
        for item in self.order_items.all():
            order_item_content_list.append([
                Paragraph(
                    f"<b>Produto:</b> {str(item.product.name)}",
                    styles['Normal']
                ),
                Paragraph(
                    f"<b>Quantidade:</b> {str(item.quantity)}",
                    styles['Normal']
                ),
            ])

        if order_item_content_list:
            order_items_table = Table(
                order_item_content_list,
                style=[('GRID', (0, 0), (-1, -1), 1, colors.white)]
            )
            story.append(order_items_table)
            story.append(Spacer(1, 4))

        total_amount_content = [
            [Paragraph(
                f"<b>Valor Total do Pedido:</b> R${self.invoicing}",
                styles['Normal']
            )],
        ]
        total_amount_table = Table(
            total_amount_content,
            style=[('GRID', (0, 0), (-1, -1), 1, colors.white)]
        )

        story.append(total_amount_table)
        pdf.build(story)

        return save_path

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.calculate_invoicing()
        self.generate_pdf()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def calculate_item_invoicing(self):
        return self.product.value * self.quantity
