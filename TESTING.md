# The Tech SPot - Testing

![The Tech Spot. Screenshot of website]()

[View The Tech Spot on Heroku]()

## CONTENTS

- [Automated Testing](#Automated-Testing)
  - [W3C Validator](#W3C-Validator)
  - [JavaScript Validator](#JavaScript-Validator)
  - [Lighthouse Testing](#Lighthouse-Testing)
  - [Wave Testing](#Wave-Testing)
  - [CI Python Linter](#ci-python-linter)
- [Manual Testing](#Manual-Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Full Testing](#Full-Testing)
- [Bugs](#bugs)
  - [Solved Bugs](#solved-bugs)
  - [Known Bugs](#known-bugs)

## Testing

Testing was continuous throughout the website build. I used Chrome developer tools to identify and address any issues as they arose.

- My automated testing consisted of using W3C Validator, JSHint, Lighthouse, Wave the CI Linter Python and Coverage (Django Unit Testing).
- I then manually tested the user stories along with the functionality of the website.

## Automated Testing

### W3C Validator

### JavaScript Validator

All test successfully passed.

<details>
<summary>JS Hint Validator</summary>

## Checkout App

### stripe_elements.js

![stripe_element](documentation/images/the-tech-spot-checkout-stripe_element.js.png)

## Profiles App

### countryfield.js

![countryfield.js](documentation/images/the-tech-spot-profiles-countryfield.js.png)

</details>

### Lighthouse Testing

I took the opportunity to utilize Lighthouse within Chrome Developer Tools. This allowed me to test for performance, accessibility, best practices and the SEO (search engine optimization) of the website.

- All pages pass Googles lighthouse tests for Desktop and Mobile.

#### Desktop Testing

<details>
<summary>Lighthouse Desktop Testing Screen Shots</summary>

#### Homepage
![Homepage](documentation/images/the-tech-spot-homepage-lh.png)

#### Products Page
![Products Page](documentation/images/the-tech-spot-products.png)

#### Products Detail Page
![Products Detail Page](documentation/images/the-tech-spot-product_detail-page.png)

#### Add Product Page
![Add Product Page](documentation/images/the-tech-spot-add-product.png)

#### Edit Product
![Edit Product](documentation/images/the-tech-spot-edit-product.png)

#### Bag Page
![Bag Page](documentation/images/the-tech-spot-bag.png)

#### Checkout Page
![Checkout Page](documentation/images/the-tech-spot-checkout.png)

#### Checkout Success Page
![Checkout Success Page](documentation/images/the-tech-spot-checkout-success-lh.png)

#### Profile Page
![Profile Page](documentation/images/the-tech-spot-profile.png)

#### Contact Page
![Contact Page](documentation/images/the-tech-spot-contact.png)


</details>

#### Mobile Testing

<details>
<summary>Lighthouse Mobile Testing Screen Shots</summary>

#### Homepage
![Homepage](documentation/images/the-tech-spot-homepage-mobile.png)

#### Products Page
![Products Page](documentation/images/the-tech-spot-products-page-mobile.png)

#### Products Detail Page
![Products Detail Page](documentation/images/the-tech-spot-product_detail-page-mobile.png)

#### Add Product Page
![Add Product Page](documentation/images/the-tech-spot-add-product-mobile.png)

#### Edit Product
![Edit Product](documentation/images/the-tech-spot-edit-product-mobile.png)

#### Bag Page
![Bag Page](documentation/images/the-tech-spot-bag-mobile.png)

#### Checkout Page
![Checkout Page](documentation/images/the-tech-spot-checkout-mobile.png)

#### Checkout Success Page
![Checkout Success Page](documentation/images/the-tech-spot-checkout-success-mobile.png)

#### Profile Page
![Profile Page](documentation/images/the-tech-spot-profile-mobile.png)

#### Contact Page
![Contact Page](documentation/images/the-tech-spot-contact-mobile.png)

</details>

### Wave Testing

All pages pass the Wave validator.

<details>
<summary>Wave Testing</summary>

#### Homepage
![Homepage](documentation/images/the-tech-spot-home-page-wave.png)

#### Products Page
![Products Page](documentation/images/the-tech-spot-products-page-wave.png)

#### Products Detail Page
![Products Detail Page](documentation/images/the-tech-spot-product-detail-page-wave.png)

#### Add Product Page
![Add Product Page](documentation/images/the-tech-spot-add-product-page-wave.png)

#### Edit Product
![Edit Product](documentation/images/the-tech-spot-edit-product-page-wave.png)

#### Bag Page
![Bag Page](documentation/images/the-tech-spot-bag-page-wave.png)

#### Checkout Page
![Checkout Page](documentation/images/the-tech-spot-checkout-page-wave.png)

#### Checkout Success Page
![Checkout Success Page](documentation/images/the-tech-spot-checkout-success-page-wave.png)

#### Profile Page
![Profile Page](documentation/images/the-tech-spot-profile-page-wave.png)

#### Contact Page
![Contact Page](documentation/images/the-tech-spot-contact-page-wave.png)

</details>

### Coverage
<details>
<summary>Django Unit Testing Using Coverage</summary>

#### Coverage Testing

```bash
Name                                              Stmts   Miss  Cover
---------------------------------------------------------------------
bag\__init__.py                                       0      0   100%
bag\admin.py                                          1      0   100%
bag\apps.py                                           4      0   100%
bag\contexts.py                                      22      6    73%
bag\migrations\__init__.py                            0      0   100%
bag\models.py                                         1      0   100%
bag\templatetags\__init__.py                          0      0   100%
bag\templatetags\bag_tools.py                         6      2    67%
bag\test_views.py                                    23      0   100%
bag\urls.py                                           3      0   100%
bag\views.py                                         39     15    62%
checkout\__init__.py                                  1      0   100%
checkout\admin.py                                    12      0   100%
checkout\apps.py                                      6      0   100%
checkout\forms.py                                    28      0   100%
checkout\migrations\0001_initial.py                   6      0   100%
checkout\migrations\0002_alter_order_country.py       5      0   100%
checkout\migrations\0003_order_user_profile.py        5      0   100%
checkout\migrations\__init__.py                       0      0   100%
checkout\models.py                                   50     14    72%
checkout\signals.py                                   9      2    78%
checkout\test_forms.py                               22      0   100%
checkout\urls.py                                      4      0   100%
checkout\views.py                                    87     71    18%
checkout\webhook_handler.py                          74     58    22%
checkout\webhooks.py                                 28     19    32%
contact\__init__.py                                   0      0   100%
contact\admin.py                                      8      0   100%
contact\apps.py                                       4      0   100%
contact\forms.py                                     16      1    94%
contact\migrations\0001_initial.py                    5      0   100%
contact\migrations\__init__.py                        0      0   100%
contact\models.py                                    10      0   100%
contact\test_forms.py                                15      0   100%
contact\test_models.py                                9      0   100%
contact\test_views.py                                 6      0   100%
contact\urls.py                                       3      0   100%
contact\views.py                                     23     12    48%
env.py                                                5      0   100%
home\__init__.py                                      0      0   100%
home\admin.py                                         1      0   100%
home\apps.py                                          4      0   100%
home\migrations\__init__.py                           0      0   100%
home\models.py                                        1      0   100%
home\test_views.py                                    6      0   100%
home\urls.py                                          3      0   100%
home\views.py                                         3      0   100%
manage.py                                            11      2    82%
products\__init__.py                                  0      0   100%
products\admin.py                                     9      0   100%
products\apps.py                                      4      0   100%
products\forms.py                                    15      0   100%
products\migrations\0001_initial.py                   6      0   100%
products\migrations\__init__.py                       0      0   100%
products\models.py                                   21      0   100%
products\test_forms.py                                7      0   100%
products\test_models.py                              12      0   100%
products\test_views.py                               19      0   100%
products\urls.py                                      3      0   100%
products\views.py                                    88     61    31%
products\widgets.py                                   7      0   100%
profiles\__init__.py                                  0      0   100%
profiles\admin.py                                     1      0   100%
profiles\apps.py                                      4      0   100%
profiles\forms.py                                    18      1    94%
profiles\migrations\0001_initial.py                   8      0   100%
profiles\migrations\__init__.py                       0      0   100%
profiles\models.py                                   21      0   100%
profiles\test_models.py                               8      0   100%
profiles\test_views.py                               19      0   100%
profiles\urls.py                                      3      0   100%
profiles\views.py                                    26      6    77%
the_tech_spot\__init__.py                             0      0   100%
the_tech_spot\asgi.py                                 4      4     0%
the_tech_spot\settings.py                            46      0   100%
the_tech_spot\urls.py                                 5      0   100%
the_tech_spot\wsgi.py                                 4      4     0%
---------------------------------------------------------------------
TOTAL                                               927    278    70%
```
</details>

### CI Python Linter

- All Python code is consistent in style and conforms to the PEP8 style guide. The CI Python Linter has been used to check that the code conforms to PEP8 standard. This includes indentation, comments, trailing white spaces, maximum line length etc. 

- All tests successfully pass.

<details>
<summary>CI Python Linter Results</summary>

## The Tech Spot

### settings.py

![settings.py](documentation/images/the-tech-spot-settings.py.png)

### urls.py

![urls.py](documentation/images/the-tech-spot-urls.py.png)

## Bag App

### apps.py
![apps.py](documentation/images/the-tech-spot-bag-apps.py.png)

### bag_tools.py
![bag_tools.py](documentation/images/the-tech-spot-bag-bag_tools.py.png)

### context.py
![context.py](documentation/images/the-tech-spot-bag-contexts.py.png)

### test_views.py
![test_views.py](documentation/images/the-tech-spot-bag-test_views.py.png)

### urls.py
![urls.py](documentation/images/the-tech-spot-bag-urls.py.png)

### views.py
![views.py](documentation/images/the-tech-spot-bag-views.py.png)

## Checkout App

## admin.py
![admin.py](documentation/images/the-tech-spot-checkout-admin.py.png)

## apps.py
![apps.py](documentation/images/the-tech-spot-checkout-apps.py.png)

## forms.py
![forms.py](documentation/images/the-tech-spot-checkout-forms.py.png)

## signals.py
![signals.py](documentation/images/the-tech-spot-checkout-signals.py.png)

## models.py
![models.py](documentation/images/the-tech-spot-checkout-models.py.png)

## test_forms.py
![test_forms.py](documentation/images/the-tech-spot-checkout-test_forms.py.png)

## urls.py
![urls.py](documentation/images/the-tech-spot-checkout-urls.py.png)

## views.py
![views.py](documentation/images/the-tech-spot-checkout-views.py.png)

## webhook_handler.py
![webhook_handler.py](documentation/images/the-tech-spot-checkout-webhook_handler.py.png)

## webhooks.py
![webhooks.py](documentation/images/the-tech-spot-checkout-webhooks.py.png)

## Home App

## apps.py
![apps.py](documentation/images/the-tech-spot-home-apps.py.png)

## urls.py
![urls.py](documentation/images/the-tech-spot-home-urls.py.png)

## views.py
![views.py](documentation/images/the-tech-spot-home-views.py.png)

## test_views.py
![test_views.py](documentation/images/the-tech-spot-home-test_views.py.png)

## Products App

## admin.py
![admin.py](documentation/images/the-tech-spot-products-admin.py.png)

## apps.py
![apps.py](documentation/images/the-tech-spot-products-apps.py.png)

## forms.py
![forms.py](documentation/images/the-tech-spot-products-forms.py.png)

## models.py
![models.py](documentation/images/the-tech-spot-products-models.py.png)

## test_forms.py
![test_forms.py](documentation/images/the-tech-spot-products-test_forms.py.png)

## test_models.py
![test_models.py](documentation/images/the-tech-spot-products-test_models.py.png)

## test_views.py
![test_views.py](documentation/images/the-tech-spot-products-test_views.py.png)

## urls.py
![urls.py](documentation/images/the-tech-spot-products-urls.py.png)

## views.py
![views.py](documentation/images/the-tech-spot-products-views.py.png)

## widgets.py
![widgets.py](documentation/images/the-tech-spot-products-widgets.py.png)

## Profiles App

## apps.py
![apps.py](documentation/images/the-tech-spot-profiles-apps.py.png)

## forms.py
![forms.py](documentation/images/the-tech-spot-profiles-forms.py.png)

## models.py
![models.py](documentation/images/the-tech-spot-profiles-models.py.png)

## test_models.py
![test_models.py](documentation/images/the-tech-spot-profiles-test_models.py.png)

## test_views.py
![test_views.py](documentation/images/the-tech-spot-profiles-test_views.py.png)

## urls.py
![urls.py](documentation/images/the-tech-spot-profiles-urls.py.png)

## views.py
![views.py](documentation/images/the-tech-spot-profiles-views.py.png)

## Contact App

## admin.py
![admin.py](documentation/images/the-tech-spot-contact-admin.py.png)

## apps.py
![apps.py](documentation/images/the-tech-spot-contact-apps.py.png)

## forms.py
![forms.py](documentation/images/the-tech-spot-contact-forms.py.png)

## models.py
![models.py](documentation/images/the-tech-spot-contact-models.py.png)

## test_forms.py
![test_forms.py](documentation/images/the-tech-spot-contact-test_forms.py.png)

## test_models.py
![test_models.py](documentation/images/the-tech-spot-contact-test_models.py.png)

## test_views.py
![test_views.py](documentation/images/the-tech-spot-contact-test_views.py.png)

</details>

### Manual Testing

### Full Testing

Full testing was performed on the following devices:

- Laptop:

  - Macbook Pro 2015 13 inch screen

- Mobile Devices:
  - iPhone 15 pro.
  - iPhone 12 pro.
  - iPhone 11 pro.
  - Phone X.

Each device tested the site using the following browsers:

- Google Chrome
- Safari

## Bugs