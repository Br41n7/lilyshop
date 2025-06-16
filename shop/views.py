from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm
from .models import Category, Product
# from .recommender import Recommender
from site_settings.models import * 
from django.http import HttpRequest, HttpResponse
from typing import Optional, Dict, Any, List



def product_list(request: HttpRequest, category_slug: Optional[str] = None) -> HttpResponse:
    """
    Displays a list of available products, optionally filtered by category.

    Args:
        request: The incoming HttpRequest object.
        category_slug: The slug of the category to filter by (optional).

    Returns:
        An HttpResponse rendering the product list template.
    """
    language = request.LANGUAGE_CODE
    category: Optional[Category] = None

    # Fetch all categories. This is needed for the category navigation/list in the template.
    categories: List[Category] = Category.objects.all()

    # Start with all available products
    products = Product.objects.filter(available=True)

    # If a category slug is provided, filter products by that category
    if category_slug:
        # Fetch the specific category based on translated slug and language
        category = get_object_or_404(
            Category,
            translations__language_code=language,
            translations__slug=category_slug,
        )
        # Filter the products queryset by the fetched category
        products = products.filter(category=category)

    # Prepare the context dictionary for the template
    context: Dict[str, Any] = {
        'category': category,
        'categories': categories, # <-- UNCOMMENTED THIS LINE
        'products': products,
    }

    return render(
        request,
        'shop/product/list.html',
        context
    )


def product_detail(request: HttpRequest, id: int, slug: str) -> HttpResponse:
    """
    Displays the details of a single product.

    Args:
        request: The incoming HttpRequest object.
        id: The ID of the product.
        slug: The slug of the product.

    Returns:
        An HttpResponse rendering the product detail template.
    """
    language = request.LANGUAGE_CODE

    # Fetch the product based on ID, translated slug, and availability
    product = get_object_or_404(
        Product,
        id=id,
        translations__language_code=language,
        translations__slug=slug,
        available=True,
    )

    # Instantiate the form for adding the product to the cart
    cart_product_form = CartAddProductForm()

    # r = Recommender()
    # recommended_products = r.suggest_products_for([product], 4) # Suggest 4 products

    # Prepare the context dictionary for the template
    context: Dict[str, Any] = {
        'product': product,
        'cart_product_form': cart_product_form,
        # 'recommended_products': recommended_products,
    }

    return render(
        request,
        'shop/product/detail.html', # Assuming this is the correct template path
        context
    )



def home(request):
    products=Product.objects.all()
    hot_products=Product.objects.filter(is_hot=True)
    return render(request, 'shop/home.html',
                  {
                      'products':products,
                      'hot_products':hot_products,

                  })

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         language = request.LANGUAGE_CODE
#         category = get_object_or_404(
#             Category,
#             translations__language_code=language,
#             translations__slug=category_slug,
#         )
#         products = products.filter(category=category)
#     return render(
#         request,
#         'shop/product/list.html',
#         {
#             'category': category,
# #            'categories': categories,
#             'products': products,
#         },
#     )


# def product_detail(request, id, slug):
#     language = request.LANGUAGE_CODE
#     product = get_object_or_404(
#         Product,
#         id=id,
#         translations__language_code=language,
#         translations__slug=slug,
#         available=True,
#     )
#     cart_product_form = CartAddProductForm()
#     r = Recommender()
#     recommended_products = r.suggest_products_for([product], 4)
#     return render(
#         request,
#         'shop/product/detail.html',
#         {
#             'product': product,
#             'cart_product_form': cart_product_form,
#             'recommended_products': recommended_products,
#         },
#     )




    
