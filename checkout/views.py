from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        # 'stripe_public_key': 'sk_test_51Jzr2fHmTUV1jLZyFuHYMnzw57YzM4eBIo7umDp7itPEx1dSXWSA7Fwi8Q9cnzlHXcYlCzqZnGJE7RMCx5ARqGpH003Lq0nI3G',
        'stripe_public_key': 'pk_test_51Jzr2fHmTUV1jLZyRMJFfHLtqputaOu5DoviFsb0KETFc2HvmcjTEqtpWiLRbL2aUlX5be8A37gabOUSJU1eiUMP00cMWT6Pv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
