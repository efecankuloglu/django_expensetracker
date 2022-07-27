from django.urls import path

from .views import MainPageView, update_expense, ExpenseDeleteView


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('update/<int:pk>/', update_expense, name='update_expense'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='delete_expense'),
]