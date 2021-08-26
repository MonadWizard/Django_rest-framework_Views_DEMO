viewser makes more easyer code structures then all class base view for principals. 😏

একই নাম এর একাধিক class এ mixins বা generic_view ব্যবহার করা যায় না। তাই DRF এ `viewSets` ব্যবহার করা হয়।

viewsets ব্যবহার করে same class এ multiple class base views operation করা যায়।

#### viewsets

views.py configure as:

    viewsets --------> ViewSet
        |                   |-----------Router
        |------------>ModelViewSet
        |
        |------------>ReadOnlyModelViewSet

-   viewsets.ViewSet call করলে list(), create(), retrieve(), update(), delete() এই সব function customly নিজে নিজে করতে হয়।
-   অথবা viewset.ModelViewSet call করলে automatic list(), create(), retrieve(), update(), delete() এই সব function execute করা যায়।
-   viewset.ReadOnlyModelViewSet ব্যবহার করে non-id or id base operation এর list() function execute করা যায়।

urls.py এর configuration different:

-   1st need to create a router. (drf provides `DefaultRouter`)
-   2nd register viewset. (`'url',views.YourViewClass`)
-   3rd diclar url inside urlpatterns which you expect. (`include(router.urls)`)
